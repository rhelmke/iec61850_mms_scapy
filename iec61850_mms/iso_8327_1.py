"""
Basic Scapy Definitions for the ISO 8327-1 session protocol

Source documents for these definitions:
    -   https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-ses.h
    -   https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-ses.c

Limited Support for:
    - User Data (DT)
    - Connect (CN)
    - Accept (AC)
    - A Dummy to skip multi-layered DT / GIVE-PDU
"""


from scapy.packet import Packet
from scapy.fields import ByteField, LenField, StrLenField, PacketField, FieldLenField, PacketListField


class ISO_8327_1_Session_Protocol_Parameter(Packet):
    name = "ISO 8327-1 Session Protocol Parameter"
    fields_desc = [ByteField("type", 0x05),
                   FieldLenField("length", None, fmt="B",
                                 length_of="parameter_value"),
                   StrLenField("value", None,
                               length_from=lambda x: x.length)]

    def extract_padding(self, s):
        return '', s


class ISO_8327_1_Session_User_Data(Packet):
    name = "ISO 8327-1 User Data"
    fields_desc = [ByteField("spdu_type", 193),
                   ByteField("length", None)]

    def extract_padding(self, s):
        return '', s


class ISO_8327_1_Session_Dummy(Packet):
    name = "ISO 8327-1 Dummy PDU"
    fields_desc = [ByteField("pdu_type", 1),
                   ByteField("length1", None),
                   ByteField("spdu_type", 1),
                   ByteField("length2", None)]


class ISO_8327_1_Session_Connect(Packet):
    name = "ISO 8327-1 Session Connect"
    fields_desc = [ByteField("spdu_type", 0x0d),
                   LenField("length", None,
                            fmt="!B", adjust=lambda pkt, x: len(pkt) + x),
                   PacketListField("parameters", None,
                                   ISO_8327_1_Session_Protocol_Parameter,
                                   count_from=lambda x: 4),
                   PacketField("user_data", None, ISO_8327_1_Session_User_Data)]


class ISO_8327_1_Session_Accept(Packet):
    name = "ISO 8327-1 Session Accept"
    fields_desc = [ByteField("spdu_type", 0x0e),
                   LenField("length", None,
                            fmt="!B", adjust=lambda pkt, x: len(pkt) + x),
                   PacketListField("parameters", None,
                                   ISO_8327_1_Session_Protocol_Parameter,
                                   count_from=lambda x: 3),
                   PacketField("user_data", None, ISO_8327_1_Session_User_Data)]


SPDU_TYPES = {
    0x0d: ISO_8327_1_Session_Connect,  # Connect SPDU (CN)
    0x0e: ISO_8327_1_Session_Accept,  # Accept SPDU (AC)
    0x01: ISO_8327_1_Session_Dummy,   # Dummy (in order to skip right to data)
}


class ISO_8327_1_Session(Packet):
    def guess_payload_class(self, payload):
        ln = len(payload)
        if ln < 1 or int(payload[0]) not in SPDU_TYPES:
            return self.default_payload_class(payload)
        return SPDU_TYPES[int(payload[0])]

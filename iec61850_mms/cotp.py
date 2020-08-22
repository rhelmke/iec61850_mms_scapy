"""
Basic Scapy Definitions for COTP (ISO 8327/X.225 - Connection-Oriented Transport Protocol)

Source documents for these definitions:
    -   https://www.itu.int/rec/T-REC-X.225-199511-I/en
    -   https://www.fit.vut.cz/research/publication-file/11832/TR-61850.pdf

Limited Support for:
    - Data (DT)
    - Connection Requests (CR)
    - Connection Responses (CC)
"""


from scapy.packet import Packet
from scapy.fields import ByteField, LenField, ShortField, StrLenField, \
                         BitField, PacketListField, FieldLenField


class COTP_Parameter(Packet):
    name = "COTP Parameter"
    fields_desc = [ByteField("code", None),
                   FieldLenField("length", None, fmt="B", length_of="value"),
                   StrLenField("value", None, length_from=lambda x: x.length)]

    def extract_padding(self, s):
        return '', s


class COTP_Connection_Request(Packet):
    name = "COTP Connection Request (CR)"
    fields_desc = [LenField("length", None, fmt="!B", adjust=lambda x: x + 5),
                   ByteField("tpdu_code", 0xd0),
                   ShortField("destination_reference", None),
                   ShortField("source_reference", None),
                   BitField("class", 0, 4),
                   BitField("reserved", 0, 2),
                   BitField("extended_format", 0, 1),
                   BitField("explicit", 0, 1),
                   PacketListField("parameters", None, COTP_Parameter)]


class COTP_Connection_Confirm(Packet):
    name = "COTP Connection Confirm (CC)"
    fields_desc = COTP_Connection_Request.fields_desc


class COTP_Data(Packet):
    name = "COTP Data (DT)"
    fields_desc = [ByteField("length", 2),
                   ByteField("tpdu_code", 0x0f),
                   BitField("last_data_unit", 1, 1),
                   BitField("tpdu_number", 0, 7)]


masked_tpdu_types = {
    0b1110: COTP_Connection_Request,  # CR
    0b1101: COTP_Connection_Confirm,  # CC
    # 0b0110: None, # AK, not required for MMS
    # 0b0101: None, # RJ, not required for MMS
}


fixed_tpdu_types = {
    # 0b10000000: None,  # DR, not required for MMS
    # 0b11000000: None,  # DC, not required for MMS
    0b11110000: COTP_Data,  # DT
    # 0b00010000: None,  # ED, not required for MMS
    # 0b00100000: None,  # EA, not required for MMS
    # 0b01110000: None,  # ER, not required for MMS
}


class COTP(Packet):
    def guess_payload_class(self, payload):
        ln = len(payload)
        if ln < 2:
            return self.default_payload_class(payload)
        tpdu_code = int(payload[1])
        cls = None

        if tpdu_code in fixed_tpdu_types:
            cls = fixed_tpdu_types[tpdu_code]

        if cls is not None:
            return cls
        tpdu_code >>= 0x04
        if tpdu_code in masked_tpdu_types:
            cls = masked_tpdu_types[tpdu_code]

        return cls if cls is not None else self.default_payload_class(payload)



from scapy.packet import Packet, Raw
from .mms import MMS
from .iso_8327_1 import ISO_8327_1_Session


class Pseudo_Layer(Packet):
    def guess_payload_class(self, payload):
        res = ISO_8327_1_Session().guess_payload_class(payload)
        return res if res != Raw else MMS

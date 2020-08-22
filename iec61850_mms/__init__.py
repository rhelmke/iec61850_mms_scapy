from . import tpkt
from . import cotp
from . import iso_8327_1
from . import iso_8823
from . import iso_8650_1

from .tpkt import TPKT
from .cotp import COTP_Data, COTP_Connection_Confirm, COTP, COTP_Connection_Request
from .iso_8327_1 import ISO_8327_1_Session, ISO_8327_1_Session_User_Data, ISO_8327_1_Session_Accept, \
    ISO_8327_1_Session_Connect
from .iso_8823 import ISO_8823_Presentation_CP_Type, ISO_8823_Presentation_CPA_Type, ISO_8823_Presentation_CPC_Type
from .iso_8650_1 import AARE, AARQ, ACSE
from .mms import MMS, MMS_Confirmed_Request_PDU, MMS_Initiate_Response_PDU, MMS_Initiate_Request_PDU


def bind_layers():
    from scapy.all import bind_layers
    from scapy.layers.inet import TCP
    from .iso_8327_1 import ISO_8327_1_Session_Dummy
    from ._internal import Pseudo_Layer
    # TPKT is nowadays above tcp and usually on port 102
    bind_layers(TCP, TPKT, sport=tpkt.TPKT_ISO_TSAP_PORT)
    bind_layers(TCP, TPKT, dport=tpkt.TPKT_ISO_TSAP_PORT)
    # cotp
    bind_layers(TPKT, COTP)
    # ISO 8327_1, Session establishment should be in a COTP Data PDU
    # YET!! MMS may be layered right on top of COTP in a minimized network stack... so bind the next layer to a
    # pseudo-layer that guesses the right class.
    bind_layers(COTP_Data, Pseudo_Layer)
    # ISO 8823, this is where it gets tricky...
    bind_layers(ISO_8327_1_Session_Accept, ISO_8823_Presentation_CPA_Type)
    bind_layers(ISO_8327_1_Session_Dummy, ISO_8823_Presentation_CPC_Type)
    bind_layers(ISO_8327_1_Session_Connect, ISO_8823_Presentation_CP_Type)
    # Up to ISO 8823, everything is a tidy scapy layer. However, all layers including and above ISO 8823 is ASN.1.
    # I didn't find another way than injecting ASN.1-defined PDUs into each other. Thus, everything above presentation
    # layer is a cluster of nested scapy ASN.1-engine objects. Harder to dissect in scripts :-/ any suggestions?

"""
Basic scapy asn.1 defintions for the ISO 8823 presentation layer

Source documents for these definitions:
    -   https://github.com/wireshark/wireshark/blob/master/epan/dissectors/asn1/atn-ulcs/atn-ulcs.asn
    -   https://github.com/mz-automation/libiec61850/blob/v1.4/src/mms/iso_presentation/iso_presentation.c

Supported types:
    - CP
    - CPA
    - CPC
"""

from .tags import *
from .ber import *
from .fields import *
from .types import *
from .packets import *

from .packets import ISO_8823_Presentation_CP_Type, ISO_8823_Presentation_CPA_Type, ISO_8823_Presentation_CPC_Type

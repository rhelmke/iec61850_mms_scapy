"""
ISO 8650-1 (ACSE) Tags

Tags from:
    -   https://www.itu.int/ITU-T/formal-language/itu-t/x/x227/1995/ACSE-1.html
"""
from scapy.asn1.asn1 import *


class ASN1_Tags_ACSE(ASN1_Class_UNIVERSAL):
    name = "ACSE"

    AARQ_TYPE_TAG = 0x60
    AARE_TYPE_TAG = 0x61
    APPLICATION_CONTEXT_NAME_TAG = 0xa1
    CALLED_AP_TITLE_FORM_2_TAG = 0xa2
    CALLED_AE_QUALIFIER_FORM_2_TAG = 0xa3
    CALLING_AP_TITLE_FORM_2_TAG = 0xa6
    CALLING_AE_QUALIFIER_FORM_2_TAG = 0xa7
    USER_INFORMATION_TAG = 0xbe
    EXTERNAL_T_TAG = 0x28
    AARE_RESULT_TYPE_TAG = 0xa2
    ACSE_SERVICE_USER_TAG = 0xa3
    INDIRECT_REFERENCE_TAG = 0x02
    MMS_DATA_TAG = 0xa0




# CP-type ::= SET {
#   mode-selector           [0] IMPLICIT Mode-selector, #### <-------- DONE
#   normal-mode-parameters #### <-------- CHECK
#     [2] IMPLICIT SEQUENCE {
#                            calling-presentation-selector  #### <-------- CHECK
#                              [1] IMPLICIT Calling-presentation-selector
#                                OPTIONAL,
#                            called-presentation-selector #### <-------- CHECK
#                              [2] IMPLICIT Called-presentation-selector OPTIONAL,
#                            presentation-context-definition-list  #### <-------- CHECK
#                              [4] IMPLICIT Presentation-context-definition-list
#                                OPTIONAL,
#                            user-data  #### <-------- CHECK
#                              User-data OPTIONAL} OPTIONAL
#   -- Shall be used for normal mode only.
#   -- Shall be the parameters of the CP PPDU.
# }


# CPA-PPDU ::= SET {
#   mode-selector           [0] IMPLICIT Mode-selector,
#   x410-mode-parameters
#     [1] IMPLICIT SET {COMPONENTS OF Reliable-Transfer-APDU.RTOACapdu} OPTIONAL--  This OPTIONAL element shall be absent for a
#   --  nested presentation connection.
#   --  Shall be used for X.410 mode only. Shall be bitwise
#   --  compatible with CCITT Recommendation X.410-1984.
#   --  This shall be the User data parameter of the CPA PPDU1) --,
#   normal-mode-parameters
#     [2] IMPLICIT SEQUENCE {protocol-version
#                              [0] IMPLICIT Protocol-version DEFAULT {version-1},
#                            responding-presentation-selector
#                              [3] IMPLICIT Responding-presentation-selector
#                                OPTIONAL,
#                            presentation-context-definition-result-list
#                              [5] IMPLICIT Presentation-context-definition-result-list
#                                OPTIONAL,
#                            presentation-requirements
#                              [8] IMPLICIT Presentation-requirements OPTIONAL,
#                            user-session-requirements
#                              [9] IMPLICIT User-session-requirements OPTIONAL,
#                            --  shall not be present if equal to the Revised session
#                            --  requirements parameter
#                            protocol-options
#                              [11]  Protocol-options DEFAULT {},
#                            --  shall be absent if no options are selected
#                            responders-nominated-context
#                              [13]  Presentation-context-identifier OPTIONAL,
#                            --  shall only be present if nominated-context is
#                            --  selected in protocol-options
#                            user-data
#                              User-data OPTIONAL} OPTIONAL
#   --  Shall be used for normal mode only.
# }

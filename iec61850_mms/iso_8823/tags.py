"""
ASN1 ISO 8823 scapy tag definitions

Values extracted from:
    -   https://github.com/mz-automation/libiec61850/blob/v1.4/src/mms/iso_presentation/iso_presentation.c
"""
from scapy.asn1.asn1 import *


class ASN1_Tags_ISO_8823(ASN1_Class_UNIVERSAL):
    name = "ISO 8823 OSI Presentation"

    CP_TYPE_TAG = 0x31
    MODE_SELECTOR_TAG = 0xa0
    CONTENT_TAG = 0xa0
    MODE_VALUE_TAG = 0x80
    NORMAL_MODE_PARAMETERS_TAG = 0xa2
    PRESENTATION_CONTEXT_IDENTIFIER_TAG = 0x02
    FULLY_ENCODED_DATA_TAG = 0x61
    PARSE_PCD_ENTRY_TAG = 0x30
    ABSTRACT_SYNTAX_NAME_TAG = 0x06
    TRANSFER_SYNTAX_NAME_TAG = 0x06
    CALLING_PRESENTATION_SELECTOR_TAG = 0x81
    CALLED_PRESENTATION_SELECTOR_TAG = 0x82
    RESPONDING_PRESENTATION_SELECTOR_TAG = 0x83
    PRESENTATION_CONTEXT_DEFINITION_LIST_TAG = 0xa4
    PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST_TAG = 0xa5
    RESULT_TAG = 0x80
    RESULT_LIST_TRANSFER_SYNTAX_TAG = 0x81
    USER_DATA_TAG = 0x61
    PDV_LIST_TAG = 0x30





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

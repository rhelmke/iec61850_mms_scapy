"""
ISO 8823 Packet/PDU Definitions
"""
from scapy.asn1packet import *
from .fields import *
from ..iso_8650_1 import ACSE, ASN1_Codecs
from ..mms import MMS


class ISO_8823_Presentation_PMV(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_SEQUENCE(
       ASN1F_PRESENTATION_CONTEXT_IDENTIFIER("presentation_context_identifier", 0),
    )


class ISO_8823_Presentation_Result(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_SEQUENCE(
        ASN1F_RESULT("result", 0),
        ASN1F_RESULT_LIST_TRANSFER_SYNTAX("transfer_syntax_name", None)
    )


class ISO_8823_Presentation_Definition(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_SEQUENCE(
        ASN1F_PRESENTATION_CONTEXT_IDENTIFIER("presentation_context_identifier", 0),
        ASN1F_ABSTRACT_SYNTAX_NAME("abstract_syntax_name", None),
        ASN1F_SEQUENCE(
            ASN1F_TRANSFER_SYNTAX_NAME("transfer_syntax_name", None)
        )
    )


class ISO_8823_Presentation_Fully_Encoded_Data(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_FULLY_ENCODED_DATA(
        ASN1F_SEQUENCE(
            ASN1F_PRESENTATION_CONTEXT_IDENTIFIER("presentation_context_identifier", 0),
            ASN1F_CONTENT(
                ASN1F_CHOICE(
                    "",
                    None,
                    ACSE,  # may contain ACSE -> MMS
                    MMS  # or direct MMS
                )
            )
        ),
    )


class ISO_8823_Presentation_CPC_Type(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_USER_DATA(
        "user_data",
        None,
        ISO_8823_Presentation_Fully_Encoded_Data
    )


class ISO_8823_Presentation_CPA_Type(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CP_TYPE(
        ASN1F_MODE_SELECTOR(
            ASN1F_MODE_VALUE("mode_value", 1),
        ),
        ASN1F_NORMAL_MODE_PARAMETERS(
            ASN1F_RESPONDING_PRESENTATION_SELECTOR("responding_presentation_selector", "\x00\x00\x00\x01"),
            ASN1F_PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST(
                "presentation_context_definition_result_list",
                None,
                ISO_8823_Presentation_Result
            ),
            ASN1F_USER_DATA(
                "user_data",
                None,
                ISO_8823_Presentation_Fully_Encoded_Data
            )
        )
    )


class ISO_8823_Presentation_CP_Type(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CP_TYPE(
        ASN1F_MODE_SELECTOR(
           ASN1F_MODE_VALUE("mode_value", 1),
        ),
        ASN1F_NORMAL_MODE_PARAMETERS(
            ASN1F_CALLING_PRESENTATION_SELECTOR("calling_presentation_selector", "\x00\x00\x00\x01"),
            ASN1F_CALLED_PRESENTATION_SELECTOR("called_presentation_selector", "\x00\x00\x00\x01"),
            ASN1F_PRESENTATION_CONTEXT_DEFINITION_LIST(
                "presentation_context_definition_list",
                None,
                ISO_8823_Presentation_Definition
            ),
            ASN1F_USER_DATA(
                "user_data",
                None,
                ISO_8823_Presentation_Fully_Encoded_Data
            )
        )
    )


class ISO_8823_Presentation(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CHOICE(
        "ISO 8823 Presentation",
        ISO_8823_Presentation_CP_Type(),  # default
        ISO_8823_Presentation_CP_Type,
    )

"""
MMS ASN1 Type Mappings
"""
from scapy.asn1.asn1 import *
from .tags import ASN1_Tags_ISO_8823


class ASN1_MODE_SELECTOR(ASN1_SET):
    tag = ASN1_Tags_ISO_8823.MODE_SELECTOR_TAG


class ASN1_NORMAL_MODE_PARAMETERS(ASN1_SEQUENCE):
    tag = ASN1_Tags_ISO_8823.NORMAL_MODE_PARAMETERS_TAG


class ASN1_MODE_VALUE(ASN1_INTEGER):
    tag = ASN1_Tags_ISO_8823.MODE_VALUE_TAG


class ASN1_CP_TYPE(ASN1_SET):
    tag = ASN1_Tags_ISO_8823.CP_TYPE_TAG


class ASN1_CALLING_PRESENTATION_SELECTOR(ASN1_STRING):
    tag = ASN1_Tags_ISO_8823.CALLING_PRESENTATION_SELECTOR_TAG


class ASN1_CALLED_PRESENTATION_SELECTOR(ASN1_STRING):
    tag = ASN1_Tags_ISO_8823.CALLED_PRESENTATION_SELECTOR_TAG


class ASN1_PRESENTATION_CONTEXT_IDENTIFIER(ASN1_INTEGER):
    tag = ASN1_Tags_ISO_8823.PRESENTATION_CONTEXT_IDENTIFIER_TAG


class ASN1_ABSTRACT_SYNTAX_NAME(ASN1_OID):
    tag = ASN1_Tags_ISO_8823.ABSTRACT_SYNTAX_NAME_TAG


class ASN1_TRANSFER_SYNTAX_NAME(ASN1_OID):
    tag = ASN1_Tags_ISO_8823.TRANSFER_SYNTAX_NAME_TAG


class ASN1_FULLY_ENCODED_DATA(ASN1_SEQUENCE):
    tag = ASN1_Tags_ISO_8823.FULLY_ENCODED_DATA_TAG


class ASN1_PDV_LIST(ASN1_SEQUENCE):
    tag = ASN1_Tags_ISO_8823.PDV_LIST_TAG


class ASN1_CONTENT(ASN1_SEQUENCE):
    tag = ASN1_Tags_ISO_8823.CONTENT_TAG


class ASN1_RESPONDING_PRESENTATION_SELECTOR(ASN1_STRING):
    tag = ASN1_Tags_ISO_8823.RESPONDING_PRESENTATION_SELECTOR_TAG


class ASN1_PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST(ASN1_SEQUENCE):
    tag = ASN1_Tags_ISO_8823.PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST_TAG


class ASN1_RESULT_LIST_TRANSFER_SYNTAX(ASN1_OID):
    tag = ASN1_Tags_ISO_8823.RESULT_LIST_TRANSFER_SYNTAX_TAG


class ASN1_RESULT(ASN1_INTEGER):
    tag = ASN1_Tags_ISO_8823.RESULT_TAG
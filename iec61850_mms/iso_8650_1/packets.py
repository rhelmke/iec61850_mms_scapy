"""
ISO 8650-1 (ACSE) Packet/PDU Definitions
"""
from scapy.asn1packet import *
from scapy.asn1.asn1 import ASN1_Codecs
from .fields import *
from ..mms import MMS


class CALLED_AP_TITLE_FORM_2(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CALLED_AP_TITLE_FORM_2("called_ap_title_form_2", None)


class CALLED_AE_QUALIFIER_FORM_2(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CALLED_AE_QUALIFIER_FORM_2("called_ae_qualifier_form_2", 0)


class CALLING_AP_TITLE_FORM_2(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CALLING_AP_TITLE_FORM_2("calling_ap_title_form_2", None)


class CALLING_AE_QUALIFIER_FORM_2(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CALLING_AE_QUALIFIER_FORM_2("calling_ae_qualifier_form_2", 0)


class ACSE_SERVICE_USER(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_ACSE_SERVICE_USER("service-user", 0, enum=[x for x in range(0, 15)])


class AARE(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_AARE_TYPE(
        ASN1F_APPLICATION_CONTEXT_NAME("application-context-name", None),
        ASN1F_AARE_RESULT_TYPE("result", 0, enum=[0, 1, 2]),
        ASN1F_CHOICE(
            "acse_service_user",
            None,
            ACSE_SERVICE_USER
        ),
        ASN1F_USER_INFORMATION(
            ASN1F_EXTERNAL_T(
                ASN1F_INDIRECT_REFERENCE("indirect_reference", 0),
                ASN1F_ACSE_MMS_DATA(
                    ASN1F_CHOICE(
                        "MMS PDU",
                        None,
                        MMS
                    )
                )
            ),
        )
    )


class AARQ(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_AARQ_TYPE(
        ASN1F_APPLICATION_CONTEXT_NAME("application-context-name", None),
        ASN1F_CHOICE(
            "called_ap_title",
            None,
            CALLED_AP_TITLE_FORM_2
        ),
        ASN1F_CHOICE(
            "called_ae_qualifier",
            None,
            CALLED_AE_QUALIFIER_FORM_2
        ),
        ASN1F_CHOICE(
            "calling_ap_title",
            None,
            CALLING_AP_TITLE_FORM_2
        ),
        ASN1F_CHOICE(
            "calling_ae_qualifier",
            None,
            CALLING_AE_QUALIFIER_FORM_2
        ),
        ASN1F_USER_INFORMATION(
            ASN1F_EXTERNAL_T(
                ASN1F_INDIRECT_REFERENCE("indirect_reference", 0),
                ASN1F_ACSE_MMS_DATA(
                    ASN1F_CHOICE(
                        "MMS PDU",
                        None,
                        MMS
                    )
                )
            ),
        )
    )


class ACSE(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CHOICE(
        "ACSE",  # name
        AARQ(),  # default
        AARQ,
        AARE
   )

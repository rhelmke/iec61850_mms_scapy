"""
MMS Packet/PDU Definitions
"""
from scapy.asn1packet import ASN1_Packet
from scapy.asn1.asn1 import ASN1_Codecs
from .fields import *


class MMS_VMD_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_VMD_SPECIFIC("vmd_specific", "")


class MMS_Domain_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DOMAIN_SPECIFIC(
        ASN1F_ISO646_STRING("domain_specific1", ""),
        ASN1F_ISO646_STRING("domain_specific2", "")
    )


class MMS_AA_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_AA_SPECIFIC("aa_specific", "".encode("ascii"))


class MMS_Name(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_NAME(
        ASN1F_CHOICE(
            '',
            MMS_VMD_Specific(),
            MMS_VMD_Specific(),
            MMS_Domain_Specific,
            MMS_AA_Specific
        )
    )


class MMS_Variable_Entry(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_SEQUENCE(
        ASN1F_CHOICE(
            "variableSpecification",
            None,
            MMS_Name,
        ),
    )


class MMS_List_Of_Variables(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_LIST_OF_VARIABLES(
        "listOfVariables",
        None,
        MMS_Variable_Entry
    )


class MMS_Variables_List_Names(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_VARIABLES_LIST_NAMES(
        ASN1F_CHOICE(
            "accessSpecificationVariablesListEntry",
            MMS_VMD_Specific(),
            MMS_VMD_Specific,
            MMS_Domain_Specific,
            MMS_AA_Specific
        )
    )


class MMS_VMD_state(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_VMD_STATE("vmd_state", 0)


class MMS_Object_Scope_VMD_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_OBJECT_SCOPE_VMD_SPECIFIC("objectScopeVMDSpecific", 0)


class MMS_Object_Scope_Domain_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_OBJECT_SCOPE_DOMAIN_SPECIFIC("objectScopeDomainSpecific", 0)


class MMS_Object_Scope_AA_Specific(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_OBJECT_SCOPE_AA_SPECIFIC("objectScopeAASpecific", 0)


class MMS_Object_Scope(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_OBJECT_SCOPE(
        ASN1F_CHOICE(
            "objectScope",
            MMS_Object_Scope_VMD_Specific(),
            MMS_Object_Scope_VMD_Specific,
            MMS_Object_Scope_Domain_Specific,
            MMS_Object_Scope_AA_Specific
        )
    )


class MMS_Basic_Object_Class(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_BASIC_OBJECT_CLASS("basicObjectClass", 0)


class MMS_Object_Class(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_OBJECT_CLASS(
        ASN1F_CHOICE(
            "objectClass",
            MMS_Basic_Object_Class(),
            MMS_Basic_Object_Class
        )
    )


class MMS_Get_Name_List_Request(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_GET_NAME_LIST_REQUEST(
        ASN1F_OBJECT_CLASS(
            ASN1F_CHOICE(
                "objectClass",
                MMS_Basic_Object_Class(),
                MMS_Basic_Object_Class
            )
        ),
        ASN1F_OBJECT_SCOPE(
            ASN1F_CHOICE(
                "objectScope",
                MMS_Object_Scope_VMD_Specific(),
                MMS_Object_Scope_VMD_Specific,
                MMS_Object_Scope_Domain_Specific,
                MMS_Object_Scope_AA_Specific
            )
        ),
    )


class MMS_Data_Boolean(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_BOOLEAN_("bool", False)


class MMS_Data_BitString(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_BIT_STRING("bit_string", None)


class MMS_Data_Int(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_INTEGER("integer", 0)


class MMS_Data_UInt(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_UNSIGNED("unsigned", 0)


class MMS_Data_Float(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_FLOATING_POINT("floating_point", 0)


class MMS_Data_OctetString(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_OCTET_STRING("data_octet", None)


class MMS_Data_VisibleString(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_VISIBLE_STRING("visible_str", "")


class MMS_Data_BinaryTime(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_BINARY_TIME("binary_time", None)


class MMS_Data_MMSString(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_MMS_STRING("mms_str", None)


class MMS_Data_UTCTime(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_DATA_TYPE_UTC_TIME("utc_time", None)


class MMS_Data(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CHOICE(
        'data',
        None,
        MMS_Data_Boolean,
        MMS_Data_BitString,
        MMS_Data_Int,
        MMS_Data_UInt,
        MMS_Data_Float,
        MMS_Data_OctetString,
        MMS_Data_VisibleString,
        MMS_Data_BinaryTime,
        MMS_Data_MMSString,
        MMS_Data_UTCTime
    )


class MMS_Write_Request(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_WRITE_REQUEST(
        ASN1F_CHOICE(
            "variableAccessSpecification",
            None,
            MMS_List_Of_Variables,
            MMS_Variables_List_Names
        ),
        ASN1F_LIST_OF_DATA(
            "listOfData",
            None,
            MMS_Data
        )
    )


class MMS_Read_Request(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_READ_REQUEST(
        ASN1F_optional(ASN1F_READ_REQUEST_SPECIFICATION_WITH_RESULT("specificationWithResult", False)),
        ASN1F_READ_REQUEST_VARIABLE_ACCESS_SPECIFICATION(
            ASN1F_CHOICE(
                "variableAccessSpecification",
                None,
                MMS_List_Of_Variables,
                MMS_Variables_List_Names
            ),
        )
    )


class MMS_Confirmed_Request_PDU(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CONFIRMED_REQUEST_PDU(
        ASN1F_INTEGER("invokeID", 0),
        ASN1F_CHOICE(
            "confirmedServiceRequest",
            MMS_Get_Name_List_Request(),
            MMS_Get_Name_List_Request,
            MMS_Read_Request,
            MMS_Write_Request,
        )
    )


class MMS_Initiate_Response_PDU(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_INITIATE_RESPONSE_PDU(
        ASN1F_LOCAL_DETAIL_CALLED("localDetailCalled", 0),
        ASN1F_NEGOTIATED_MAX_SERV_OUTSTANDING_CALLING("negotiatedMaxServOutstandingCalling", 0),
        ASN1F_NEGOTIATED_MAX_SERV_OUTSTANDING_CALLED("negotiatedMaxServOutstandingCalled", 0),
        ASN1F_NEGOTIATED_DATA_STRUCTURE_NESTING_LEVEL("negotiatedDataStructureNestingLevel", 0),
        ASN1F_MMS_INIT_RESPONSE_DETAIL(
            ASN1F_NEGOTIATED_VERSION_NUMBER("negotiatedVersionNumber", 0),
            ASN1F_NEGOTIATED_PARAMETER_CBB("negotiatedParameterCBB", None),
            ASN1F_SERVICES_SUPPORTED_CALLED("servicesSupportedCalled", None)
        )
    )


class MMS_Initiate_Request_PDU(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_INITIATE_REQUEST_PDU(
        ASN1F_LOCAL_DETAIL_CALLING("localDetailCalling", 0),
        ASN1F_PROPOSED_MAX_SERV_OUTSTANDING_CALLING("proposedMaxServOutstandingCalling", 0),
        ASN1F_PROPOSED_MAX_SERV_OUTSTANDING_CALLED("proposedMaxServOutstandingCalled", 0),
        ASN1F_PROPOSED_DATA_STRUCTURE_NESTING_LEVEL("proposedDataStructureNestingLevel", 0),
        ASN1F_MMS_INIT_REQUEST_DETAIL(
            ASN1F_PROPOSED_VERSION_NUMBER("proposedVersionNumber", 0),
            ASN1F_PROPOSED_PARAMETER_CBB("proposedParameterCBB", None),
            ASN1F_SERVICES_SUPPORTED_CALLING("servicesSupportedCalling", None)
        )
    )


class MMS(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CHOICE(
        "MMS",
        MMS_Confirmed_Request_PDU(),
        MMS_Confirmed_Request_PDU,
        MMS_Initiate_Request_PDU,
        MMS_Initiate_Response_PDU,
    )

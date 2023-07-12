from enum import Enum


class FormatName(str, Enum):
    CSV = "CSV"
    YAML = "YAML"
    TOML = "TOML"
    JSON = "JSON"
    XML = "XML"
    ASN_1 = "ASN.1"
    APACHE_AVRO = "Apache Avro"
    BSON = "BSON"
    CBOR = "CBOR"
    FLAT_BUFFERS = "FlatBuffers"
    FLEX_BUFFERS = "FlexBuffers"
    MICROSOFT_BOND = "Microsoft Bond"
    CAPTN_PROTO = "Capt'n Proto"
    MASSAGE_PACK = "MassagePack"
    PROCOLE_BUFFERS = "Protocol Buffers"
    APACHE_THRIFT = "Apache Thrift"
    SMILES = "Smile"
    UB_JSON = "UB JSON"
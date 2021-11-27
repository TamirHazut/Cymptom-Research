from marshmallow_dataclass import dataclass


@dataclass
class MetadataOptions:
    State: str
    HttpTokens: str
    HttpPutResponseHopLimit: int
    HttpEndpoint: str
    HttpProtocolIpv6: str
    
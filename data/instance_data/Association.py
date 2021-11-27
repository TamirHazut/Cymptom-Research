from marshmallow_dataclass import dataclass


@dataclass
class Association:
    IpOwnerId: str
    PublicDnsName: str
    PublicIp: str

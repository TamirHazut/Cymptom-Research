from marshmallow_dataclass import dataclass
from .Association import Association


@dataclass
class IpAddress:
    Association: Association
    Primary: bool
    PrivateDnsName: str
    PrivateIpAddress: str

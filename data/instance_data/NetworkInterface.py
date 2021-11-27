from marshmallow_dataclass import dataclass
from typing import List
from .Association import Association
from .Attachment import Attachment
from .Group import Group
from .IpAddress import IpAddress
from .Ipv6Addresses import Ipv6Address


@dataclass
class NetworkInterface:
    Association: Association
    Attachment: Attachment
    Description: str
    Groups: List[Group]
    InterfaceType: str
    Ipv6Addresses: List[Ipv6Address]
    MacAddress: str
    NetworkInterfaceId: str
    OwnerId: str
    PrivateDnsName: str
    PrivateIpAddress: str
    PrivateIpAddresses: List[IpAddress]
    SourceDestCheck: bool
    Status: str
    SubnetId: str
    VpcId: str

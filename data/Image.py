from marshmallow_dataclass import dataclass
from typing import List
from data.instance_data.BlockDeviceMapping import BlockDeviceMapping


@dataclass
class Image:
    Architecture: str
    CreationDate: str
    ImageId: str
    ImageLocation: str
    ImageType: str
    Public: bool
    OwnerId: str
    PlatformDetails: str
    UsageOperation: str
    State: str
    BlockDeviceMappings: List[BlockDeviceMapping]
    Description: str
    EnaSupport: bool
    Hypervisor: str
    ImageOwnerAlias: str
    Name: str
    RootDeviceName: str
    RootDeviceType: str
    SriovNetSupport: str
    VirtualizationType: str
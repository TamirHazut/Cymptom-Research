from marshmallow_dataclass import dataclass
from typing import List
import datetime
from ..instance_data.BlockDeviceMapping import BlockDeviceMapping
from ..instance_data.CapacityReservationSpecification import CapacityReservationSpecification
from ..instance_data.CpuOptions import CpuOptions
from ..instance_data.EnclaveOptions import EnclaveOptions
from ..instance_data.Group import Group
from ..instance_data.HibernationOptions import HibernationOptions
from ..instance_data.MetadataOptions import MetadataOptions
from ..instance_data.Monitoring import Monitoring
from ..instance_data.NetworkInterface import NetworkInterface
from ..instance_data.Placement import Placement
from ..instance_data.ProductCode import ProductCode
from ..instance_data.State import State
from ..instance_data.Tag import Tag


@dataclass
class Instance:
    AmiLaunchIndex: int
    Architecture: str
    BlockDeviceMappings: List[BlockDeviceMapping]
    CapacityReservationSpecification: CapacityReservationSpecification
    ClientToken: str
    CpuOptions: CpuOptions
    EbsOptimized: bool
    EnaSupport: bool
    EnclaveOptions: EnclaveOptions
    HibernationOptions: HibernationOptions
    Hypervisor: str
    ImageId: str
    InstanceId: str
    InstanceType: str
    KeyName: str
    LaunchTime: datetime.datetime
    MetadataOptions: MetadataOptions
    Monitoring: Monitoring
    NetworkInterfaces: List[NetworkInterface]
    PrivateDnsName: str
    PrivateIpAddress: str
    ProductCodes: List[ProductCode]
    Placement: Placement
    PlatformDetails: str
    PublicDnsName: str
    PublicIpAddress: str
    RootDeviceName: str
    RootDeviceType: str
    SecurityGroups: List[Group]
    SourceDestCheck: bool
    State: State
    StateTransitionReason: str
    SubnetId: str
    Tags: List[Tag]
    VirtualizationType: str
    VpcId: str
    UsageOperation: str
    UsageOperationUpdateTime: datetime.datetime

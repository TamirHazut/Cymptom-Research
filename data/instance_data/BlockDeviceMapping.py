from marshmallow_dataclass import dataclass
from typing import List
from .Ebs import Ebs


@dataclass
class BlockDeviceMapping:
    DeviceName: str
    Ebs: Ebs

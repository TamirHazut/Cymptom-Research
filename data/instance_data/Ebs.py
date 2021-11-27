from marshmallow_dataclass import dataclass


@dataclass
class Ebs:
    AttachTime: str = ''
    DeleteOnTermination: bool = False
    Encrypted: bool = False
    Status: str = ''
    SnapshotId: str = ''
    VolumeId: str = ''
    VolumeSize: int = 0
    VolumeType: str = ''

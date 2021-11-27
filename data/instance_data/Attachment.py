from marshmallow_dataclass import dataclass


@dataclass
class Attachment:
    AttachTime: str
    AttachmentId: str
    DeleteOnTermination: bool
    DeviceIndex: int
    Status: str
    NetworkCardIndex: int

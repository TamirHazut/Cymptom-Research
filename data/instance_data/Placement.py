from marshmallow_dataclass import dataclass


@dataclass
class Placement:
    AvailabilityZone: str
    GroupName: str
    Tenancy: str

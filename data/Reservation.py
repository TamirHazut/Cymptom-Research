from data.instance_data.Group import Group
from typing import List
from .reservation_data.Instance import Instance
from marshmallow_dataclass import dataclass


@dataclass
class Reservation:
    Groups: List[Group]
    Instances: List[Instance]
    OwnerId: str
    ReservationId: str

from marshmallow_dataclass import dataclass


@dataclass
class CapacityReservationSpecification:
    CapacityReservationPreference: str

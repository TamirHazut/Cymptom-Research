from marshmallow import fields
from marshmallow_dataclass import dataclass


@dataclass(eq=True)
class Region:
    Endpoint: str
    RegionName: str
    OptInStatus: str

    def __hash__(self):
        return hash((self.RegionName, self.Endpoint))

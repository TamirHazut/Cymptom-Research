from marshmallow_dataclass import dataclass


@dataclass
class ProductCode:
    ProductCodeId: str
    ProductCodeType: str

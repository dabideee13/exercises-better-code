import string
import random


class VehicleInfo:

    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, electric, catalogue_price) -> None:
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:

    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self) -> None:
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self) -> None:
        self.add_vehicle_info("Test Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)

    def generate_vehicle_id(self, length) -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_license_plate(self, id) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand) -> None:
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_license_plate(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: str):
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)
        vehicle.print()


def main():
    app = Application()
    app.register_vehicle("Volkswagen ID3")


if __name__ == '__main__':
    main()

from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def turn_off(self) -> None:
        raise NotImplementedError


class LightBulb(Switchable):
    def turn_on(self) -> None:
        print("LightBulb: turned on...")

    def turn_off(self) -> None:
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self) -> None:
        print("Fan: turned on...")

    def turn_off(self) -> None:
        print("Fan: turned off...")


class ElectricPowerSwitch:

    def __init__(self, light_bulb: LightBulb) -> None:
        self.light_bulb = light_bulb
        self.on = False

    def press(self) -> None:
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


def main():
    light_bulb = LightBulb()
    fan = Fan()
    switch = ElectricPowerSwitch(light_bulb)
    switch2 = ElectricPowerSwitch(fan)
    switch.press()
    switch.press()
    switch2.press()
    switch2.press()


if __name__ == '__main__':
    main()

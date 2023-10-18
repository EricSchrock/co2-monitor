from machine import I2C, Pin

class ENS160:
    def __init__(self, i2c: int = 0, scl: str = "GP17", sda: str = "GP16"):
        self.i2c = I2C(i2c, scl=Pin(scl), sda=Pin(sda))

    def _read(self, reg: int, size: int):
        return int.from_bytes(self.i2c.readfrom_mem(0x53, reg, size), 'little')

    def _write(self, reg: int, value: bytes, size: int):
        self.i2c.writeto_mem(0x53, reg, value.to_bytes(size, 'little'))

    def opmode(self, mode=None) -> int:
        if mode is not None:
            self._write(0x10, mode, 1)
            return mode
        else:
            return self._read(0x10, 1)

    def status(self) -> int:
        return self._read(0x20, 1)

    def aqi(self) -> int:
        return self._read(0x21, 1)

    def tvoc(self) -> int:
        return self._read(0x24, 2)

    def eco2(self) -> int:
        return self._read(0x24, 2)

import viam_wrap
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from typing import Mapping, Self
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
import time
import board
import busio
import adafruit_mpr121

class MPR121(Sensor):
    MODEL = "michaellee1019:mpr121:mpr121"
    # Create MPR121 object.
    mpr121: adafruit_mpr121.MPR121 = None

    @classmethod
    def new(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        output = self(config.name)
        output.reconfigure(config, dependencies)
        return output

    def reconfigure(self,
                    config: ComponentConfig,
                    dependencies: Mapping[ResourceName, ResourceBase]):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.mpr121 = adafruit_mpr121.MPR121(i2c)

    async def get_readings(self, **kwargs):
        return self.mpr121


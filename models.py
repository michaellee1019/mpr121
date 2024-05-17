import viam_wrap
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from typing import Mapping, Self
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
import sys
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

        i2c_address: int = 0x5A
        if "i2c_address" in config.attributes.fields:
            i2c_address = int(config.attributes.fields["i2c_address"].string_value, base=16)

        self.mpr121 = adafruit_mpr121.MPR121(i2c=i2c, address=i2c_address)

    async def get_readings(self, **kwargs):
        return {"touchpads": [t.value for t in self.mpr121]}

if __name__ == '__main__':
    # necessary for pyinstaller to see it
    # build this with: 
    # pyinstaller --onefile --hidden-import viam-wrap --paths $VIRTUAL_ENV/lib/python3.10/site-packages installable.py 
    # `--paths` arg may no longer be necessary once viam-wrap is published somewhere
    # todo: utility to append this stanza automatically at build time
    viam_wrap.main(sys.modules.get(__name__))
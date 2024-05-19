# mpr121
A Viam module that returns sensor values from a capacitive touch sensor device with the MPR121 chip.

# Attributes
No configuration attributes are required if your device operates on the i2c address of `0x5A`. Otherwise you can configure a different address using the config example below. The module is built assuming the default I2C bus.

```json
{
  "i2c_address": "0x5A"
}
```

# GetReadings
The Sensor.GetReadings response will look like the following. A touchpads array contains the status of each pad/input to the device. True means that it is being touched, false means untouched. In the below example, input 0 is touched and 1-11 is untouched.

```json
	
{
  "touchpads": [
    true,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false
  ]
}

```

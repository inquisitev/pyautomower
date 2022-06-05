

Emergency Stop
- Start with motor power at `1`, receive `EMERGENCY_STOP`, check that motor power is `0`
- Start with motor power at `0`, receive `EMERGENCY_STOP`, check that motor power is `0`
- Start with motor power at -1, receive `EMERGENCY_STOP`, check that motor power is `0`

Standard Operation (fresh init each test)
- Receive `IMU_HEADING_UPDATE { id, 0, 0, 0 }` then Receive `TURN_COMMAND{ id, 30, 5 }`, while `IMU_HEADING_UPDATE->yaw` is not nearly equal `30`, left motor command should be greater than `0`, right motor command should be less than `0`. should also receive interpolated values for `IMU_HEADING_UPDATE`. when `IMU_HEADING_UPDATE { id, 30, 0, 0 }` is received, motor power should go to `0`. 

- Receive `IMU_HEADING_UPDATE { id, 0, 0, 0 }` then Receive `TURN_COMMAND{ id, -30, 5 }`, while `IMU_HEADING_UPDATE->yaw` is not nearly equal `30`, left motor command should be less than `0`, right motor command should be greater than `0`. should also receive interpolated values for `IMU_HEADING_UPDATE`. when `IMU_HEADING_UPDATE { id, -30, 0, 0 }` is received, motor power should go to `0`. 

- Receive `DRIVE_COMMAND{id, 0, 1, 3}`, left motor command and right motor command should be greater than `0` until `WHEEL_ENCODER_VALUE->leftEncoderValue` is nearly `3.0` and`WHEEL_ENCODER_VALUE->rightEncoderValue` is nearly `3.0`, then left motor command and right motor command should equal `0`

- Receive `DRIVE_COMMAND{id, 0, 1, 3}`, left motor command and right motor command should be greater than `0`, then receive IMU_HEADING_UPDATE{ id, 3, 0, 0}. left motor command should be greater than `0`, right motor command should be greater than left motor command as a response to IMU_HEADING_UPDATE. 

- Receive `DRIVE_COMMAND{id, 0, 1, 3}`, Receive `DRIVE_COMMAND{id, 0, 1, 3}` left motor command and right motor command should be greater than `0` until `WHEEL_ENCODER_VALUE->leftEncoderValue` is nearly `3.0` and`WHEEL_ENCODER_VALUE->rightEncoderValue` is nearly `3.0`, then left motor command and right motor command should equal `0`. The left and right motor should once again be greater than 0 again until `WHEEL_ENCODER_VALUE->leftEncoderValue` is nearly `6.0` and`WHEEL_ENCODER_VALUE->rightEncoderValue` is nearly `6.0`. then the left and right motor power should be `0`.

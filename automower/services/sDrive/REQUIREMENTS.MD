## Requirements

### Event Bus 
- [ ] This service shall connect to sEventBus
- [ ] Upon disconnection from sEventBus, this service will invoke `EMERGENCY_STOP`
### Incoming Events
- [ ] This service shall listen to :
        `EMERGENCY_STOP`,
        `TURN_COMMAND`,
        `DRIVE_COMMAND`,
        `IMU_HEADING_UPDATE`,
        `IMU_CRASH_EVENT` , and
        `MANUAL_DRIVE_COMMAND`

- [ ] `EMERGENCY_STOP` [ON RECEIVE] => stop all motors. recovery on power cycle. 
- [ ] `TURN_COMMAND` [ON RECEIVE] => turn until `IMU_HEADING_UPDATE->yaw` is nearly equal to `IMU_HEADING_UPDATE->yaw` + `TURN_COMMAND->headingOffset` using shortest path. interruptable by `EMERGENCY_STOP` only. queued if other request active
- [ ] `DRIVE_COMMAND` [ON_RECEIVE] => drive until distance recorded by encoders is nearly equal to `DRIVE_COMMAND->distance`, while maintaining that `IMU_HEADING_UPDATE->yaw` is nearly equal to `DRIVE_COMMAND->headingToMaintain`. interruptable by `EMERGENCY_STOP`) only. queued if other request active
- [ ] `IMU_HEADING_UPDATE` [ON_RECEIVE] => should be simply cached for usage in `TURN_COMMAND` AND `DRIVE_COMMAND`
- [ ] `IMU_CRASH_EVENT` [ON_RECEIVE] => stop all motors. recovery on power cycle.
- [ ] `MANUAL_DRIVE_COMMAND` [ON_RECEIVE] => Direct control over motor power, override `IMU_CRASH_EVENT`

### Outgoing Events
- [ ] This service shall broadcast:
        `IDENTITY_CLAIM`,
        `MOTOR_STATE`, and
        `WHEEL_ENCODER_VALUE`

- [ ] `IDENTITY_CLAIM` shall be broadcast on connection to `sEventBus`. `IDENTITY->processName` shall be `sDrive`. `IDENTITY->key` shall be a randomly generated string. `IDENTITY` shall be cached for later use. 
- [ ] `MOTOR_STATE` shall broadcast with `MOTOR_STATE->leftPower` as `currentLeftPower`, `MOTOR_STATE->rightPower` as `currentRightPower`, and `MOTOR_STATE->sender` as cached identity.
- [ ] `WHEEL_ENCODER_VALUE` shall broadcast with `WHEEL_ENCODER_VALUE->leftEncoderValue` as `currentLeftEncoderValue`, `WHEEL_ENCODER_VALUE->leftEncoderValue` as `currentRightEncoderValue`, and `MOTOR_STATE->sender` as cached identity.
### Sensor Inputs
- [ ] Encoders shall be used to record and maintain velocity target

### Actuator Outputs
- [ ] Motor power shall be commanded using [RoboClaw](https://resources.basicmicro.com/using-the-roboclaw-python-library/) python library

### Data Processing
- [ ] when executing DRIVE_COMMAND Motor power shall be computed the sum of two PID control algorithms, HEADING and VELOCITY
- [ ] when executing TURN_COMMAND motor power shall be computed by TURNING pid control algorithms

### Calibration
- [ ] PID parameters retrieved from sPersist

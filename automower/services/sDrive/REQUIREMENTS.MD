### Requirements

- [ ] This service shall connect to sEventBus
- [ ] This service shall use [RoboClaw](https://resources.basicmicro.com/using-the-roboclaw-python-library/) python library 
- [ ] Upon disconnection from sEventBus, this service will send EMERGENCY_STOP event
- [ ] Upon disconnection from sEventBus, this service will set motor power to 0 using roboclaw library. 
- [ ] This service shall deny any motor value outside of the bounds defined in the roboclaw library.
- [ ] This service shall allow input only from select services
- [ ] If connection to sEventBus fails, this service shall retry in 10 seconds. If retry fails, this service shall exit. 
- [ ] sEventBus communications shall run on a secondary thread. 
- [ ] This service will subscribe to the DRIVE_COMMAND event
- [ ] If EMERGENCY_STOP is received on sEventBus, this service shall set motor power to 0 using the roboclaw library. 
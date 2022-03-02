#pdmv3_cw
import serial
from enum import Enum
from aerodiode import Aerodiode
import csv
import struct

class Pdmv3_cw(Aerodiode):
    """
        Class to command one pdmv3_cw Aerodiode's product
    """
    #Command
    COMMAND_READ_CW_OR_PULSE        = 0x20

    #Instruction
    INSTRUCT_CURRENT_PERCENT        = 0x10
    INSTRUCT_TEMPERATURE            = 0x11
    INSTRUCT_CURRENT_ALARM          = 0x13
    INSTRUCT_CURRENT_SOURCE         = 0x15
    INSTRUCT_READ_INTERLOCK_STATUS  = 0x1A #OK
    INSTRUCT_LASER_ACTIVATION       = 0x1B

    def __init__(self, port):
      """
        Open serial device.
        :param dev: Serial device path. For instance '/dev/ttyUSB0' on linux, 'COM0' on Windows.
      """
      #Connection
      Aerodiode.__init__(self,port)

      #Adress (int type)
      _add = self.get_addr()



    

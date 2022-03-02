#pdmv3
import serial
from enum import Enum
from aerodiode import Aerodiode
import csv
import struct
   
class Pdmv3(Aerodiode):
    """
        Class to command one pdmv3 Aerodiode's product
    """
    #Command
    COMMAND_READ_CW_OR_PULSE        = 0x20

    #Instruction
    INSTRUCT_SYNC_SOURCE            = 0x0A
    INSTRUCT_PULSE_SOURCE           = 0x0B
    INSTRUCT_FREQUENCY              = 0x0C
    INSTRUCT_PULSE_WIDTH            = 0x0D
    INSTRUCT_DELAY                  = 0x0E
    INSTRUCT_OFFSET_CURRENT         = 0x0F
    INSTRUCT_CURRENT_PERCENT        = 0x10
    INSTRUCT_TEMPERATURE            = 0x11
    INSTRUCT_CURRENT_ALARM          = 0x13
    INSTRUCT_CURRENT_SOURCE         = 0x15
    INSTRUCT_READ_INTERLOCK_STATUS  = 0x1A
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

    def read_cw_or_pulse(self):
        """
           Read if the ccs configuration is pulsed or continue
           return 0 if pulsed
                  1 if continue
        """
        self.send_query(self._add, self.COMMAND_READ_CW_OR_PULSE, data = [])


    
    
    

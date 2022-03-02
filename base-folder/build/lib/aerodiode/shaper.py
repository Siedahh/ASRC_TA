#Shaper
# -*- coding: utf-8 -*-
import serial
from enum import Enum
from aerodiode import Aerodiode
import csv
import struct

class Shaper(Aerodiode):
   """
    Class to command one Shaper Aerodiode's product
   """

   #SHAPE----------------------------------------------
   SHAPE1 = 0x00
   SHAPE2 = 0x01
   SHAPE3 = 0x02
   SHAPE4 = 0x03
   #Command--------------------------------------------
   COMMAND_SEND_SHAPE_DATA                      = 0x16
   COMMAND_SAVE_SHAPE_DATA                      = 0x17
   COMMAND_SET_INTER_SHAPE_TIME                 = 0x25
   COMMAND_PLAY_SHAPE                           = 0x26
   #Instruction---------------------------------------
   INSTRUCT_LASER_ACTIVATION                    = 0x0A #ok
   INSTRUCT_INTERSHAPE_DELAY_MODE               = 0x0D #ok -> conv 
   INSTRUCT_LASER_TEMPERATURE                   = 0x0E #ok -> conv
   INSTRUCT_MIN_TIME_BETWEEN_TWO_SHAPE          = 0x0F #ok -> conv
   INSTRUCT_SHAPE_DEFAULT_OUTPUT_VALUE          = 0x11 #ok -> conv
   INSTRUCT_OFFSET_CURRENT                      = 0x14 #ok -> conv
   INSTRUCT_CURRENT                             = 0x15 #ok -> conv
   INSTRUCT_MAX_VOLTAGE_MODULATION              = 0x16 #ok -> conv
   INSTRUCT_PEAK_CURRENT_MODULATION             = 0x19 #ok -> conv
   INSTRUCT_TRIGGER_SYNCHRO_SOURCE_A            = 0x1E #ok -> conv
   INSTRUCT_TRIGGER_SYNCHRO_SOURCE_B            = 0x1F #ok -> conv
   INSTRUCT_TRIGGER_SEQUENCE_SYNC_A             = 0x20 #ok -> conv
   INSTRUCT_TRIGGER_SEQUENCE_SYNC_B             = 0x21 #ok -> conv
   INSTRUCT_DELAY_SYNC_A_SYNC_B                 = 0x22 #ok -> conv
   INSTRUCT_INTERNAL_SYNC_FREQUENCY_A           = 0x23 #ok -> conv
   #Instruction : Shape 1-----------------------------
   INSTRUCT_SHAPE1_SYNC_FB_DELAY                = 0x24 #ok
   INSTRUCT_SHAPE1_SYNC_FB_PULSE_WIDTH          = 0x25 #ok
   INSTRUCT_SHAPE1_TRIG_OUT1_DELAY              = 0x26 #ok
   INSTRUCT_SHAPE1_TRIG_OUT1_PULSE_WIDTH        = 0x27 #ok
   INSTRUCT_SHAPE1_TRIG_OUT2_DELAY              = 0x28 #ok
   INSTRUCT_SHAPE1_TRIG_OUT2_PULSE_WIDTH        = 0x29 #ok
   INSTRUCT_SHAPE1_TRIG_OUT3_DELAY              = 0x2A #ok
   INSTRUCT_SHAPE1_TRIG_OUT3_PULSE_WIDTH        = 0x2B #ok
   INSTRUCT_SHAPE1_PDM_PULSE_DELAY              = 0x2C #ok
   INSTRUCT_SHAPE1_PDM_PULSE_PULSE_WIDTH        = 0x2D #ok
   INSTRUCT_SHAPE1_DELAY                        = 0x2E #ok -> conv
   
   INSTRUCT_SHAPE1_STEP_COUT                    = 0x5A #ok -> Shape1 nombre de palier
   INSTRUCT_SHAPE1_STEP_SIZE                    = 0x5B #ok -> Shape1 nombre de point par palier
   INSTRUCT_SHAPE1_TRIGGER_STEP_SIZE            = 0x5C #ok -> Shape1 pas d'incrémentation du trigger
   INSTRUCT_SHAPE1_INTERNSHAPE_OFFSET_TIME      = 0x5D #ok
   INSTRUCT_SHAPE1_MAX_INTERNSHAPE_TIME_VALUE   = 0x5E #ok
   #Instruction : Shape 2-----------------------------
   INSTRUCT_SHAPE2_SYNC_FB_DELAY                = 0x2F #ok
   INSTRUCT_SHAPE2_SYNC_FB_PULSE_WIDTH          = 0x30 #ok
   INSTRUCT_SHAPE2_TRIG_OUT1_DELAY              = 0x31 #ok
   INSTRUCT_SHAPE2_TRIG_OUT1_PULSE_WIDTH        = 0x32 #ok
   INSTRUCT_SHAPE2_TRIG_OUT2_DELAY              = 0x33 #ok
   INSTRUCT_SHAPE2_TRIG_OUT2_PULSE_WIDTH        = 0x34 #ok
   INSTRUCT_SHAPE2_TRIG_OUT3_DELAY              = 0x35 #ok
   INSTRUCT_SHAPE2_TRIG_OUT3_PULSE_WIDTH        = 0x36 #ok
   INSTRUCT_SHAPE2_PDM_PULSE_DELAY              = 0x37 #ok
   INSTRUCT_SHAPE2_PDM_PULSE_PULSE_WIDTH        = 0x38 #ok
   INSTRUCT_SHAPE2_DELAY                        = 0x39 #ok -> conv
   
   INSTRUCT_SHAPE2_STEP_COUT                    = 0x5F #ok -> Shape1 nombre de palier
   INSTRUCT_SHAPE2_STEP_SIZE                    = 0x60 #ok -> Shape1 nombre de point par palier
   INSTRUCT_SHAPE2_TRIGGER_STEP_SIZE            = 0x61 #ok -> Shape1 pas d'incrémentation du trigger
   INSTRUCT_SHAPE2_INTERNSHAPE_OFFSET_TIME      = 0x62 #ok
   INSTRUCT_SHAPE2_MAX_INTERNSHAPE_TIME_VALUE   = 0x63 #ok
   #Instruction : Shape 3-----------------------------
   INSTRUCT_SHAPE3_SYNC_FB_DELAY                = 0x3A #ok
   INSTRUCT_SHAPE3_SYNC_FB_PULSE_WIDTH          = 0x3B #ok
   INSTRUCT_SHAPE3_TRIG_OUT1_DELAY              = 0x3C #ok
   INSTRUCT_SHAPE3_TRIG_OUT1_PULSE_WIDTH        = 0x3D #ok
   INSTRUCT_SHAPE3_TRIG_OUT2_DELAY              = 0x3E #ok
   INSTRUCT_SHAPE3_TRIG_OUT2_PULSE_WIDTH        = 0x3F #ok
   INSTRUCT_SHAPE3_TRIG_OUT3_DELAY              = 0x40 #ok
   INSTRUCT_SHAPE3_TRIG_OUT3_PULSE_WIDTH        = 0x41 #ok
   INSTRUCT_SHAPE3_PDM_PULSE_DELAY              = 0x42 #ok
   INSTRUCT_SHAPE3_PDM_PULSE_PULSE_WIDTH        = 0x43 #ok
   INSTRUCT_SHAPE3_DELAY                        = 0x44 #ok -> conv
   
   INSTRUCT_SHAPE3_STEP_COUT                    = 0x64 #ok -> Shape1 nombre de palier
   INSTRUCT_SHAPE3_STEP_SIZE                    = 0x65 #ok -> Shape1 nombre de point par palier
   INSTRUCT_SHAPE3_TRIGGER_STEP_SIZE            = 0x66 #ok -> Shape1 pas d'incrémentation du trigger
   INSTRUCT_SHAPE3_INTERNSHAPE_OFFSET_TIME      = 0x67 #ok
   INSTRUCT_SHAPE3_MAX_INTERNSHAPE_TIME_VALUE   = 0x68 #okINSTRUCT_SHAPE1_INTERNSHAPE_OFFSET_TIME      = 0x5D #ok
   INSTRUCT_SHAPE1_MAX_INTERNSHAPE_TIME_VALUE   = 0x5E #ok
   #Instruction : Shape 4-----------------------------
   INSTRUCT_SHAPE4_SYNC_FB_DELAY                = 0x45 #ok
   INSTRUCT_SHAPE4_SYNC_FB_PULSE_WIDTH          = 0x46 #ok
   INSTRUCT_SHAPE4_TRIG_OUT1_DELAY              = 0x47 #ok
   INSTRUCT_SHAPE4_TRIG_OUT1_PULSE_WIDTH        = 0x48 #ok
   INSTRUCT_SHAPE4_TRIG_OUT2_DELAY              = 0x49 #ok
   INSTRUCT_SHAPE4_TRIG_OUT2_PULSE_WIDTH        = 0x4A #ok
   INSTRUCT_SHAPE4_TRIG_OUT3_DELAY              = 0x4B #ok
   INSTRUCT_SHAPE4_TRIG_OUT3_PULSE_WIDTH        = 0x4C #ok
   INSTRUCT_SHAPE4_PDM_PULSE_DELAY              = 0x4D #ok
   INSTRUCT_SHAPE4_PDM_PULSE_PULSE_WIDTH        = 0x4E #ok
   INSTRUCT_SHAPE4_DELAY                        = 0x4F #ok -> conv
   
   INSTRUCT_SHAPE4_STEP_COUT                    = 0x69 #ok -> Shape1 nombre de palier
   INSTRUCT_SHAPE4_STEP_SIZE                    = 0x6A #ok -> Shape1 nombre de point par palier
   INSTRUCT_SHAPE4_TRIGGER_STEP_SIZE            = 0x6B #ok -> Shape1 pas d'incrémentation du trigger
   INSTRUCT_SHAPE4_INTERNSHAPE_OFFSET_TIME      = 0x6C #ok
   INSTRUCT_SHAPE4_MAX_INTERNSHAPE_TIME_VALUE   = 0x6D #ok

   #INSTRUCTION GAINSWITCH------------------------------
   INSTRUCT_GAINSWITCH_CORRECTION_MODE           = 0x82
   INSTRUCT_GAINSWITCH_CORRECTION_RAMP_AMPLITUDE = 0x83
   INSTRUCT_GAINSWITCH_CORRECTION_RAMP_DURATION  = 0x84

   #INSTRUCTION ALARMS----------------------------------
   INSTRUCT_ALARMS_ENABLE                        = 0xC8
   INSTRUCT_ALARMS_BEHAVIORS                     = 0xC9
   INSTRUCT_ALARMS_BEHAVIORS2                    = 0xCD

   #MEASURE ID------------------------------------------
   MAIN_VOLTAGE                                 = 0x00
   LASER_DIODE_TEMPERATURE                      = 0x01
   ALARM_STATE                                  = 0x02
   AVERAGE_OPTICAL_POWER                        = 0x04
   
   #XNNVALUE-------------------------------------------
   VALUE_LASER_OFF                              = 0x00
   VALUE_LASER_ON                               = 0x01

   SYNC_EXT0                                    = 0x00
   SYNC_EXT1                                    = 0x01
   SYNC_EXTKK                                   = 0x02
   SYNC_INTERNAL                                = 0x03
   SYNC_NONE                                    = 0x04

   ALARM_NOT_ENABLE                             = 0x00
   ALARM_ENABLE                                 = 0x01

   GAINSWITCH_CORRECTION_MODE_ON                = 0x01
   GAINSWITCH_CORRECTION_MODE_OFF               = 0x00

   INTERSHAPE_DELAY_MODE_ANALOG                 = 0x00
   INTERSHAPE_DELAY_MODE_TRIG_SOFT              = 0x01
   

   #Methods
   def __init__(self, port):
      """
        Open serial device.
        :param dev: Serial device path. For instance '/dev/ttyUSB0' on linux, 'COM0' on Windows.
      """
      #Connection
      Aerodiode.__init__(self,port)

      #Adress (int type)
      _add = self.get_addr()

      #Alarm (dictionnary type)    
      self.alarm_enable = dict(laser_temperature = 0, MPDM_MOS_temperature = 0, reserved1 = 0, reserved2 = 0,
                               diode_average_power = 1,diode_average_current = 1, main_voltage = 1, aux_off = 1)
      
      self.alarm_behavior = dict(laser_temperature = 0, MPDM_MOS_temperature = 0, reserved1 = 0, reserved2 = 0,
                                 diode_average_power = 0,diode_average_current = 0, main_voltage = 0, aux_off = 0)

      self.alarm_behavior2 = dict(laser_temperature = 0, MPDM_MOS_temperature = 0, reserved1 = 0, reserved2 = 0,
                                 diode_average_power = 0,diode_average_current = 0, main_voltage = 0, aux_off = 0)

      self.alarm_state = dict(laser_temperature = 0, MPDM_MOS_temperature = 0, reserved1 = 0, reserved2 = 0,
                                 diode_average_power = 0,diode_average_current = 0, main_voltage = 0, aux_off = 0)
      
      self.read_alarm_enable(); self.read_alarm_behavior(); self.read_alarm_behavior2() #set the alarm dicionnary with the MCU's value

      #Sequence (dictionnary type)
      self.sequence_a = dict(LAST_VALID_ID = 0, ID8 = 0, ID7 = 0, ID6 = 0, ID5 = 0, ID4 = 0, ID3 = 0, ID2 = 0, ID1 = 0)
      self.sequence_b = dict(LAST_VALID_ID = 0, ID8 = 0, ID7 = 0, ID6 = 0, ID5 = 0, ID4 = 0, ID3 = 0, ID2 = 0, ID1 = 0)
     

   def read_csv(self, csv_file):
      """
         Convert a csv file in list..
         :param csv_file: file path of your csv file
         :return: a table from your csv file
      """
      table_csv = []                      
      with open(csv_file) as file: #open csv as file variable
         read = csv.reader(file) #read file variable
         print('\n') #??? but it works
         for line in read: #read line by line
              #convert a list of string to int
              int_line = "".join(line) #step 1 convert the list in a string
              int_line = int(int_line) #step 2 convert in int
              table_csv.append(int_line) #add to the end of the table
      return table_csv
   
   def send_csv(self, shape_id, table_csv):
      """
         Send a csv_table to the Shaper.
         :param shape id: bytes from 0x00 to 0x03 (4 shapes available)
         :param shape table_csv: table of integer
         :no return 
      """

      if len(table_csv)>4000:
         raise ValueError('data must be inferior to 4000.')

      csv_output = [table_csv[i:i +60] for i in range(0, len(table_csv), 60)] #tableau 2D contenant des tableaux 1D qui sont les découpes de table_csv par pacquet de 60.

      for i in range(0, len(csv_output)):

         start = [0x00, 0x00] #Always start at the offset 0 which is declared on two bytes
         if (i>0):
            length = (0x3C)*i #=(60)*i because the card receive the data 60 by 60 values
            if (length < 0xFF):#verify if the new offset could be represented on one or two bytes
               start[0] = length
            else:
               start[1] = length//0xFF
               start[0] = length - (length//0xFF)*0xFF

         csv_send = []
         for j in range(0,len(csv_output[i])):
            value1 = csv_output[i][j]//(0x100) 
            value0 = csv_output[i][j] - (csv_output[i][j]//0x100)*0x100
            #value 1 and 0 enable to represent each data on two bytes
            csv_send.append(value1)
            csv_send.append(value0)
             
         data = [shape_id, start[1], start[0]] + csv_send #concatenate the data
         self.send_query(self._add, self.COMMAND_SEND_SHAPE_DATA, data) #send the csv_send

   def play_shape(self, shape_id):
      return self.send_query(self._add, self.COMMAND_PLAY_SHAPE, bytearray([shape_id]))

   def save_shape_data(self):
      return self.send_query(self._add, self.COMMAND_SAVE_SHAPE_DATA)

   def set_inter_shape_time(self, shapeid, time): 
      data = [shapeid]
      data_value = struct.pack('>f',time)

      for i in range(0, len(data_value)):
            data.append(data_value[i])

      return self.send_query(self._add, self.COMMAND_SET_INTER_SHAPE_TIME, data)
      
   def read_alarm(self, alarm_id, alarm_dict, typ = 0):
      '''
         Read alarm
         :param alarm_id:
         :param alarm_dict: data dictionnary which contains the alarm data
         :param typ: Read Intruction(0)/Measure(1)
      '''
      
      if typ == 0: #read instruction
         alarm_status_bit = "{0:08b}".format(self.read_integer_instruction(alarm_id))[::-1] #str type on 8 bit
      else: #read measure
         alarm_status_bit = "{0:08b}".format(self.measure(alarm_id))[::-1] #str type

      j = 0;
      for i in alarm_dict:
         alarm_dict[i] = alarm_status_bit[j]
         j += 1

      return alarm_dict;

   def set_alarm(self, alarm_id, alarm_dict):
      '''
         Set alarm instructions only
         :param alarm_id:
         :param alarm_dict: data dictionnary which contains the alarm data
      '''
      data = [0x00, alarm_id]
      value_int = 0
      cmp = 0
      for i in alarm_dict:
         value_int += int(alarm_dict[i])*2**cmp
         cmp += 1
      data.append(value_int)
      return self.send_query(self._add, self.COMMAND_WRITE, data)

   def read_alarm_enable(self):
      '''
         set alarm enable status from the MCU to the software
         :return alarm_enable dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.read_alarm(self.INSTRUCT_ALARMS_ENABLE, self.alarm_enable)
      
   def set_alarm_enable(self):
      '''
         set alarm enable status from the software to the MCU
         :return alarm_enable dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.set_alarm(self.INSTRUCT_ALARMS_ENABLE, self.alarm_enable)

   def read_alarm_behavior(self):
      '''
         set alarm behavior status from the MCU to the software
         :return alarm_behavior dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.read_alarm(self.INSTRUCT_ALARMS_BEHAVIORS, self.alarm_behavior)
      
   def set_alarm_behavior(self):
      '''
         set alarm behavior status from the software to the MCU
         :return alarm_behavior dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.set_alarm(self.INSTRUCT_ALARMS_BEHAVIORS, self.alarm_behavior)
      

   def read_alarm_behavior2(self):
      '''
         set alarm behavior2 status from the MCU to the software
         :return alarm_behavior2 dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.read_alarm(self.INSTRUCT_ALARMS_BEHAVIORS2, self.alarm_behavior2)

   def read_alarm_state(self):
      '''
         set alarm status from the MCU to the software
         :return alarm_status dictionnary such as 1 = ON and 0 = OFF
      '''
      return self.read_alarm(self.ALARM_STATE, self.alarm_state, 1)

   def read_sequence_shape(self, sequence_id, sequence_dict):
      """
         Set the value from the MCU's sequence to the sequence_dict such as sequence_a or sequence_b
         :param sequence_id: to indentify the sequence to change such as INSTRUCT_TRIGGER_SEQUENCE_SYNC_A or INSTRUCT_TRIGGER_SEQUENCE_SYNC_B
         :param sequence_dict: sequence dictionnary sequence_a or sequence_b
         :no return
      """
      sequence_in_bit = "{0:028b}".format(self.read_integer_instruction(self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_A)) #conversion of an integer to a string of bits of length 28
      sequence_dict['LAST_VALID_ID'] = int(sequence_in_bit[0:4],2)                                  #read the length on 4 bit, conversion bit string to int
      j = 4                                                                                         #start to read at four the sequence because the length is already set
      for i in sequence_dict:
         if i != 'LAST_VALID_ID' :
            sequence_dict[i] = int(sequence_in_bit[j:j+3],2)                                        #each id are written on 3 bits, conversion bit string to int
            j += 3                                                                                  

      return sequence_dict

   def set_sequence_shape(self, sequence_id, sequence_dict):
      """
         Set the value modified in the sequence dictionnary such as sequence_a or sequence_b to the MCU
         :param sequence_id: to indentify the sequence to change such as INSTRUCT_TRIGGER_SEQUENCE_SYNC_A or INSTRUCT_TRIGGER_SEQUENCE_SYNC_B
         :param sequence_dict: sequence dictionnary sequence_a or sequence_b
         :no return
         conversion sequence dictionary -> bit string -> int -> bytes (U32 format)
      """

      sequence_in_bit_table = []                                              #table collecting the contents of the sequence dictionnary
      for i in sequence_dict:
         if i == 'LAST_VALID_ID' :
            sequence_in_bit_table.append("{0:04b}".format(sequence_dict[i]))  #length is written on 4 bits
         else:
            sequence_in_bit_table.append("{0:03b}".format(sequence_dict[i]))  #id 1 to 8 are written on 3 bits
      sequence_in_bit_str = "".join(sequence_in_bit_table)                    #conversion in string
      sequence_in_int = int(sequence_in_bit_str, 2)                           #conversion in int       
      sequence_in_bytes = sequence_in_int.to_bytes(4, 'big')                  #conversion in bytes
      value3 = sequence_in_bytes[3]                                           #value3 of the data send
      value2 = sequence_in_bytes[2]
      value1 = sequence_in_bytes[1]
      value0 = sequence_in_bytes[0]

      data = [0x00, self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_A]
      data += [value0, value1, value2, value3]                                #concatenate the instructions to send

      return self.send_query(self._add, self.COMMAND_WRITE, data)

   def read_sequence_a(self):
      return self.read_sequence_shape(self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_A, self.sequence_a)

   def set_sequence_a(self):
      return self.set_sequence_shape(self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_B, self.sequence_a)

   def read_sequence_b(self):
      return self.read_sequence_shape(self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_A, self.sequence_a)

   def set_sequence_b(self):
      return self.set_sequence_shape(self.INSTRUCT_TRIGGER_SEQUENCE_SYNC_B, self.sequence_a)

   def measure_main_voltage(self):
      return self.measure(self.MAIN_VOLTAGE, typ = 1)

   def measure_laser_diode_temperature(self):
      return self.measure(self.LASER_DIODE_TEMPERATURE, typ = 1)

   def measure_alarm_state(self):
      return self.measure(self.ALARM_STATE, typ = 0)

   def measure_average_optical_power(self):
      return self.measure(self.AVERAGE_OPTICAL_POWER, typ = 1)
  

         
   
           
     







   
      
         
      
         
         


         




      
      
      


   

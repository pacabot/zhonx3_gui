'''
Created on 6 mars 2016

@author: Lord
'''
import array

CMD_STX = 0x02
CMD_ETX = 0x03

class ZhonxCommand:
    '''
    Base class for Zhonx commands
    '''

    def __init__(self, serialInstance, instruction):
        '''
        Constructor
        '''
        self.tty = serialInstance
        self.instruction = instruction
        
    @staticmethod    
    def __buildCmd__(self, data):
        '''
        Command format:
        STX + LEN_MSB + LEN_LSB + INSTRUCTION + DATA + ETX
        '''
        # Compute total command length
        self.length = 1 + 2 + 1 + len(data) + 1
        
        # Declare a binary buffer to store the command
        self.command = array.array('b')
        
        # Start of transmission character
        self.command.append(CMD_STX)
        # MSB part of length
        self.command.append((self.length >> 8) & 0xFF)
        # LSB part of length
        self.command.append(self.length & 0xFF)
        # Instruction
        self.command.append(self.instruction)
        # Payload data
        self.command.append(data)
        # End of transmission character
        self.command.append(CMD_ETX)
    
    
    def send(self, data):
        
        # Build command
        self.__buildCmd__(data)
        # Send command
        self.tty.write(self.command)
        
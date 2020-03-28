import serial


class Serial:
    """Class for exchanging information between Raspberry and Arduino"""

    def __init__(self, port='/dev/ttyACM0'):
        """Initialize serial variables
        :param port: serial port number of Arduino"""
        self.ser = serial.Serial(port, 9600)

    def send(self, message):
        """Function for sending data to Arduino
        :param message: string to send"""
        self.ser.write(message.encode("utf-8"))

    def send_speeds(self, speeds, angle):
        """User function for sending speeds and angles to Arduino
        :param speeds: list of speed for each motor
        :param angle: robot angle in degrees"""
        speeds = [round(s + 255) for s in speeds]
        message = speeds + [angle]
        message = [str(m).zfill(3) for m in message]
        message = " ".join(message)

        self.send(message)

    def read(self):
        """Function for reading data from Arduino
        :return: data string from Arduino"""
        if self.ser.in_waiting > 0:
            line = self.ser.readline()
            line = line.decode('utf-8')
            return line

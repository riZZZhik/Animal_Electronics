import serial


class Serial:
    """Class for exchanging information between RaspBerry and Arduino"""

    def __init__(self, port='/dev/ttyUSB0'):
        """Initialize serial variables"""
        self.ser = serial.Serial(port, 9600)

    def send(self, message):
        """Function for sending data to Arduino"""
        self.ser.write(b"{message}")

    def read(self):
        """Function for reading data from Arduino
        :return: data string from Arduino"""
        if self.ser.in_waiting > 0:
            line = self.ser.readline()
            return line


if __name__ == "__main__":
    from time import sleep
    serial = Serial()

    while True:
        serial.send("TEST TEST TEST")
        sleep(2)

        print(serial.read())
        sleep(1)

import serial


class Serial:
    """Class for exchanging information between RaspBerry and Arduino"""

    def __init__(self, port='/dev/ttyACM0'):
        """Initialize serial variables"""
        self.ser = serial.Serial(port, 9600)

    def send(self, message):
        """Function for sending data to Arduino"""
        self.ser.write(message.encode("utf-8"))

    def read(self):
        """Function for reading data from Arduino
        :return: data string from Arduino"""
        if self.ser.in_waiting > 0:
            line = self.ser.readline()
            line = line.decode('utf-8')
            return line


if __name__ == "__main__":
    from time import sleep
    serial = Serial()

    while True:
        serial.send("255 100 050 010 000")
        sleep(2)

        print(serial.read())
        sleep(1)

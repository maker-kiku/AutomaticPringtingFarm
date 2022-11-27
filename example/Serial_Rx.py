import serial

serialport = serial.Serial("/dev/tty.usbmodem1201", 115200, timeout=3)
# serialport = serial.Serial("/dev/tty.usbserial-2", 115200, timeout=3)
# serialport = serial.Serial("/dev/cu.usbserial-A907NDP7", 115200, timeout=3)
# serialport = serial.Serial("/dev/cu.usbmodem11301", 115200, timeout=3)

while True:
    print("RX data: " + serialport.readline().decode("utf-8"))
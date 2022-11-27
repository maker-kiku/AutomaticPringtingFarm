import serial

# serialport = serial.Serial("/dev/cu.usbserial-11410", 115200, timeout=3)
# serialport = serial.Serial("/dev/cu.usbserial-A907NDP7", 115200, timeout=3)
serialport = serial.Serial("/dev/cu.usbmodem11301", 115200, timeout=3)

for index in range(0, 14):
    print("RX data: " + serialport.readline().decode("utf-8")) 

while True:
    # TX (Transmit)로 송신할 데이터 입력 받기
    towrite = input("TX data: ") 

    # 입력 받은 데이터 + '\n' (개행) 데이터 송신 (아스키 인코딩)
    serialport.write((towrite + '\n').encode())
    print("RX data: " + serialport.readline().decode("utf-8")) 

        
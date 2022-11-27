import serial

# serialport = serial.Serial("/dev/tty.usbmodem12101", 115200, timeout=3)
serialport = serial.Serial("/dev/cu.usbmodem12201", 115200, timeout=3)

while True:
    # TX (Transmit)로 송신할 데이터 입력 받기
    rxData = serialport.readline().decode("utf-8")

    if rxData:
        print("RX data: " + rxData)
        continue

    else:   
        towrite = input("TX data: ")

        # 입력 받은 데이터 + '\n' (개행) 데이터 송신 (아스키 인코딩)
        serialport.write((towrite + '\n').encode())
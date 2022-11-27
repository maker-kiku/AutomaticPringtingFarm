import serial

serialport = serial.Serial("/dev/tty.usbmodem1201", 115200, timeout=3)

while True:
    # TX (Transmit)로 송신할 데이터 입력 받기
    print("RX data: " + serialport.readline().decode("utf-8"))
    
    towrite = input("TX data: ")
    # 입력 받은 데이터 + '\n' (개행) 데이터 송신 (아스키 인코딩)
    serialport.write((towrite + '\n').encode())
    print("RX data: " + serialport.readline().decode("utf-8"))



# ⸮Start
# 22:24:49.888 -> rcvd : 3
# 22:24:49.888 -> Recv : sta
# 22:24:49.922 -> rcvd : 3
# 22:24:49.922 -> Recv : rt^
# 22:24:51.702 -> rcvd : 14
# 22:24:51.702 -> Recv : echo: 3.10.0-4
# 22:24:51.702 -> rcvd : 64
# 22:24:51.702 -> Recv : 4nerBufferBytes: 1760^echo:Hardcoded Default Settings Loaded^adc
# 22:24:51.702 -> rcvd : 52
# 22:24:51.702 -> Recv : _init^config)^Compiled: May  6 2021^echo: Free Memor
# 22:24:51.738 -> rcvd : 64
# 22:24:51.738 -> Recv : y: 2054  PlannerBufferBytes: 1760^echo:Hardcoded Default Setting
# 22:24:51.738 -> rcvd : 18
# 22:24:51.738 -> Recv : s Loaded^adc_init^
# 22:24:52.061 -> rcvd : 19
# 22:24:52.061 -> Recv : Extruder fan type: 
# 22:24:53.070 -> rcvd : 18
# 22:24:53.070 -> Recv : NOCTUA^CrashDetect
# 22:24:53.122 -> rcvd : 10
# 22:24:53.122 -> Recv :  ENABLED!^
# 22:24:54.189 -> rcvd : 33
# 22:24:54.189 -> Recv : FSensor ENABLED (sensor board rev
# 22:24:54.189 -> rcvd : 21
# 22:24:54.189 -> Recv : ision: 0.4 or newer)^
# 22:24:54.378 -> rcvd : 13
# 22:24:54.378 -> Recv : Sending 0xFF^
# 22:24:54.378 -> rcvd : 16
# 22:24:54.378 -> Recv : echo:SD card ok^
# 22:24:54.436 -> rcvd : 19
# 22:24:54.436 -> Recv : LCD status changed^
# 22:25:19.807 -> rcvd : 29
# 22:25:19.807 -> Recv : MMU not responding - DISABLED
# 22:25:19.807 -> rcvd : 1
# 22:25:19.807 -> Recv : ^

# RX data: start
# RX data: echo: 3.10.0-4481
# RX data: echo: Last Updated: May  6 2021 13:52:17 | Author: (none, default config)
# RX data: Compiled: May  6 2021
# RX data: echo: Free Memory: 2054  PlannerBufferBytes: 1760
# RX data: echo:Hardcoded Default Settings Loaded
# RX data: adc_init
# RX data: Extruder fan type: NOCTUA
# RX data: CrashDetect ENABLED!
# RX data: FSensor ENABLED (sensor board revision: 0.4 or newer)
# RX data: Sending 0xFF
# RX data: echo:SD card ok
# RX data: LCD status changed
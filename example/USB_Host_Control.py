import re
import serial
 
prusa1 = serial.Serial("/dev/cu.usbmodem13101", 115200, timeout=3) # Open Prusa serial port
prusa2 = serial.Serial("/dev/cu.usbmodem13201", 115200, timeout=3) # Open Prusa serial port
prusa3 = serial.Serial("/dev/cu.usbmodem13301", 115200, timeout=3) # Open Prusa serial port
prusa4 = serial.Serial("/dev/cu.usbmodem13401", 115200, timeout=3) # Open Prusa serial port

# ================================================= 메인 코드 시작 =================================================

for index in range(0, 14): # Get serial signal
    print("RX data: " + prusa1.readline().decode("utf-8"))

prusa1.write(("M104 S180" + '\n').encode("ascii")) # 커멘드 전송
prusa1.write(("M140 S60" + '\n').encode("ascii")) # 커멘드 전송


prusa2.write(("M104 S180" + '\n').encode("ascii")) # 커멘드 전송
prusa2.write(("M140 S60" + '\n').encode("ascii")) # 커멘드 전송


prusa3.write(("M104 S180" + '\n').encode("ascii")) # 커멘드 전송
prusa3.write(("M140 S60" + '\n').encode("ascii")) # 커멘드 전송


prusa4.write(("M104 S180" + '\n').encode("ascii")) # 커멘드 전송
prusa4.write(("M140 S60" + '\n').encode("ascii")) # 커멘드 전송
# write_command_until_ok('M105')
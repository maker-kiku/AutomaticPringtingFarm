import re
import serial
 
prusa = serial.Serial("/dev/cu.usbmodem114301", 115200, timeout=3) # Open Prusa serial port
gcode = open('/Users/dev_kiku/Desktop/Test_Ship.gcode','r') # Open g-code file

def write_command_until_ok(_command):
    print("Tx : " + _command)
    prusa.write((_command + '\n').encode("ascii")) # 커멘드 전송
    
    while True:
        rx = prusa.readline().decode("utf-8") # 응답
        rx = re.sub(r'\n', '', rx) # 개행문자 제거
        print("Rx : " + rx)

        if "checksum mismatch" in rx: # 에러 발생하면 다시 커멘드 전송
            write_command_until_ok(_command)
        elif "ok" in rx: # 응답이 'ok'이면 
            break
        elif "Done saving file" in rx:
            break

# ================================================= 메인 코드 시작 =================================================

for index in range(0, 14): # Get serial signal
    print("RX data: " + prusa.readline().decode("utf-8"))

write_command_until_ok('M23 test.gco')
write_command_until_ok('M24')

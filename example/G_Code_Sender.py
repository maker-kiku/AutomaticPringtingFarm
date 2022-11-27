import re
import serial
 
prusa = serial.Serial("/dev/cu.usbmodem1101", 115200, timeout=3) # Open Prusa serial port
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

def strip_comment(_line): # 주석 제거하는 코드
    if ";" not in _line:
        # shortcut
        return _line

    result = []
    for c in _line:
        if c == ";":
            break
        result += c

    return "".join(result)

def calc_checksum(_command, _linenumber): 
    command_to_send = b"N" + str(_linenumber).encode("ascii") + b" " + _command.encode("ascii")

    checksum = 0
    for c in bytearray(command_to_send):
        checksum ^= c

    command_to_send = command_to_send + b"*" + str(checksum).encode("ascii")
    return command_to_send

# ================================================= 메인 코드 시작 =================================================

for index in range(0, 14): # Get serial signal
    print("RX data: " + prusa.readline().decode("utf-8"))

write_command_until_ok('M20 L')
write_command_until_ok('N0 M110 N0*125')
write_command_until_ok('M28 test.gco')

linenumber = 1

for command_from_gcode in gcode: # g-code 파일 전송 
    stripped_command = strip_comment(command_from_gcode) # 주석 제거
    stripped_command = re.sub(r'\n', '', stripped_command) # 개행문자 제거
    stripped_command = stripped_command.strip(' ') # 공백 제거
    
    if stripped_command: # 공백인 command 출력 하지 않음
        command_with_checksum = calc_checksum(strip_comment(stripped_command), linenumber)
        write_command_until_ok(command_with_checksum.decode("utf-8"))
        linenumber += 1

write_command_until_ok('M29')  
write_command_until_ok('M20 L')
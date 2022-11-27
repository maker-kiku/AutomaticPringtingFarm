import re, serial, time
 
rs485 = serial.Serial("/dev/cu.usbserial-11430", 115200, timeout=3) # Open rs485 serial port
gcode = open('/Users/dev_kiku/Desktop/Test_Ship.gcode','r') # Open g-code file

def write_command_until_ok(_command):
    print("Tx : P1 " + _command)
    rs485.write(("P1 " + _command + '\n').encode("ascii")) # 커멘드 전송
    
    
    while True:
        rx = rs485.readline().decode("utf-8") # 응답 확인
        rx = re.sub(r'\n', '', rx) # 개행문자 제거
        print("Rx : " + rx)

        if "checksum mismatch" in rx: # 에러 발생하면 다시 커멘드 전송
            print("RX : " + rs485.readline().decode("utf-8"))
            print("RX : " + rs485.readline().decode("utf-8"))
            write_command_until_ok(_command)
        if "responding" in rx: # 에러 발생하면 다시 커멘드 전송
            write_command_until_ok(_command)
        elif "ok" in rx: # 응답이 'ok'이면 
            return
        elif "Done saving file" in rx:
            return
        elif "error" in rx: # 응답이 'error'이면 
            return

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

# for index in range(0, 14): # Get serial signal
#     print("RX data: " + rs485.readline().decode("utf-8"))

write_command_until_ok('M20 L') # 파일 리스트 보기 : okd
time.sleep(0.1)
write_command_until_ok('N0 M110 N0*125') # : ok
time.sleep(0.1)
write_command_until_ok('M28 test2.gco') # 파일 작성 시작 : ok
time.sleep(0.1)

linenumber = 1

for command_from_gcode in gcode: # g-code 파일 전송 
    stripped_command = strip_comment(command_from_gcode) # 주석 제거
    stripped_command = re.sub(r'\n', '', stripped_command) # 개행문자 제거
    stripped_command = stripped_command.strip(' ') # 공백 제거
    
    if stripped_command: # 공백인 command 출력 하지 않음
        command_with_checksum = calc_checksum(strip_comment(stripped_command), linenumber)
        write_command_until_ok(command_with_checksum.decode("utf-8"))
        linenumber += 1
        time.sleep(0.1)
    
    

write_command_until_ok('M29') # 파일 작성 종료 : Done saving file
time.sleep(0.1)
write_command_until_ok('M23 test.gco') # 파일 선택 : ok

write_command_until_ok('M24') # 프린트 : ok


# write_command_until_ok('P0 M105')


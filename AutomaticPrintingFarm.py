import serial
import serial.tools.list_ports

all_port = serial.tools.list_ports.comports()
serial_port = [] # prusa의 시리얼 포트 정보

for p in all_port:
    if 'Prusa' in p.description:
        serial_port.append(p.device)

prusa_port = [] # 연결되어 있는 프루사 포트 저장 배열
prusa_count = len(serial_port) # 연결되어 있는 프루사 대수

if serial_port: # 연결되어 있는 프루사 포트가 존재한다면
    print('prusa_count : ' + str(prusa_count))

    for count in range(0, prusa_count):
        print("Prusa_" + str(count) + " : " + serial_port[count])
        prusa_port.append(serial.Serial(serial_port[count], 115200, timeout=3))

        while True:
            # TX (Transmit)로 송신할 데이터 입력 받기
            rxData = prusa_port[count].readline().decode("utf-8")

            if rxData:
                print("Prusa_" + str(count) + "_Rx : " + rxData)
                continue

            break

    # for count in range(0, prusa_count):
        prusa_port[count].write(("G28 X0 Y0" + '\n').encode("ascii")) # 커멘드 전송
        # prusa_port[count].write(("M104 S180" + '\n').encode("ascii")) # 커멘드 전송
        # prusa_port[count].write(("M140 S60" + '\n').encode("ascii")) # 커멘드 전송

            # else:   
            #     towrite = input("TX data: ")

            #     # 입력 받은 데이터 + '\n' (개행) 데이터 송신 (아스키 인코딩)
            #     prusa_port[0].write((towrite + '\n').encode())
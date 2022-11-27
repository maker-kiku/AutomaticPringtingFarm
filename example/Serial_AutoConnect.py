import serial.tools.list_ports

port = serial.tools.list_ports.comports()

prusa_port = []

for p in port:
    if 'Prusa' in p.description:
        prusa_port.append(p.device)

print(prusa_port)


# serialport = serial.Serial("/dev/tty.usbmodem12101", 115200, timeout=3)


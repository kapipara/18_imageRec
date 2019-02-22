import serial

ser = serial.Serial('COM9', 38400, timeout=0.1)
ser.write('$V\r\n'.encode())
tmp = ser.readline().decode()
print(tmp)
ser.close()
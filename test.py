import serial

# Open the serial port (replace 'COM3' with the appropriate port name)
ser = serial.Serial('COM7', 9600)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            print(line)

except KeyboardInterrupt:
    print("Data printing stopped by the user.")

finally:
    # Close the serial port
    ser.close()

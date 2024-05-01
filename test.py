import serial
import matplotlib.pyplot as plt

# Open the serial port (replace 'COM7' with the appropriate port name)
ser = serial.Serial('COM7', 9600)

# Initialize empty lists to store data
x_data = []
y_data = []
z_data = []

# Initialize the plot
fig, ax = plt.subplots()
ax.set_title('Real-time Data from Serial Port')
ax.set_xlabel('Time')
ax.set_ylabel('Data')

# Function to update the plot
def update_plot():
    ax.clear()
    ax.set_title('Real-time Data from Serial Port')
    ax.set_xlabel('Time')
    ax.set_ylabel('Data')
    ax.plot(x_data, '--b')
    ax.plot(y_data, '-r')
    plt.draw()
    plt.pause(0.01)

# Continuously read and plot data
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            print(line)
            data = line.split(',')
            if len(data) == 3:  # Assuming the data has two parts (x, y)
                x = float(data[0])
                y = float(data[1])
                z = float(data[2])
                x_data.append(x)
                y_data.append(y)
                z_data.append(z)
                update_plot()

except KeyboardInterrupt:
    print("Plotting stopped by the user.")

finally:
    # Close the serial port
    ser.close()

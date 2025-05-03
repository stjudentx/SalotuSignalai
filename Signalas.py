import serial, time, csv
import matplotlib.pyplot as plt

ser = serial.Serial('COM5', 9600, timeout=1)
filename = "bio_signal_log.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Voltage"])
    values = []

    try:
        while True:
            line = ser.readline().decode().strip()
            if line:
                voltage = float(line)
                timestamp = time.time()
                writer.writerow([timestamp, voltage])
                values.append(voltage)

                # Real-time plot (every 100 points)
                if len(values) % 100 == 0:
                    plt.clf()
                    plt.plot(values[-500:])
                    plt.pause(0.01)

    except KeyboardInterrupt:
        print("Recording stopped.")
# Failas: kratky_signal_logger.py

import serial
import time
import csv
import matplotlib.pyplot as plt

# Konfigūruojame serijinį prievadą (pakeiskite COM portą jei reikia)
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

filename = "bio_signal_log.csv"

# Failo antraštė
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Laikas_s", "Signalo_voltai"])

print("Pradedamas įrašymas...")
pradzios_laikas = time.time()

try:
    while True:
        linija = ser.readline().decode('utf-8').strip()
        if linija:
            dabartinis_laikas = time.time() - pradzios_laikas
            voltai = float(linija)
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([dabartinis_laikas, voltai])
            print(f"{dabartinis_laikas:.1f}s -> {voltai:.3f} V")
except KeyboardInterrupt:
    print("\nBaigta.")
    ser.close()

# Vizualizacija
print("Atvaizduojami duomenys...")
data = []
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        data.append([float(row[0]), float(row[1])])

data = list(zip(*data))
plt.plot(data[0], data[1])
plt.xlabel("Laikas (s)")
plt.ylabel("Signalas (V)")
plt.title("Augalo bioelektrinis signalas (Kratky sistema)")
plt.grid(True)
plt.show()
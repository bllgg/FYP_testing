import csv
import matplotlib.pyplot as plt
import statistics

acc_x_data = []
acc_y_data = []
acc_z_data = []
gyro_x_data = []
gyro_y_data = []
gyro_z_data = []
mag_x_data = []
mag_y_data = []
mag_z_data = []
with open("Datasets/sp_stationary_mz_to_north_py_up.csv") as source_file:
    csv_reder = csv.reader(source_file, delimiter = ',')
    for row in csv_reder:
        # json_data = {"seq_num": int(row[0]), "dev_id": row[2], "tx_pow": -75, "RSSI": int(row[3]), "MAC": row[1],
        #              "acc_x": row[4], "acc_y": row[5], "acc_z": row[6], "gyr_x": row[7], "gyr_y": row[8],
        #              "gyr_z": row[9], "mag_x": row[10], "mag_y": row[11], "mag_z": row[12]}
        # j_d = json.dumps(json_data)
        acc_x_data.append(float(row[4]))
        acc_y_data.append(float(row[5]))
        acc_z_data.append(float(row[6]))

        gyro_x_data.append(float(row[7]))
        gyro_y_data.append(float(row[8]))
        gyro_z_data.append(float(row[9]))

        mag_x_data.append(float(row[10]))
        mag_y_data.append(float(row[11]))
        mag_z_data.append(float(row[12]))

# print(rssi_data)
print("mean:", statistics.mean(acc_x_data))
print("variance:", statistics.variance(acc_x_data))
print("standard_deviation", statistics.stdev(acc_x_data))

plt.subplot(3, 3, 1)
plt.hist(acc_x_data, 20)
plt.title("acc x")

plt.subplot(3, 3, 2)
plt.hist(acc_y_data, 20)
plt.title("acc y")

plt.subplot(3, 3, 3)
plt.hist(acc_z_data, 20)
plt.title("acc z")

plt.subplot(3, 3, 4)
plt.hist(gyro_x_data, 20)
plt.title("gyr x")

plt.subplot(3, 3, 5)
plt.hist(gyro_y_data, 20)
plt.title("gyr y")

plt.subplot(3, 3, 6)
plt.hist(gyro_z_data, 20)
plt.title("gyr z")

plt.subplot(3, 3, 7)
plt.hist(mag_x_data, 20)
plt.title("mag x")

plt.subplot(3, 3, 8)
plt.hist(mag_y_data, 20)
plt.title("mag y")

plt.subplot(3, 3, 9)
plt.hist(mag_z_data, 20)
plt.title("mag z")

plt.suptitle("Sensor data histograms")
plt.show()
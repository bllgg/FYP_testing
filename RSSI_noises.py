import csv
import matplotlib.pyplot as plt
import statistics
import os

rssi_data = []
with open("Datasets/stat_gen_data_com_1.csv") as source_file:
    csv_reder = csv.reader(source_file, delimiter = ',')
    for row in csv_reder:
        # json_data = {"seq_num": int(row[0]), "dev_id": row[2], "tx_pow": -75, "RSSI": int(row[3]), "MAC": row[1],
        #              "acc_x": row[4], "acc_y": row[5], "acc_z": row[6], "gyr_x": row[7], "gyr_y": row[8],
        #              "gyr_z": row[9], "mag_x": row[10], "mag_y": row[11], "mag_z": row[12]}
        # j_d = json.dumps(json_data)
        rssi_data.append(int(row[3]))

# print(rssi_data)
print("mean:", statistics.mean(rssi_data))
print("variance:", statistics.variance(rssi_data))
print("standard_deviation", statistics.stdev(rssi_data))
plt.hist(rssi_data)
plt.show()
os.system("rm Datasets/stat_gen_data_com_1.csv")
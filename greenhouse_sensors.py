import numpy as np
np.random.seed(7)
readings = np.random.randint(20, 41, size=(6, 3))
print("Sensor readings:")
print(readings)

mean_per_sensor = np.mean(readings, axis=0)
print("Mean per sensor:", mean_per_sensor)

std_per_sensor = np.std(readings, axis=0)

normalized = (readings - mean_per_sensor) / std_per_sensor

print("Normalized column means:", np.round(np.mean(normalized, axis=0), 10))

peak_hours = np.argmax(readings, axis=0)
print("Hour of max per sensor:", peak_hours)

mean_row = mean_per_sensor.reshape(1, 3)

new_readings = np.vstack((readings, mean_row))

print("New shape:", new_readings.shape)

np.random.seed(7)

readings_again = np.random.randint(20, 41, size=(6, 3))

print("Reproducible:", np.array_equal(readings, readings_again))
print("Overall hottest reading:", readings.max())
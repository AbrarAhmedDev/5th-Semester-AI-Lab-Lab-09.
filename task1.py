
import numpy as np

units = np.array([
    [30, 20, 10],
    [25, 30, 15],
    [40, 25, 20],
    [35, 15, 25]
])

price = np.array([100, 150, 200])

revenue = units * price

daily_revenue = np.sum(revenue, axis=1)

units_per_item = np.sum(units, axis=0)

best_day = np.argmax(daily_revenue)

coffee_last_two_days = units[-2:, 1]

print("Revenue per day:", daily_revenue)
print("Units sold per item:", units_per_item)
print("Best day index:", best_day)
print("Coffee, last two days:", coffee_last_two_days)
print("Total weekly revenue:", np.sum(daily_revenue))
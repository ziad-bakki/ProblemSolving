from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily


start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

location = Point(42.7370, -84.4839)

data = Daily(location, start, end)
data = data.fetch()

count = 0
minimum_temp = 0
for index, row in data.iterrows():
    # if row['tmin'] < 0 or row['tmax'] < 0:
    #     count += 1
    if row['tmin'] < minimum_temp:
        minimum_temp = row['tmin']
# print(f"It was below 0 degrees celsius {count} times!")
print(f'The lowest temperature in 2023 was {minimum_temp} degrees celsius!')


from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily


start = datetime(2024, 1, 1)
end = datetime(2024, 2, 1)

location = Point(42.7370, -84.4839)

data = Daily(location, start, end)
data = data.fetch()

count = 0
for index, row in data.iterrows():
    if row['tmin'] < 0 or row['tmax'] < 0:
        count += 1
print(f"It was below 0 degrees celsius {count} times!")
# print(data)
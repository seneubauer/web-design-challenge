from asyncore import write
import pandas as pd

df = pd.read_csv("city_weather_data.csv")

to_html = df.to_html(index=False, justify="left")

f = open("csv_weather_data.html", "w+")
f.write(to_html)
f.close()
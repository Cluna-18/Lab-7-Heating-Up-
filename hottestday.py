import pandas as pd
from pathlib import Path
import csv

tempsPath = Path("city_temperature.csv")
citytemps = pd.read_csv(tempsPath, sep = ",")

reg = citytemps.groupby(["Region"])
idx_max=reg['AvgTemperature'].idxmax()
max_temps = citytemps.loc[idx_max]

max_temps.to_csv("city_maxtemps.csv", index_label ="idx")

print(max_temps)




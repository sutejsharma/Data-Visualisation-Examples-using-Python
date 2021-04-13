import pandas as pd
from pandas import Grouper
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import seaborn as sns


file_path = "C:\\Users\\admin\\Desktop\\SQLite.csv"

data_file = pd.read_csv(file_path, parse_dates=True, squeeze = True)

#plt.bar(data_file["channel"],data_file["spend"])
#plt.ylabel("USD Spent")
#plt.xlabel("Channel")

ax = sns.barplot(x="channel",y="spend",data=data_file)
ax.set_title("USD Spent by Channel")
plt.show()

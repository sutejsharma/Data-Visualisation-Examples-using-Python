import pandas as pd
from pandas import Grouper
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import seaborn as sns


file_path = "C:\\Users\\admin\\Desktop\\Tapclicks Challenge\\SQLite.csv"

data_file = pd.read_csv(file_path, parse_dates=True, squeeze = True)

#data = {'Channel': data_file["channel"], 'Clicks': data_file["clicks"]}
#x = pd.DataFrame(data)
#ts = pd.Series(df['Clicks'].values, index=df['Channel'])
#data_file.boxplot(column='clicks', by='channel')

sns.boxplot(x='channel',y='clicks',data=data_file)
plt.show()
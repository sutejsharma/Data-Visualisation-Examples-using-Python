import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv

file_path = "C:\\Users\\admin\\Desktop\\SQLite.csv"

data_file = pd.read_csv(file_path, parse_dates=True, squeeze = True)

data = {'Date': data_file["date"], 'Clicks': data_file["clicks"]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

ts = pd.Series(df['Clicks'].values, index=df['Date'])
plt.ylabel('Clicks')
plt.xlabel('Date')
plt.title('Clicks By Date for the Entire Year')
ts.plot()
plt.show()

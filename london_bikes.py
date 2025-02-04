import zipfile
import pandas as pd
import zipfile36
import kagglehub
from openpyxl import Workbook

# download dataset from kaggle using kaggle API
path = kagglehub.dataset_download("hmavrodiev/london-bike-sharing-dataset")

# extract the file from the downloaded zip file
zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()

# read in the csv file as a pandas dataframe
bikes = pd.read_csv("london_merged.csv")
#bikes.info()

# count unique values in weather_code column
bikes.weather_code.value_counts()
#print(bikes.weather_code.value_counts())

# count unique values in season column
bikes.season.value_counts()
#print(bikes.season.value_counts())

# specifying the column names
new_cols_dict= {
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}
# rename column names
bikes.rename(new_cols_dict, axis=1, inplace=True)

# changing humidity values to percentage
bikes.humidity_percent = bikes.humidity_percent / 100

# creating a season dictionary
season_dic = {
    '0.0': 'spring',
    '1.0': 'summer',
    '2.0': 'autumn',
    '3.0': 'winter'
}

# creating a weather dictionary
weather_dic = {
    '1.0': 'clear',
    '2.0': 'scattered clouds',
    '3.0': 'broken clouds',
    '4.0': 'cloudy',
    '7.0': 'rain',
    '10.0': 'rain with thunderstorms',
    '26.0': 'snowfall'
}

# changing the seasons column data type to string
bikes.season = bikes.season.astype('str')
#mapping the values 0-3 to the actual written season
bikes.season = bikes.season.map(season_dic)

#changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')
#mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dic)

#print(bikes.head())

#writing dataframe to excel file
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')

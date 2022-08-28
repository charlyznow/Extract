import csv
import pandas as pd
import requests
from datetime import  datetime
import os 

url = 'https://swapi.dev/api/people/'
raw_path = 'C://Users//carlos.nieves//Documents//Python Scripts//raw_api//'
date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
response = requests.get(url)

data = pd.DataFrame(response.json()["results"])[['name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','species']]

for i in range (1,82):
    response= requests.get(url)
    temp_df = pd.DataFrame(response.json()["results"])[['name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','species']]
    data.append(temp_df,ignore_index=False)

temp_name = raw_path + 'peple_api' + '_' + date + '.csv'

for file in os.listdir(raw_path):
    if file.endswith('.csv'):
        print(os.path.join(raw_path,file))


temp_df.to_csv(  temp_name, sep='|',header=True, index=False)


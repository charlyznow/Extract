import pandas as pd
import requests
from datetime import  datetime
import os 
import glob


url = 'https://swapi.dev/api/people/'
pattern = r'C://Users//carlos.nieves//Documents//Campus//BussinesETL//PythonScripts//raw_api//*.csv'
raw_path = 'C://Users//carlos.nieves//Documents//Campus//BussinesETL//PythonScripts//raw_api//'
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
response = requests.get(url)

for item in glob.iglob(pattern , recursive=True):
    os.remove(item)
    print('Deleting Csv Files into the Directory')

data = pd.DataFrame(response.json()["results"])[['name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','species']]

for i in range (1,82):
    response= requests.get(url)
    temp_df = pd.DataFrame(response.json()["results"])[['name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','species']]
    data.append(temp_df,ignore_index=False)

temp_name = raw_path + 'people_api' + '_' + date + '.csv'

temp_df.to_csv(  temp_name, sep='|',header=True, index=False)


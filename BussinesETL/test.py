import pandas as pd
import requests
from datetime import  datetime
import os 
import glob

pattern = r'C://Users//carlos.nieves//Documents//Campus//BussinesETL//PythonScripts//raw_api//*.csv'

for item in glob.iglob(pattern , recursive=True):
    os.remove(item)
    print('Deleting File')



"""
for f in os.listdir(raw_path):
    file = raw_path + 'peple*.csv'
    if os.path.isfile(file):
        print('Deleting File:',file )
        os.remove(file)
"""
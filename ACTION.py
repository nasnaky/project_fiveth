import time

import pandas as pd
import requests

while 1:
    df = pd.read_excel('C:/Users/user/Desktop/새 폴더/복사본 PLX-DAQ-v2.11.xlsm')
    df = df.values.tolist()

    url1 = "http://10.82.18.147:8001/CW/"
    data1 = {"WATER": int(df[-1][0]/100)}
    data1 = data1
    print(data1)
    response1 = requests.post(url1, data=data1)
    url1 = "http://10.82.18.147:8001/CH/"
    data1 = {"DEGREE": int(df[-1][1]/10)}
    print(data1)
    response2 = requests.post(url1, data=data1)
    url1 = "http://10.82.18.147:8001/CT/"
    data1 = {"TEMP": int(df[-1][2]-5)}
    print(data1)
    response3 = requests.post(url1, data=data1)
    print(response1.status_code, response2.status_code, response3.status_code)
    time.sleep(80)

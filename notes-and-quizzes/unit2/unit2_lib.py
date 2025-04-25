import requests
#mport numpy as np

def get_readings(id:int, url:str="http://192.168.6.142/readings") -> list:
    req = requests.get(url)
    data = req.json()
    readings = data["readings"][0]
    temp = []
    for sample in readings:
        if sample["sensor_id"] == id:
            temp.append(sample["value"])
    return temp

def smoothing(data:list, size_window:int=12) -> list:
    x = []
    y = []
    for i in range(0, len(data), size_window):
        #print(data[i:i+size_window])
        segment_mean = sum(data[i:i+size_window])/size_window
        y.append(segment_mean)
        x.append(i)
    return x, y
#Testing Use

import requests

user = {"username": "bob", 'password':'B@bisthebestname'}
bobsensor = [18,19,20,21,22,23,24,25]


req = requests.post('http://192.168.6.142/login', json=user)
access_token = req.json()["access_token"]
print(access_token)

req = requests.get("http://192.168.6.142/sensors" , headers={"Authorization": f"Bearer {access_token}"})

req2 = requests.get("http://192.168.6.142/readings" , headers={"Authorization": f"Bearer {access_token}"})

print(req.json())

#print(req2.json())
data = req2.json()["readings"][0]


temp = []
humidity = []

temp_samples =[]
humidity_samples = []

for sample in data:
    if sample["id"] in bobsensor:
        if sample["id"] == 5:
           temp.append(sample["value"])
        if sample["id"] == 4:
           humidity.append(sample["value"])



for i in range(len(temp)):
    temp_samples.append(i)

for i in range(len(humidity)):
    humidity_samples.append(i)

print(temp)
print(humidity)

print(temp_samples)
print(humidity_samples)

import matplotlib.pyplot as plt

plt.plot(temp_samples, temp)
plt.plot(humidity_samples, humidity)
plt.show()
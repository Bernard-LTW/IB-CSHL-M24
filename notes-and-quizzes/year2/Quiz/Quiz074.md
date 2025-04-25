# Quiz 074

## Prompt
A data package is build by splitting the data into fixed sizes (load) and attach a header which contains the MAC address, IP address of the sender (sx) and destination (rx), and a sequence number to reconstruct the data.
## Code Structure

### Python File
```python
def build_data_pkg(mac_rx,ip_rx,mac_sx,ip_sx,data):
    chunks = 0
    leftover = 0
    if len(data) % 4 == 0:
        chunks = len(data) // 4
    else:
        chunks = len(data) // 4
        leftover = len(data) % 4
    output = []
    for i in range(chunks):
        target = data[i*4:(i+1)*4]
        output.append(f"{mac_rx}|{ip_rx}|{mac_sx}|{ip_sx}|{i}|{target}")
    if leftover:
        target = data[-leftover:]
        output.append(f"{mac_rx}|{ip_rx}|{mac_sx}|{ip_sx}|{chunks}|{target}")
    return output

print(build_data_pkg("80:90:00:00:00:00","192.168.3.3","80:90:00:00:00:01","192.168.4.5","Hello World"))
```

### Paper Programming
![Paper Programming](../Assets/Quiz074.jpeg)
*Fig.1* **Proof of Paper Programming**


### Evidence
![Evidence](../Assets/Quiz074Evidence.jpg)
*Fig.2* **Image showing output of program**

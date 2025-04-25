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

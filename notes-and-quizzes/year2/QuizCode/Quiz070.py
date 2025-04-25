#2023-03-07 Quiz 070
def ipv4machine_bernard():
    output = []
    for a in range(0,256):
        for b in range(0,256):
            for c in range(0,256):
                for d in range(0,256):
                    output.append(f"{a}.{b}.{c}.{d}")
    return output

# def ipv4machine():
#     return [f"{a}.{b}.{c}.{d}" for a in range(0,256) for b in range(0,256) for c in range(0,256) for d in range(0,256)]

def ipv4machine_alex():
    a = 0
    b = 0
    c = 0
    d = 0
    while a < 1:
        #print(f"{a}.{b}.{c}.{d}")
        d += 1
        if d == 256:
            d = 0
            c += 1
        if c == 256:
            c = 0
            b += 1
        if b == 256:
            b = 0
            a += 1
    return


# #test run time of algorithms
# import time
# # start = time.time()
# # ipv4machine()
# # end = time.time()
# # print(f"ipv4machine: {end-start}")
# time.sleep(3)
# start = time.time()
# ipv4machine_bernard()
# end = time.time()
# print(f"ipv4machine_bernard: {end-start}")
# temp1 = end-start
# time.sleep(3)
# start = time.time()
# ipv4machine_alex()
# end = time.time()
# print(f"ipv4machine_alex: {end-start}")
# temp2 = end-start
#
# print(f"ipv4machine_bernard is {temp2/temp1} times faster than ipv4machine_alex")


print(ipv4machine_bernard())
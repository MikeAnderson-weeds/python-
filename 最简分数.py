import math
begain_list = list(range(1,41))
finished_list = []
for t in begain_list:
    if math.gcd(t,40) == 1:
        finished_list.append(t)
    else:
        continue
for i in finished_list:
    print(f"{i}/{40}")

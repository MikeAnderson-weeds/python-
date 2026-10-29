
#素数有很多神奇的性质，所以很美。我们知道一个日期将年、月、日按顺序连接在一起可以组成一个八位数，
# 例如2011年3月6日可以写成20110306。如果某人的生日组成的数是一个素数可以叫Ta素宝宝。
# 请编程找出1988年,1989年的所有素宝宝。
#变量名：x i m n j k t u y num

import math
zhishu_list = []
begain_list = []
begain_list2 = []
def main():
    for i1 in make_zhishu():
        jianyan_f(i1)
    for i2 in sorted(zhishu_list):
        print(i2)
    

def make_zhishu():

    for i in list(range(1,13)):
        if 0 < i < 10:
            j1 = int("19880"+str(i))
            j2 = int("19890"+str(i))
            begain_list.extend([j1,j2])
        else:
            j3 = int("1988"+str(i))
            j4 = int("1989"+str(i))
            begain_list.extend([j3,j4])
    for h in begain_list:

        for p in list(range(1,32)):
            if 0 < p < 10:
                begain_list2.append(int(str(h)+"0"+str(p)))
            else:
                begain_list2.append(int(str(h)+str(p)))
    for t in begain_list2:
        if is_zhishu(t) == True:
            zhishu_list.append(t)
        else:
            continue
    return zhishu_list
def is_zhishu(u):
    u = int(u)
    if u < 2 :
        return False
    if u in (2,3):
        return True
    if u % 2 == 0:
        return False
    for y in range(3, int(math.isqrt(u)) + 1, 2):
        if u % y ==0:
            return False
    return True 
jianyan_list = ["0229","0230","0231","0431","0631","0931","1131"]
def jianyan_f(shu):
    SHU = str(shu)[-4:]
    if SHU in jianyan_list:
        zhishu_list.remove(shu)
    return zhishu_list

    
main()



#输出所有的"水仙花数"。所谓"水仙花数"是指这样的一个三位数：其各位数字的立方和等于该数本身。例如：371是一个"水仙花数"，371=33+73+13.
def main():
    for i in range(100,1000):
        if judge_SXH(i):
            print(i)
def judge_SXH(n):
    str_list  = list(str(n))
    num_list = []
    final_list = []
    for k in str_list:
        num_k = int(k)
        num_list.append(num_k)
    for i in num_list:
        lifang = i**3
        final_list.append(lifang)
    if n == sum(final_list):
        return True
    else :
        return False

main()
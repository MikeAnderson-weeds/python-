
#设t是一个小于 10 的自然数，n是一个正整数，求 s = t + tt + ttt + ··· ttt(n个t)
def main():
    t,n = map(int,input().split())
    print(sum(calculate(t,n)))

    
def calculate(i,j):
    final_list = []
    str_num = str(i)
    int(j)
    listed_num = list(range(1,j+1))
    for k in listed_num:
        result = int(str_num*k)
        final_list.append(result)
    return final_list


main()

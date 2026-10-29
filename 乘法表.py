
#输出九九口诀乘法表，要求口诀表的第i行第j列输出i*j=k的形式，中间用空格隔开
def main():
    for i in range(1,10):
        for j in range(1,10):
            k = i*j
            print(f"{i}*{j}={k}",end = " ")
main()

#中国古代数学著作《算经》中提出一个问题：公鸡每只5钱，母鸡每只3钱，小鸡1钱3只。若用100钱买100只鸡（每种鸡必须都买到，且钱不许有剩余），
# 输出所有的买法，
# 要求输出结果形式如“rooster=公鸡只数,hen=母鸡只数,chick=小鸡只数”，并且按公鸡只数由小到大的顺序输出，有多组解时分行输出。
def main():
    for (x,y,z) in buy():
        print(f"rooster={x},hen={y},chick={z}")

b_list = []
def buy():
    all_list = make_list()
    for (a,b,c) in all_list:
        if 5*a + 3*b + c*(1/3) == 100 and a + b + c ==100:
            b_list.append((a,b,c))
        else:
            continue
    return b_list
c_list = []
def make_list():
    for i in list(range(1,101)):
        for j in list(range(1,101)):
            for k in list(range(1,101)):
                c_list.append((i,j,k))
    return c_list
    
main()

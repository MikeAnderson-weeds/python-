
#把前n（n<=10000)个正整数顺序写在一起：123456789101112...数一数0-9各出现多少次。

def main():
    str_list = []
    get_start = int(input())
    for i in range(1,get_start + 1):
        str_num = str(i)
        str_list.append(str_num)
    result = "".join(str_list)
    listed_result = list(result)
    for i in range(0,10):
        print(calculate(i,listed_result))
def calculate(m,listed_result):
    num = 0
    for i in listed_result:
        if int(i) == m:
            num += 1
        else:
            continue
    return num


if __name__ == "__main__":
    main()


#给出一个由A和X组成的字符串（长度为1-80），统计字符总得分，
#其中每个A的得分为目前连续出现的A的个数，X的得分为0。例如AAXXAXXAAA的得分为1+2+1+1+2+3等于10。
def main():
    get_str = list(input())
    m = calculate_A(get_str)
    print(m)
def calculate_A(s):
    total_score = 0
    sum_A = 0
    for i in s:
        if i == "A":
            sum_A += 1
            total_score += sum_A
        else:
            sum_A = 0
    return total_score

if __name__ == "__main__":
    main()



    
    




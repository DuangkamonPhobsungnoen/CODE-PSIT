""" GCD_N """
def gcd_n(num_1, num_2):
    """ ฟังก์ชั่น GCD_N """
    while num_2:
        num_1, num_2 = num_2, num_1%num_2
    return num_1
def main(number, mylist, num):
    """ GCD_N """
    for _ in range(number):
        mylist += [(int(input()))]
    for i in range(0, len(mylist)):
        ans = gcd_n(num, mylist[i])
        num = ans
    print(ans)
main(int(input()), [], 0)

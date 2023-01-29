""" Dart """

def main():
    """ ฟังก์ชั่น Dart """
    ans = 0
    for _ in range(int(input())):
        number = input().split()
        summ = ((int(number[0])**2)+(int(number[1])**2))**0.5
        if 0 <= summ <= 2:
            ans += 5
        if 2 < summ <= 4:
            ans += 4
        if 4 < summ <= 6:
            ans += 3
        if 6 < summ <= 8:
            ans += 2
        if 8 < summ <= 10:
            ans += 1
        else:
            ans += 0
    print(ans)
main()

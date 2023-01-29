"""Compound Interest"""
def main(money, interest, time):
    """ฟังก์ชั่น Compound Interest"""
    for _ in range(time):
        money = money*(1+(interest/100))
    print('%.2f' %money)
main(int(input()), float(input()), int(input()))

"""HeadsAndLegs"""

def main():
    """ฟังก์ชั่น HeadsAndLegs"""
    num = int(input())
    legs = int(input())
    rabbit = (legs/2)-num
    crow = num-rabbit
    if rabbit < 0 or crow < 0 or legs % 2 != 0:
        print("Impossible")
    elif rabbit > 0 or crow > 0 or legs % 2 == 0:
        print("%d %d" %(rabbit, crow))
main()

"""PongYa"""
def main():
    """ฟังก์ชั่น PongYa"""
    num = int(input())
    if num%3 == 0 or num%10 == 3:
        print('PONG')
    elif num%3 != 0:
        print(num)
main()

"""GCD_v2"""
def main(number1, number2):
    """ฟังก์ชั่น GCD_v2"""
    while number2:
        number1, number2 = number2, number1%number2
    print(number1)
main(int(input()), int(input()))

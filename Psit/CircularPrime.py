"""CircularPrime"""

def prime(number1):
    """หาจำนวนเฉพาะช่วงที่กำหนด"""
    for number2 in range(2, int((number1**0.5) + 1)):
        if (number1%number2) == 0:
            break
    else:
        return number1
def cirpirme(number1):
    """ฟังก์ชันจำแนกจำนวนเฉพาะ"""
    str_number = str(number1)
    for number2 in range(0, len(str_number)):
        numr = str_number[number2:len(str_number)] + str_number[0:number2]
        if not prime(int(numr)):
            return False
    return True
def circularprime(number1, ans):
    """ฟังก์ชั่น CircularPrime"""
    for number2 in range(2, number1+1):
        if prime(number2) and cirpirme(number2):
            ans += number2
    print(ans)
circularprime(int(input()), 0)

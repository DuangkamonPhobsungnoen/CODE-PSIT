"""isPrime_large"""
def main(number):
    """ฟังก์ชั่น isPrime_large"""
    if number == 1:
        return 'NO'
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return 'NO'
    return 'YES'
print(main(int(input())))

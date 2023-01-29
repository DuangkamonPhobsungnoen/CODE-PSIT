"""max"""

def main():
    """การหาค่า max ถ้าไม่ใช้ฟังก์ชัน max"""
    number_1 = int(input())
    num_max = 0
    for _ in range(number_1):
        number_2 = int(input())
        if number_2 > num_max:
            num_max = number_2
    print(num_max)
main()

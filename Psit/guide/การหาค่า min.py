"""min"""

def main():
    """การหาค่า min ถ้าไม่ใช้ฟังก์ชัน min"""
    number_1 = int(input())
    for i in range(number_1):
        number_2 = int(input())
        if i == 0:
            num_min = number_2
        if number_2 < num_min:
            num_min = number_2
    print(num_min)
main()

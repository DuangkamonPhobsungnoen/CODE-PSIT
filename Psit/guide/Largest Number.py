"""max"""

def check(num1, num2):
    """ฟังก์ชันหาค่า max"""
    if num1 >= num2:
        return num1
    elif num1 <= num2:
        return num2
def main():
    """การหาค่า max จากเลขหลายตัว"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num1 = int(str(num_a) + str(num_b) + str(num_c))
    num2 = int(str(num_a) + str(num_c) + str(num_b))
    num3 = int(str(num_b) + str(num_a) + str(num_c))
    num4 = int(str(num_b) + str(num_c) + str(num_a))
    num5 = int(str(num_c) + str(num_a) + str(num_b))
    num6 = int(str(num_c) + str(num_b) + str(num_a))
    ans = check(num1, num2)
    ans = check(ans, num3)
    ans = check(ans, num4)
    ans = check(ans, num5)
    ans = check(ans, num6)
    print(ans)
main()

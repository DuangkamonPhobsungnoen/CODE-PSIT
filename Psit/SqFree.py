# """ลองเฉยๆอ่ะครับ"""
# def main(limit):
#     a = [True] * limit
#     yield 1
#     a[0] = a[1] = False
#     for i, is_square_free in enumerate(a):
#         if is_square_free:
#             yield i
#             i2 = i * i
#             for n in range(i2, limit, i2):
#                 a[n] = False
# test2 = len(set(main(int(input()))))
# print(test2)

"""SqFree"""

def main(number):
    """ฟังก์ชั่น SqFree"""
    for i in range(2, number+1):
        for j in range(2, int(i**0.5)+1):
            if i%(j**2) == 0:
                number -= 1
                break
    print(number)
main(int(input()))
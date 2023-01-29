"""Perfect"""


def main(number):
    """Perfect"""
    check = 0
    for num_per in range(2, number+1):
        result = 0
        for i in range(1, num_per):
            if (num_per % i) == 0:
                result += i
        if num_per == result and i > 1:
            check += num_per
    print(check)


main(int(input()))

# """Perfect"""

# def main(number, ans, total):
#     """Perfect"""
#     for i in range(2, number+1):
#         for j in range(1, int(i**0.5)+1):
#             if i%j == 0:
#                 total += j
#                 if j > 1 and j != i/j:
#                     total += i/j
#         if total == i:
#             ans += i
#         total = 0
#     return ans
# print(main(int(input()), 0, 0))

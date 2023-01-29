def sum_amicable(number):
    """ฟังก์ชั่น หาผลรวม amicable numbers ทั้งหมด"""
    ans = 0
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            ans += i
    return ans
def main(number, summ):
    """ amicable numbers """
    for i in range(4, number):
        if sum_amicable(i) > 4:
            if sum_amicable(i) != i and sum_amicable(sum_amicable(i)) == i:
                summ += i
    print(summ)
main(int(input()), 0)

# """Amicable"""
# def sum_factor(num):
#     """function1"""
#     result = []
#     for i in range(1, int(num**0.5) + 1):
#         if num % i == 0:
#             result.extend([i, num//i])
#     return sum(set(result)-set([num]))
# def amicable_pair(number):
#     """function2"""
#     result = []
#     for j in range(1, number+1):
#         you = sum_factor(j)
#         if sum_factor(you) == j and j != you:
#             result.append(tuple(sorted((j, you))))
#     return set(result)
# def main(ans):
#     """function3"""
#     preans = str(amicable_pair(int(input()))).replace("{", "").replace("}", "")\
#     .replace("(", "").replace(")", "").split(",")
#     for i in preans:
#         ans += int(i)
#     print(ans)
# main(0)

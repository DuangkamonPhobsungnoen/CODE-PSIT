"""NumDays"""

def main(day1, month1, day2, month2):
    """ฟังก์ชั่น NumDays"""
    keep_day1 = 0
    keep_day2 = 0
    day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, \
        9:30, 10:31, 11:30, 12:31}
    for i in range(1, month1):
        keep_day1 += day[i]
    for j in range(1, month2):
        keep_day2 += day[j]
    keep = abs((keep_day1+day1)-(keep_day2+day2))
    if day1 > day[month1] or day2 > day[month2]:
        print('Impossible')
    else:
        print(keep)
main(int(input()), int(input()), int(input()), int(input()))

# """NumDays"""
 
# def check(month):
#     """check"""
#     if month in [4, 6, 9, 11]:
#         return 30
#     elif month == 2:
#         return 28
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
 
# def main():
#     """Function NumDays"""
#     day1 = int(input())
#     month1 = int(input())
#     day2 = int(input())
#     month2 = int(input())
#     daysum = 0
#     if check(month1) != None and check(month2) != None and \
#         day1 <= check(month1) and day2 <= check(month2):
#         if month1 == month2:
#             print(abs(day2 - day1))
#         else:
#             daysum += check(month1) - day1
#             for i in range(month1+1, month2):
#                 daysum += check(i)
#             daysum += day2
#             print(abs(daysum))
#     else:
#         print("Impossible")
# main()
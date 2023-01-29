"""SMS"""

def main():
    """ฟังก์ชั่น SMS"""
    time = int(input())
    list_ans = []
    list_kub = ["CAB", "FDE", "IGH", "LJK", "OMN", "SPQR", "VTU", "XYZW"]
    for _ in range(time):
        num = int(input())
        num1 = int(input())
        if num == 1:
            list_ans = list_ans[0:-1*num1]
        elif num != 7 and num != 9 and num != 1:
            list_ans.append(list_kub[num-2][num1%3])
        else:
            list_ans.append(list_kub[num-2][num1%4])
    if list_ans == []:
        print('null')
    else:
        print(*list_ans, sep='')
main()

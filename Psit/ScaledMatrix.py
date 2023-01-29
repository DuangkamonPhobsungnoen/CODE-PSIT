""" ScaledMatrix """

def main():
    """ ฟังก์ชั่น ScaledMatrix """
    num_i = int(input())
    num_j = int(input())
    ans = []
    list_max = []
    count1 = ''
    for _ in range(num_j*num_i):
        data = float(input())
        ans.append(data)
    data_min = abs(min(ans))
    for i in ans:
        sum_ans = (float(i) + float(data_min))
        list_max.append(sum_ans)
        list_num = str(list_max).replace('[', '').replace(']', '').replace(',', '')
    data_max = max(list_max)
    for j in str(list_num).split():
        summ = float(j) / float(data_max)
        summ1 = '%.2f' %summ
        count1 += str(summ1)+" "
        if count1.count(" ")%num_j == 0:
            print(count1)
            count1 = ""
main()

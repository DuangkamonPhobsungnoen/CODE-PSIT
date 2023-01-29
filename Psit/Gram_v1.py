""" Gram_v1 """
def main():
    """ Gram_v1 """
    garm = input()
    ans = ""
    list_total = []
    list_num = []
    for i in garm:
        ans += i
        if len(ans) == 2:
            list_total.append(ans)
            ans = ans[-1]
    for j in range(len(list_total)):
        list_num.append(list_total.count(list_total[j]))
    list_nummax = max(list_num)
    print((list_total[list_num.index(list_nummax)]))
    print(list_nummax)
main()

""" Flatten """
def main(list_num, list_ans, list_i):
    """ Flatten """
    for i in list_num:
        if i.isnumeric() or i == '-':
            list_i += (i) #ทำให้เลขติดกัน
        else:
            if list_i.isnumeric() or list_i.find("-") != -1:
                list_ans += [(int(list_i))]
                list_i = ''
    list_ans.sort(reverse=True)
    print(list_ans)
main(input(), [], '')

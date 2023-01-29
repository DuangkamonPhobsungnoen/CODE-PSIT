""" OTP """
def oottpp(txt):
    """ OTP1 """
    ans = []
    for i in range(len(txt)):
        num = str(txt[i:]).count(txt[i])
        ans.append(num)
    return ans
def main():
    """ OTP2 """
    otp, ans = '', ''
    list_i = []
    while otp != "0":
        otp = input()
        data = (oottpp(otp))
        maxx = (max(data))
        check = (data.count(maxx))
        if len(otp) == 4:
            if maxx == 2 and check == 1:
                ans += "Valid "
            else:
                ans += "Invalid "
        elif len(otp) == 6:
            if (maxx == 3 and check == 1) or (maxx == 2 and check == 2):
                ans += "Valid "
            else:
                ans += "Invalid "
        elif len(otp) == 8:
            if (maxx == 3 and check == 2) or (maxx == 2 and check == 3):
                ans += "Valid "
            else:
                ans += "Invalid "
        else:
            ans += "Invalid "
    for i in ans.split():
        list_i.append(i)
    list_i.pop()
    print(*list_i, sep='\n')
main()

"""PrasomSib"""
def prasomsib(number, ans):
    """ฟังก์ชั่น PrasomSib"""
    for i in range(len(number)):
        count = 0
        for j in number[i:]:
            count += int(j)
            if count == 10:
                ans += 1
    print(ans)
prasomsib(input(), 0)

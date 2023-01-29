"""Solar System"""

def point(num, txt):
    """ฟังก์ชัน Solar System"""
    dao = ''
    for _ in range(num):
        fine_1 = str(txt).find(' ')
        dao = txt[:fine_1]
        txt = txt[fine_1 + 1:]
    return dao

def main():
    """Solar System"""
    txt_dao = input() #original
    total_dao = txt_dao.count(' ') + 1
    txt1 = txt_dao + ' '
    for i in range(1, total_dao+1):
        dao = point(i, txt1)
        if dao == 'Sun':
            losun = i
    hot, hot2, cool, cool2 = '', '', '', ''
    if losun == 1:
        hot = point(2, txt1)
    else:
        hot, hot2 = point(losun-1, txt1), point(losun+1, txt1)
    if losun-1 == total_dao-losun:
        cool, cool2 = point(1, txt1), point(total_dao, txt1)
    elif losun-1 < total_dao-losun:
        cool = point(total_dao, txt1)
    else:
        cool = point(1, txt1)
    print("Hot:", hot, hot2)
    print("Cool:", cool, cool2)
main()

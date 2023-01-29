"""i am mod"""

def temperature(temp, temp_now, temp_want):
    """ฟังก์ชั่น temperature"""
    if temp_now == 'F':
        temp = ((temp - 32) * (5/9))
    elif temp_now == 'K':
        temp = temp - 273.15
    elif temp_now == 'R':
        temp = (temp* (5/9)) - 273.15
    if temp_want == 'F':
        print('%.2f' %((temp * (9/5)) + 32))
    elif temp_want == 'K':
        print('%.2f' %(temp + 273.15))
    elif temp_want == 'R':
        print('%.2f' %((temp + 273.15) * (9/5)))
    elif temp_want == 'C':
        print('%.2f' %(temp))
temperature(float(input()), input(), input())


"""Fever"""
def temperature():
    """ฟังก์ชั่น Fever"""
    heat = float(input())
    if heat < 36:
        print('hypothermia')
    elif 36 <= heat < 38:
        print('No Fever')
    elif 38 <= heat < 39:
        print('Mild Fever')
    elif 39 <= heat < 40:
        print('High Fever')
    elif 40 <= heat:
        print('Very High Fever')
temperature()
#Natcha Surapongwuttikul
"""i am mod"""

def inverter(inverter11, ans):
    """https://youtu.be/UHpJzCd_lXo"""
    for i in inverter11:
        if i == '1':
            ans += '0'
        elif i == '0':
            ans += '1'
    print(ans.lstrip('0'))
inverter(input(), '')

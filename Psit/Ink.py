"""Ink"""
def main():
    """Ink"""
    import math
    number = input().split()
    for _ in range(int(number[1])):
        count = input().split()
        print(math.ceil(((3.1416)*(((int(count[0])**2 + int(count[1])**2)**0.5))**2)\
            /(int(number[0]))))
main()

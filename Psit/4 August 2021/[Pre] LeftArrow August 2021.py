"""[Pre] LeftArrow"""
 
def main():
    """[Pre] LeftArrow"""
    width = int(input())
    height = int(input())
    sum1 = height//2
    for i in range(sum1): #ช่องว่างบน
        print(' '*(sum1-i), end='')
        print("*"*width)
    print("*"*width)
    for i in range(sum1): #ช่องว่างล่าง
        print(' '*(i+1), end='')
        print("*"*width)
main()
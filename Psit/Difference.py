""" Difference """
def main():
    """ ฟังก์ชั่น Difference """
    num_a = int(input())
    num_b = int(input())
    myset_a = set()
    myset_b = set()
    for _ in range(num_a):
        num_1 = int(input())
        myset_a.add(num_1)
    for _ in range(num_b):
        num_2 = int(input())
        myset_b.add(num_2)
    data = sorted((myset_a - myset_b)) #data = sorted((myset_a.difference(myset_b)))
    for i in data:
        print(i, end=' ')
    print()
main()

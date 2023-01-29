"""Point Sorting"""
def main(mylist):
    """ฟังก์ชั่น Point Sorting"""
    for _ in range(int(input())):
        for _ in range(int(input())):
            mylist.append(tuple(input().split()))
        mylists = sorted(mylist, key=lambda x: x[1], reverse=True)
        mylist_sort = sorted(mylists, key=lambda x: int(x[0]) + int(x[1]))
        for i in mylist_sort:
            print(*i)
        mylist_sort, mylists, mylist = [], [], []
main([])

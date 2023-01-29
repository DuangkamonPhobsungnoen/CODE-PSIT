"""Matrix_MN"""
def main():
    """ฟังก์ชั่น Matrix_MN"""
    num_i = int(input())
    num_j = int(input())
    ans = ''
    for _ in range(num_i):
        for _ in range(num_j):
            data = str(int(input()))+" "
            ans += data
        print(ans, sep='')
        ans = ''
main()

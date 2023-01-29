"""CoinChangev1"""
def main():
    """ฟังก์ชั่น CoinChangev1"""
    coin = int(input())
    count = 0
    if coin >= 0:
        count_coin = coin//25
        count += count_coin
        check_count = coin%25
    if 10 <= check_count < 25:
        count += check_count//10
        check_count = check_count%10
    if 5 <= check_count < 10:
        count += check_count//5
        check_count = check_count%5
    if 1 <= check_count < 5:
        count += check_count
        check_count = check_count%1
    print(count)
main()

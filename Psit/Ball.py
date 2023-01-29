""" Ball """
def main(num, count):
    """ ฟังก์ชั่น Ball """
    while True:
        num = num*(3/5)
        if (num*100) < 1:
            break
        else:
            count += 1
    print(count)
main(float(input()), 0)

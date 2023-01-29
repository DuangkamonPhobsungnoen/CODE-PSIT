"""i am ingfah"""
def main(number):
    """https://youtu.be/JoZRrvZQN-E"""
    txt = True
    if number > 1:
        if number % 2 != 0 and number != 2:
            for i in range(3, int(number**0.5)+1, 2):
                if number % i == 0:
                    txt = False
                    break
        else:
            if number == 2:
                txt = True
            else:
                txt = False
    else:
        txt = False
    print(txt)
main(int(input()))

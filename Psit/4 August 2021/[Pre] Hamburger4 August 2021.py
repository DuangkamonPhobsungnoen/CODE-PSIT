"""[Pre] Hamburger"""
 
def main():
    """[Pre] Hamburger"""
    left = int(input())
    right = int(input())
    sum_left_right = (left+right)*2
    print(left*"|"+sum_left_right*"*"+right*"|")
main()
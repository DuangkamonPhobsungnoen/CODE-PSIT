"""WordSequence II"""

def main(word):
    """WordSequence II"""
    print('⭐')
    for i in range(len(word)+1):
        w = word[:i]
        print((' '*(abs(i-(len(word)))))+'⭐'*i)
        print((' '*(abs(i-(len(word)))))+(word[:i])+w[::-1])
main(input())

"""I am ingfah"""
def main():
    """Password"""
    import hashlib
    txt = hashlib.new('sha512')
    txt.update(input().encode('UTF-8'))
    print(txt.hexdigest().upper())
main()

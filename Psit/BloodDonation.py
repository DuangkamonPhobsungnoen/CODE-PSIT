"""BloodDonation"""

def main():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    blood = int(input())
    if 17 < age < 60 and weight >= 45:
        if blood == 0 and age > 55:
            print('No')
        else:
            print('Yes')
    elif 17 == age or (60 <= age <= 70):
        allow = str(input())
        if weight >= 45 and allow == 'True':
            if age > 55 and blood == 0:
                print('No')
            else:
                print('Yes')
        else:
            print('No')
    else:
        print('No')
main()

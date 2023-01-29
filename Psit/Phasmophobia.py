""" Phasmophobia """
def main(txt1, txt2, txt3):
    """ ฟังก์ชั่น Phasmophobia """
    txt_list = []
    ans = ''
    txt_list.append(txt1)
    txt_list.append(txt2)
    txt_list.append(txt3)
    ghost1 = txt_list.count('EMF Level 5')
    ghost2 = txt_list.count('Ghost Writing')
    ghost3 = txt_list.count('Fingerprints')
    ghost4 = txt_list.count('Spirit Box')
    ghost5 = txt_list.count('Freezing Temperatures')
    ghost6 = txt_list.count('Ghost Orb')
    notghost = txt_list.count('No evidence')
    if (ghost1 + ghost3 + ghost5 + notghost) > 2:
        ans += 'Banshee '
    if (ghost2 + ghost4 + ghost5 + notghost) > 2:
        ans += 'Demon '
    if (ghost1 + ghost4 + ghost6 + notghost) > 2:
        ans += 'Jinn '
    if (ghost4 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Mare '
    if (ghost1 + ghost2 + ghost4 + notghost) > 2:
        ans += 'Oni '
    if (ghost1 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Phantom '
    if (ghost3 + ghost4 + ghost6 + notghost) > 2:
        ans += 'Poltergeist '
    if (ghost1 + ghost2 + ghost3 + notghost) > 2:
        ans += 'Revenant '
    if (ghost1 + ghost2 + ghost6 + notghost) > 2:
        ans += 'Shade '
    if (ghost2 + ghost3 + ghost4 + notghost) > 2:
        ans += 'Spirit '
    if (ghost3 + ghost4 + ghost5 + notghost) > 2:
        ans += 'Wraith '
    if (ghost2 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Yurei '
    ans = ans.split()
    ans.sort()
    return ans
def phasmophobia(ans):
    """function2"""
    if ans != []:
        print(*ans, sep='\n')
    else:
        print('Not yet discovered')
phasmophobia(main(input(), input(), input()))

#'EMF Level 5' 'Ghost Writing' 'Fingerprints' 'Spirit Box' 'Freezing Temperatures' 'Ghost Orb'
#       1              2               3            4                 5                 6
#Banshee      --> 'EMF Level 5'     'Fingerprints'              'Freezing Temperatures'
#Demon       --> 'Ghost Writing'    'Spirit Box'                'Freezing Temperatures'
#jinn        --> 'EMF Level 5'      'Spirit Box'                'Ghost Orb'
#Mare        --> 'Spirit Box'       'Freezing Temperatures'     'Ghost Orb'
#Oni         --> 'EMF Level 5'      'Ghost Writing'             'Spirit Box'
#Phantom     --> 'EMF Level 5'      'Freezing Temperatures'     'Ghost Orb'
#Poltergeist --> 'Fingerprints'     'Spirit Box'                'Ghost Orb'
#Revenant    --> 'EMF Level 5'      'Ghost Writing'             'Fingerprints'
#Shade       --> 'EMF Level 5'      'Ghost Writing'             'Ghost Orb'
#Spirit      --> 'Ghost Writing'    'Fingerprints'              'Spirit Box'
#Wraith      --> 'Fingerprints'     'Spirit Box'                'Freezing Temperatures'
#Yurei       --> 'Ghost Writing'    'Freezing Temperatures'     'Ghost Orb'

# """[Recommend] Phasmophobia"""
# def main():
#     """[Recommend] Phasmophobia"""
#     txt1 = input()
#     txt2 = input()
#     txt3 = input()
#     mydict = {"EMF Level 5" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade']\
#             , "Ghost Writing" : ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei']\
#             , "Fingerprints" : ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith']\
#             , "Spirit Box" : ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith']\
#             , "Freezing Temperatures" : ['Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei']\
#             , "Ghost Orb" : ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei']\
#             , "No evidence" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade', 'Demon', \
#             'Mare', 'Poltergeist', 'Spirit', 'Wraith', 'Yurei']}
#     ans = list(set(set(mydict[txt1]).intersection(mydict[txt2])).intersection(mydict[txt3]))
#     if ans == []:
#         print("Not yet discovered")
#     else:
#         print(*sorted(ans), sep="\n")
# main()

import random 

crtanje_kockica = {
        1: '''
            -----
            |   |
            | o |
            |   |
            -----''',
        2: '''
            -----
            |o  |
            |   |
            |  o|
            -----''',
        3: '''
            -----
            |o  |
            | o |
            |  o|
            -----''',
        4: '''
            -----
            |o o|
            |   |
            |o o|
            "-----''',
        5: '''
            -----
            |o o|
            | o |
            |o o|
            -----''',

        6:'''
            -----
            |o o|
            |o o|
            |o o|
            -----'''
        
    }

def baci_kockice():

    baci = input("Želite li baciti kockice? (Da/Ne) :")

    while baci.lower() == "da":
        kockica1 = random.randint(1, 6)
        kockica2 = random.randint(1, 6)

        # print(f"Kockice su bačene: {kockica1} i {kockica2}")
        print()
        print(crtanje_kockica[kockica1])
        print()
        print(crtanje_kockica[kockica2])
        
        baci = input("Baciti ponovno? (Da/Ne)")

baci_kockice()
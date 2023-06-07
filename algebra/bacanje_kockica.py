import random

kockica1 = random.randint(1, 6)
kockica2 = random.randint(1, 6)


def baci_kockice():

    crtanje_kockica = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----"
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----"
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----"
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----"
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----"
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----"
        ),

    }

    baci = input('Zelite li baciti kockice? (Da/Ne) :')

    while baci.lower() == "da":
        kockica1 = random.randint(1, 6)
        kockica2 = random.randint(1, 6)

        print(f'Kockice su bacene: {kockica1} i {kockica2}')
        print()
        print('\n'.join(crtanje_kockica[kockica1]))
        print()
        print('\n'.join(crtanje_kockica[kockica2]))

        baci = input('Baciti ponovno? (Da/Ne)')


baci_kockice()

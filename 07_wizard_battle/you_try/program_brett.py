
import time
from actors import Wizard, Creature, SmallAnimal, Dragon
import random

def main():
    print_header()
    game_loop()

def print_header():
    pass


def game_loop():

    creatures = [
        SmallAnimal("frog", 1),
        SmallAnimal("squirrel", 3),
        Dragon("Dragon", 50, 20, 1),
        Wizard("Evil Wizard", 100)
    ]

    hero = Wizard('Gandalf', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and scary forest...'.format(
            active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd =='a':
            #Using truthiness: if wizard wins roll True is returned
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover")
                time.sleep(5)
                print("The wizard returns revitalized")
        elif cmd =='r':
            print('The wizard has become unsure of his power and flees')
        elif cmd == 'l':
            print('You look around and see')
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting game. Bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            print("GAME OVER")



if __name__ == '__main__':
    main()
import random


class Creature:
    """An opponent that the player will encounter in the wild". Creatures have the following properties:

    Attributes:
        name: A string representing the creature's name.
        the_level: An integer representing the level of a creature
    """

    def __init__(self, name, the_level):
        """Return a Create object whose name is *name* and whose attack and health is (10, 20), respectively"""
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        result = random.randint(1, 12) * self.level
        return result



class Wizard(Creature):
    """The main character of the game, played by the user"""
    """Return a Create object whose name is *name* and whose attack and health is (10, 20), respectively"""

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!")
            return False



class Dragon(Creature):

    def __init__(self, name, level, scale_thickness, breaths_fire):
       super().__init__(name, level)
       self.scale_thickness = scale_thickness
       self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scale_thickness / 10

        return base_roll * fire_modifier * scale_modifier



class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2
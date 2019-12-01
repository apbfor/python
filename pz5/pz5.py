from datetime import date

class Human:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")


class Planet:
    """
    Planet doc
    """
    def __init__(self, name, mass=None, population=None):
        self.name = name
        self.mass = mass
        self.population = population or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Planet {0}".format(self.name)

    def add_human(self, human):
        print("Welcome to {0}, {1}!".format(self.name, human.name))
        self.population.append(human)


class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return "Event \"{0}\" at {1}".format(self.description, self.date)



def main():
    solar_system = []
    planet_names = [
        "Mercury", "Venus", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune"
    ]

    for name in planet_names:
        planet = Planet(name)
        solar_system.append(planet)

    bob = Human("Bob", 29)
    bob.say_name()
    bob.say_how_old()

    event_description = "@classmethod"
    event_date = date.today()
    event = Event(event_description, event_date)
    print(event)
    for letter in 'python':
        print(ord(letter))
    bob._say("Whatever we want")

    for num in SquareIterator(1, 5):
        print(num)

class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result

if __name__ == '__main__':
    main()

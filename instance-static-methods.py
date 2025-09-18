class Pokemon:
    god_pokemon = "Arceus"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def call_name(poke):
        k = f"So you consider {poke} as the God pokemon."
        print(k)

a = Pokemon("Zapdos")
# call staticmethod either via class or pass the name explicitly
a.call_name(a.name)
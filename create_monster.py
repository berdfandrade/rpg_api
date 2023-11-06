import random
import simplejson as json

# CLASS > Monster Attributes

class Monster:
    def __init__(self, name, attack, defense, temperament, level, hp, stamina, species):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.temperament = temperament
        self.level = level
        self.hp = hp
        self.stamina = stamina
        self.species = species
    
    def __str__(self):
        return f"Monster: {self.name}, Species: {self.species}, Temperament: {self.temperament}, Level: {self.level}, HP: {self.hp}, Stamina: {self.stamina}, Attack: {self.attack}, Defense: {self.defense}"

# Function to generate monster's name

def generate_monster_name():
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    name_length = random.randint(2, 3)  # Determines a random length for the monster's name

    monster_name = ''
    for _ in range(name_length):
        if random.choice([True, False]):
            monster_name += random.choice(consonants)
        monster_name += random.choice(vowels)

    return monster_name.capitalize()

# Randomly choose a species for this monster

def choose_monster_species():
    species = [
        'Dragon',
        'Ogre',
        'Specter',
        'Giant',
        'Vampire',
        'Chimera',
        'Goblin',
        'Minotaur',
        'Gargoyle',
        'Siren',
        'Werewolf',
        'Cyclops',
        'Kraken',
        'Elemental',
        'Harpy',
        'Griffin',
        'Basilisk',
        'Centaur',
        'Succubus',
        'Yeti'
    ]

    random_species = random.choice(species)
    return random_species

# Generate stats proportional to the level, randomly for the monster

def generate_monster_stats():
    level = random.randint(1, 99)
    hp = level * 100
    stamina = level * 50
    attack = level * 30
    defense = level * 20

    return {'level': level, 'hp': hp, 'stamina': stamina, 'attack': attack, 'defense': defense}

def choose_monster_temperament():
    temperaments = [
        'Aggressive',
        'Cautious',
        'Playful',
        'Shy',
        'Fierce',
        'Peaceful',
        'Cunning',
        'Unpredictable',
        'Curious',
        'Sarcastic'
    ]

    random_temperament = random.choice(temperaments)
    return random_temperament

def generate_monster():
    stats = generate_monster_stats()
    generated_level = stats['level']
    generated_hp = stats['hp']
    generated_stamina = stats['stamina']
    generated_attack = stats['attack']
    generated_defense = stats['defense']
    generated_name = generate_monster_name()
    generated_species = choose_monster_species()
    generated_temperament = choose_monster_temperament()

    generated_monster = Monster(name=generated_name, species=generated_species, temperament=generated_temperament, level=generated_level, hp=generated_hp, stamina=generated_stamina, attack=generated_attack, defense=generated_defense)
    

    monster_dict = {
        'Name': generated_monster.name,
        'Species': generated_monster.species,
        'Temperament': generated_monster.temperament,
        'Level': generated_monster.level,
        'HP': generated_monster.hp,
        'Stamina': generated_monster.stamina,
        'Attack': generated_monster.attack,
        'Defense': generated_monster.defense
    }

    monster_json = json.dumps(monster_dict, ensure_ascii=False)
    return monster_json

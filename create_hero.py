import random
import json
from items import generate_inventory

class Hero:
    def __init__(self, name, attack, defense, temperament, level, hp, stamina, nickname, gender, inventory):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.temperament = temperament
        self.level = level
        self.hp = hp
        self.stamina = stamina
        self.nickname = nickname
        self.gender = gender
        self.inventory = inventory
    
    def __str__(self):
        return f"Hero: {self.name}, Temperament: {self.temperament}, Level: {self.level}, HP: {self.hp}, Stamina: {self.stamina}, Attack: {self.attack}, Defense: {self.defense}, Nickname: {self.nickname}, Inventory: {self.inventory}"
    
    def presentation(self):
        if self.gender == 'Male':
            return f"{self.name}, the {self.nickname}"
        elif self.gender == 'Neutral':
            return f"{self.name}, {self.nickname}"
        else:
            return f"{self.name}, the {self.nickname}"

def generate_hero_name():
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    name_length = random.randint(2, 3)  # Determines a random length for the hero's name

    hero_name = ''
    for _ in range(name_length):
        if random.choice([True, False]):
            hero_name += random.choice(consonants)
        hero_name += random.choice(vowels)

    hero_name = hero_name.capitalize()

    return hero_name

def define_hero_gender():
    gender = random.choice(['Male', 'Female', 'Neutral'])
    
    return gender

def generate_hero_nickname(gender):
    adjectives = [
        'Powerful',
        'Fearless',
        'Valiant',
        'Intrepid',
        'Courageous',
        'Heroic',
        'Brave',
        'Vigilant',
        'Audacious',
        'Fearless',
        'Magnificent',
        'Majestic',
        'Glorious',
        'Radiant',
        'Invincible',
        'Noble',
        'Wise',
        'Just'
    ]
    
    random_adjective = random.choice(adjectives)
    
    return random_adjective

def generate_hero_stats():
    level = random.randint(1, 99)
    hp = level * 100
    stamina = level * 50
    attack = level * 30
    defense = level * 20

    return {'level': level, 'hp': hp, 'stamina': stamina, 'attack': attack, 'defense': defense}

def generate_hero():
    stats = generate_hero_stats()
    hero_name = generate_hero_name()
    hero_gender = define_hero_gender()
    hero_nickname = generate_hero_nickname(hero_gender)
    hero_attack = stats['attack']
    hero_defense = stats['defense']
    hero_temperament = random.choice(['Aggressive', 'Defensive', 'Balanced'])
    hero_level = stats['level']
    hero_hp = stats['hp']
    hero_stamina = stats['stamina']
    inventory = generate_inventory(stats['level'])
    
    hero = Hero(hero_name, hero_attack, hero_defense, hero_temperament, hero_level, hero_hp, hero_stamina, hero_nickname, hero_gender, inventory)
    
    hero_dict = {
        "Name": hero.name,
        "Attack": hero.attack,
        "Defense": hero.defense,
        "Temperament": hero.temperament,
        "Level": hero.level,
        "HP": hero.hp,
        "Stamina": hero.stamina,
        "Nickname": hero.nickname,
        "Gender": hero.gender,
        "Presentation" : hero.presentation(),
        "Inventory" : hero.inventory
    }
    
    hero_json = json.dumps(hero_dict, ensure_ascii=False)
    return hero_json

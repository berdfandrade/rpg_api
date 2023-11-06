import random

items_lv_1_15 = {
    "Crow Feather": 1,
    "Common Precious Stone": 2,
    "Light Healing Potion": 3,
    "Wooden Arrow": 4,
    "Fresh Bread": 5,
    "Wolf Leather": 6,
    "Rusty Key": 7,
    "Whetstone": 8,
    "Extinguished Torch": 9,
    "Worn-out Rope": 10,
    "Bronze Dagger": 11,
    "Small Coin Pouch": 12,
}

items_lv_15_25 = {
    "Beaded Necklace": 13,
    "Torn Map": 14,
    "Ripe Apple": 15,
    "Wooden Bow": 16,
    "Sleeping Bag": 17,
    "Fire Resistance Potion": 18,
    "Brass Ring": 19,
    "Iron Short Sword": 20,
    "Silver Arrow": 21,
    "Woolen Cape": 22,
    "Wooden Flute": 23,
    "Carnival Mask": 24,
    "Participation Medal": 25,
    "Empty Spell Book": 26,
    "Enigmatic Scroll": 27,
    "Leather Helm": 28,
    "Silver Bracelet": 29,
    "Strength Elixir": 30,
    "Fire Stone": 31,
    "Fishing Rod": 32,
    "Small Backpack": 33,
    "Silver Star": 34,
    "Small Bronze Bell": 35,
    "Universal Antidote": 36,
    "Half-Full Wine Bottle": 37,
}

items_lv_25_35 = {
    "Thunder Stone": 38,
    "Feather Brooch": 39,
    "Leather Gloves": 40,
    "Reading Glasses": 41,
    "Pocket Mirror": 42,
    "Blacksmith's Hammer": 43,
    "Golden Key": 44,
    "Amulet of Protection": 45,
    "Invisibility Potion": 46,
    "Honey Bread": 47,
    "Unicorn's Tear": 48,
    "Piccolo": 49,
    "Willow Wand": 50,
    "Treasure Map": 51,
    "Jade Bracelet": 52,
    "Magic Wand": 53,
    "Leather Belt": 54,
    "Ruby Ring": 55,
    "Peacock Feather": 56,
    "Crystal Sphere": 57,
    "Ancient History Book": 58,
    "Gold Ring": 59,
    "Speed Potion": 60,
    "Magic Staff": 61,
    "Leather Boots": 62,
    "Enchanted Flower": 63,
    "Star Map": 64,
    "Ice Crystal": 65,
    "Iron Helm": 66,
}

items_lv_35_55 = {
    "Pearl Necklace": 67,
    "Major Healing Potion": 68,
    "Energy Orb": 69,
    "Sapphire Ring": 70,
    "Stone Key": 71,
    "Silk Gloves": 72,
    "Summoning Scroll": 73,
    "Ancient Statue": 74,
    "Golden Flute": 75,
    "Wisdom Tome": 76,
    "Power Ring": 77,
    "Wizard's Staff": 78,
    "Labyrinth Map": 79,
    "Wind Crystal": 80,
    "Heroic Helm": 81,
}

items_lv_55_67 = {
    "Opal Necklace": 82,
    "Permanent Invisibility Potion": 83,
    "Iron Shield": 84,
    "Silver Flute": 85,
    "Ritual Mask": 86,
    "Diamond Ring": 87,
    "Enchanted Cloak": 88,
    "Fire Crystal": 89,
    "Magic Diary": 90,
    "Phoenix Plume": 91,
    "Magic Compass": 92,
    "Elixir of Life": 93,
    "Golden Scarab": 94,
    "Wizard's Staff": 95,
    "Flying Boots": 96,
    "Enchanted Bracelet": 97,
    "Amber Necklace": 98,
    "Silver Cauldron": 99,
    "Dimensional Map": 100,
    "Crystal Globe": 101,
    "Enchanted Lyre": 102,
    "Magic Sword": 103,
    "Sacred Shield": 104,
    "Ring of Destiny": 105,
}

items_lv_67_78 = {
    "Ruby Crown": 106,
    "Moonstone": 107,
    "Silk Dress": 108,
    "Time Orb": 109,
    "Supreme Healing Potion": 110,
    "Celestial Bow": 111,
    "Platinum Coin Bag": 112,
    "Amulet of Power": 113,
    "Ebony Wand": 114,
    "Ancient Map": 115,
    "Enchanted Medallion": 116,
    "Emerald Necklace": 117,
    "Sun Stone": 118,
    "Royal Scepter": 119,
    "Divine Shield": 120,
    "King's Crown": 121,
    "Kingdom Key": 122,
}

items_lv_78_85 = {
    "Book of Prophecies": 123,
    "Navigator's Compass": 124,
    "Time Hourglass": 125,
    "Elixir of Eternity": 126,
    "Resurrection Stone": 127,
    "Golden Armor": 128,
    "Divine Staff": 129,
    "Celestial Lance": 130,
    "Wisdom Orb": 131,
    "Diamond Crown": 132,
    "Legendary Sword": 133,
    "Dragon Necklace": 134,
    "Infinite Crystal": 135,
    "Shadow Mantle": 136,
}

items_lv_85_99 = {
    "Hero's Shield": 137,
    "Ring of Immortality": 138,
    "Magic Key": 139,
    "Ancient Tomes": 140,
    "Black Pearl": 141,
    "Destiny Crown": 142,
    "Archangel's Staff": 143,
    "Divine Spear": 144,
    "Conqueror's Helm": 145,
    "Universe Orb": 146,
    "Omniscience Ring": 147,
    "Harmony Necklace": 148,
    "Excalibur Sword": 149,
    "King's Throne": 150,
    "Illusion Mirror": 151,
    "Speed Boots": 152,
    "Thunder Gloves": 153,
    "Invisibility Cape": 154,
    "Protection Ring": 155,
    "Wisdom Amulet": 156,
    "Fate Bow": 157,
    "Heroic Helm": 158,
}

def generate_inventory(level):
    inventory = []
    random_number = random.randint(3, 12)
    
    for _ in range(random_number):
        if level <= 15:
            item = random.choice(list(items_lv_1_15.keys()))
        elif level <= 25:
            item = random.choice(list(items_lv_15_25.keys()))
        elif level <= 35:
            item = random.choice(list(items_lv_25_35.keys()))
        elif level <= 55:
            item = random.choice(list(items_lv_35_55.keys()))
        elif level <= 67:
            item = random.choice(list(items_lv_55_67.keys()))
        elif level <= 78:
            item = random.choice(list(items_lv_67_78.keys()))
        elif level <= 85:
            item = random.choice(list(items_lv_78_85.keys()))
        else:
            item = random.choice(list(items_lv_85_99.keys()))
        inventory.append(item)
    return inventory


import random
import simplejson as json

# CLASS > Atributos do monstro 

class Monstro:
    def __init__(self, nome, ataque, defesa, temperamento, level, hp, stamina, especie):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.temperamento = temperamento
        self.level = level
        self.hp = hp
        self.stamina = stamina
        self.especie = especie
    
    def __str__(self):
        return f"Monstro: {self.nome}, Espécie: {self.especie}, Temperamento: {self.temperamento}, Level: {self.level}, HP: {self.hp}, Stamina: {self.stamina}, Ataque: {self.ataque}, Defesa: {self.defesa}"


# Função que gera o nome do monstro 

def gerar_nome_monstro():
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    tamanho_nome = random.randint(2, 3)  # Determina um tamanho aleatório para o nome do monstro

    nome_monstro = ''
    for _ in range(tamanho_nome):
        if random.choice([True, False]):
            nome_monstro += random.choice(consoantes)
        nome_monstro += random.choice(vogais)

    return nome_monstro.capitalize()

# Gera escolhe aleatoriamente uma especie para esse monstro 

def escolher_especie_monstro():
    especies = [
        'Dragão',
        'Ogro',
        'Espectro',
        'Gigante',
        'Vampiro',
        'Quimera',
        'Goblin',
        'Minotauro',
        'Gárgula',
        'Sereia',
        'Lobisomem',
        'Cíclope',
        'Kraken',
        'Elemental',
        'Harpia',
        'Grifo',
        'Basilisco',
        'Centauro',
        'Succubus',
        'Yeti'
    ]

    especie_aleatoria = random.choice(especies)
    return especie_aleatoria

# Gerando os stats proporicional ao level, aleatório do monsto 


def gerar_stats_monstro():
    level = random.randint(1, 99)
    hp = level * 100
    stamina = level * 50
    ataque = level * 30
    defesa = level * 20

    return {'level': level, 'hp': hp, 'stamina': stamina, 'ataque': ataque, 'defesa': defesa}



def escolher_temperamento_monstro():
    temperamentos = [
        'Agressivo',
        'Cauteloso',
        'Brincalhão',
        'Tímido',
        'Feroz',
        'Pacífico',
        'Astuto',
        'Imprevisível',
        'Curioso',
        'Sarcástico'
    ]

    temperamento_aleatorio = random.choice(temperamentos)
    return temperamento_aleatorio


def gerar_monstro():
    stats = gerar_stats_monstro()
    level_gerado = stats['level']
    hp_gerado = stats['hp']
    stamina_gerado = stats['stamina']
    ataque_gerado = stats['ataque']
    defesa_gerado = stats['defesa']
    nome_gerado = gerar_nome_monstro()
    especie_gerado = escolher_especie_monstro()
    temperamento_gerado = escolher_temperamento_monstro()

    monstro_gerado = Monstro(nome=nome_gerado, especie=especie_gerado, temperamento=temperamento_gerado, level=level_gerado, hp=hp_gerado, stamina=stamina_gerado, ataque=ataque_gerado, defesa=defesa_gerado)
    

    monstro_dict = {
        
        'Nome': monstro_gerado.nome,
        'Espécie': monstro_gerado.especie,
        'Temperamento': monstro_gerado.temperamento,
        'Level': monstro_gerado.level,
        'HP': monstro_gerado.hp,
        'Stamina': monstro_gerado.stamina,
        'Ataque': monstro_gerado.ataque,
        'Defesa': monstro_gerado.defesa
    }

   

    monstro_json = json.dumps(monstro_dict, ensure_ascii=False)
    return monstro_json


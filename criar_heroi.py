

import random
import json
from items import gerar_inventario

class Heroi:
    def __init__(self, nome, ataque, defesa, temperamento, level, hp, stamina, alcunha, genero, inventario):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.temperamento = temperamento
        self.level = level
        self.hp = hp
        self.stamina = stamina
        self.alcunha = alcunha
        self.genero = genero
        self.invetario = inventario
    
    def __str__(self):
        return f"Herói: {self.nome}, Temperamento: {self.temperamento}, Level: {self.level}, HP: {self.hp}, Stamina: {self.stamina}, Ataque: {self.ataque}, Defesa: {self.defesa}, Alcunha: {self.alcunha}, Inventário: {self.invetario}"
    
   
    def apresentacao(self):
        if self.genero == 'Masculino':
            return f"{self.nome}, o {self.alcunha}"
        elif self.genero == 'Neutro':
            return f"{self.nome}, {self.alcunha}"
        else:
            return f"{self.nome}, a {self.alcunha}"

def gerar_nome_heroi():
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    tamanho_nome = random.randint(2, 3)  # Determina um tamanho aleatório para o nome do herói

    nome_heroi = ''
    for _ in range(tamanho_nome):
        if random.choice([True, False]):
            nome_heroi += random.choice(consoantes)
        nome_heroi += random.choice(vogais)

    nome_heroi = nome_heroi.capitalize()

    return nome_heroi

def definir_genero_heroi():
    genero = random.choice(['Masculino', 'Feminino', 'Neutro'])
    if genero == 'Masculino':
        nome_heroi = gerar_nome_heroi() + 'o'
    elif genero == 'Feminino':
        nome_heroi = gerar_nome_heroi() + 'a'
    else:
        nome_heroi = gerar_nome_heroi() + 'x'
    
    return nome_heroi, genero

def gerar_alcunha_heroi(genero):
    if genero == 'Masculino':
        sufixo = 'o'
    elif genero == 'Feminino':
        sufixo = 'a'
    else:
        sufixo = 'e'
        
    adjetivos = [
        'Poderos',
        'Destemid',
        'Valente',
        'Intrépid',
        'Corajos',
        'Heroic',
        'Brav',
        'Vigilante',
        'Audaz',
        'Impávid',
        'Indômit',
        'Temerári',
        'Magnífic',
        'Majestos',
        'Glorios',
        'Radiante',
        'Invencível',
        'Nobre',
        'Sábi',
        'Just'
    ]
    
    adjetivo_aleatorio = random.choice(adjetivos)
    
    if adjetivo_aleatorio in ['Valente', 'Vigilante', 'Audaz', 'Radiante', 'Invencível']:
        alcunha = adjetivo_aleatorio
    else:
        alcunha = adjetivo_aleatorio + sufixo
    
    return alcunha

def gerar_stats_heroi():
    level = random.randint(1, 99)
    hp = level * 100
    stamina = level * 50
    ataque = level * 30
    defesa = level * 20

    return {'level': level, 'hp': hp, 'stamina': stamina, 'ataque': ataque, 'defesa': defesa}

def gerar_heroi():
    stats = gerar_stats_heroi()
    nome_heroi, genero_heroi = definir_genero_heroi()
    alcunha_heroi = gerar_alcunha_heroi(genero_heroi)
    ataque_heroi = stats['ataque']
    defesa_heroi = stats['defesa']
    temperamento_heroi = random.choice(['Agressivo', 'Defensivo', 'Equilibrado'])
    level_heroi = stats['level']
    hp_heroi = stats['hp']
    stamina_heroi = stats['stamina']
    inventario = gerar_inventario(stats['level'])
    
    heroi = Heroi(nome_heroi, ataque_heroi, defesa_heroi, temperamento_heroi, level_heroi, hp_heroi, stamina_heroi, alcunha_heroi, genero_heroi, inventario )
    
    heroi_dict = {
        "Nome": heroi.nome,
        "Ataque": heroi.ataque,
        "Defesa": heroi.defesa,
        "Temperamento": heroi.temperamento,
        "Level": heroi.level,
        "HP": heroi.hp,
        "Stamina": heroi.stamina,
        "Alcunha": heroi.alcunha,
        "Gênero": heroi.genero,
        "Apresentação" : heroi.apresentacao(),
        "Inventário" : heroi.invetario
    }
    

    heroi_json = json.dumps(heroi_dict, ensure_ascii=False)
    return heroi_json
    


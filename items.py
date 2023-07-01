

import random


itens_lv_1_15 = {
    "Pena de Corvo": 1,
    "Pedra Preciosa Comum": 2,
    "Poção de Cura Leve": 3,
    "Flecha de Madeira": 4,
    "Pão Fresco": 5,
    "Couro de Lobo": 6,
    "Chave Enferrujada": 7,
    "Pedra de Amolar": 8,
    "Tocha Apagada": 9,
    "Corda Gasta": 10,
    "Adaga de Bronze": 11,
    "Pequena Bolsa de Moedas": 12,
}

itens_lv_15_25 = {
    "Colar de Contas Coloridas": 13,
    "Mapa Rasgado": 14,
    "Maçã Madura": 15,
    "Arco de Madeira": 16,
    "Saco de Dormir": 17,
    "Poção de Resistência ao Fogo": 18,
    "Anel de Latão": 19,
    "Espada Curta de Ferro": 20,
    "Flecha de Prata": 21,
    "Capa de Lã": 22,
    "Flauta de Madeira": 23,
    "Máscara de Carnaval": 24,
    "Medalha de Participação": 25,
    "Livro de Feitiços Vazio": 26,
    "Pergaminho Enigmático": 27,
    "Elmo de Couro": 28,
    "Bracelete de Prata": 29,
    "Elixir de Força": 30,
    "Pedra de Fogo": 31,
    "Vara de Pescar": 32,
    "Mochila Pequena": 33,
    "Estrela de Prata": 34,
    "Pequeno Sino de Bronze": 35,
    "Antídoto Universal": 36,
    "Garrafa de Vinho Meio Cheia": 37,
    
}

itens_lv_25_35 = {
    "Pedra de Trovão": 38,
    "Broche de Penas": 39,
    "Luvas de Couro": 40,
    "Óculos de Leitura": 41,
    "Espelho de Bolso": 42,
    "Martelo de Ferreiro": 43,
    "Chave Dourada": 44,
    "Amuleto de Proteção": 45,
    "Poção de Invisibilidade": 46,
    "Pão de Mel": 47,
    "Lágrima de Unicórnio": 48,
    "Flautim": 49,
    "Varinha de Salgueiro": 50,
    "Mapa do Tesouro": 51,
    "Bracelete de Jade": 52,
    "Vara de Condão": 53,
    "Cinto de Couro": 54,
    "Anel de Rubi": 55,
    "Pena de Pavão": 56,
    "Esfera de Cristal": 57,
    "Livro de Histórias Antigas": 58,
    "Anel de Ouro": 59,
    "Poção de Velocidade": 60,
    "Cajado Mágico": 61,
    "Botas de Couro": 62,
    "Flor Encantada": 63,
    "Mapa das Estrelas": 64,
    "Cristal de Gelo": 65,
    "Elmo de Ferro": 66,
}

itens_lv_35_55 = {
    "Elmo de Ferro": 66,
    "Colar de Pérolas": 67,
    "Poção de Curar Ferimentos Graves": 68,
    "Orbe de Energia": 69,
    "Anel de Safira": 70,
    "Chave de Pedra": 71,
    "Luvas de Seda": 72,
    "Pergaminho de Invocação": 73,
    "Estátua Antiga": 74,
    "Flauta de Ouro": 75,
    "Tomo de Sabedoria": 76,
    "Anel do Poder": 77,
    "Cajado do Feiticeiro": 78,
    "Mapa do Labirinto": 79,
    "Cristal do Vento": 80,
    "Elmo do Herói": 81,
}

itens_lv_55_67 = {
     "Colar de Opalas": 82,
    "Poção de Invisibilidade Permanente": 83,
    "Escudo de Ferro": 84,
    "Flauta de Prata": 85,
    "Máscara Ritualística": 86,
    "Anel de Diamante": 87,
    "Capa Encantada": 88,
    "Cristal de Fogo": 89,
    "Diário Mágico": 90,
    "Penacho de Fênix": 91,
    "Bússola Mágica": 92,
    "Elixir da Vida": 93,
    "Escaravelho Dourado": 94,
    "Bastão do Feiticeiro": 95,
    "Botas Voadoras": 96,
    "Bracelete Encantado": 97,
    "Colar de Âmbar": 98,
    "Caldeirão de Prata": 99,
    "Mapa Dimensional": 100,
    "Globo de Cristal": 101,
    "Lira Encantada": 102,
    "Espada Mágica": 103,
    "Escudo Sagrado": 104,
    "Anel do Destino": 105,
}

itens_lv_67_78 = {
    "Coroa de Rubi": 106,
    "Pedra da Lua": 107,
    "Vestido de Seda": 108,
    "Orbe do Tempo": 109,
    "Poção de Cura Suprema": 110,
    "Arco Celestial": 111,
    "Saco de Moedas de Platina": 112,
    "Amuleto do Poder": 113,
    "Varinha de Ébano": 114,
    "Mapa Ancestral": 115,
    "Medalhão Encantado": 116,
    "Colar de Esmeraldas": 117,
    "Pedra do Sol": 118,
    "Cetro Real": 119,
    "Escudo Divino": 120,
    "Coroa do Rei": 121,
    "Chave do Reino": 122,
}

itens_lv_78_85 = {
    "Livro das Profecias": 123,
    "Bússola do Navegador": 124,
    "Ampulheta do Tempo": 125,
    "Elixir da Eternidade": 126,
    "Pedra da Ressurreição": 127,
    "Armadura Dourada": 128,
    "Cajado Divino": 129,
    "Lança Celestial": 130,
    "Orbe da Sabedoria": 131,
    "Coroa de Diamante": 132,
    "Espada Lendária": 133,
    "Colar do Dragão": 134,
    "Cristal do Infinito": 135,
    "Manto das Sombras": 136,
    
}

itens_lv_85_99 = {
    "Escudo do Herói": 137,
    "Anel da Imortalidade": 138,
    "Chave Mágica": 139,
    "Tomo dos Antigos": 140,
    "Pérola Negra": 141,
    "Coroa do Destino": 142,
    "Cajado do Arcanjo": 143,
    "Lança Divina": 144,
    "Elmo do Conquistador": 145,
    "Orbe do Universo": 146,
    "Anel da Onisciência": 147,
    "Colar da Harmonia": 148,
    "Espada Excalibur": 149,
    "Trono do Rei": 150,
    "Espelho da Ilusão": 151,
    "Botas da Velocidade": 152,
    "Luvas do Trovão": 153,
    "Capa da Invisibilidade": 154,
    "Anel da Proteção": 155,
    "Amuleto da Sabedoria": 156,
    "Arco do Destino": 157,
    "Elmo do Herói": 158   
}



def gerar_inventario(nivel):
    
    inventario = []
    numero_aletorio = random.randint(3,12)
    
    for _ in range(numero_aletorio):

        if nivel <= 15:
            item = random.choice(list(itens_lv_1_15.keys()))
        elif nivel <= 25:
            item = random.choice(list(itens_lv_15_25.keys()))
        elif nivel <= 35:
            item = random.choice(list(itens_lv_25_35.keys()))
        elif nivel <= 55:
            item = random.choice(list(itens_lv_35_55.keys()))
        elif nivel <= 67:
            item = random.choice(list(itens_lv_55_67.keys()))
        elif nivel <= 78:
            item = random.choice(list(itens_lv_67_78.keys()))
        elif nivel <= 85:
            item = random.choice(list(itens_lv_78_85.keys()))
        else:
            item = random.choice(list(itens_lv_85_99.keys()))
        
        inventario.append(item)
    
    return inventario

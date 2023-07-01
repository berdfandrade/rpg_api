# RPG api

Esta API em Python, utilizando o framework Flask, é responsável por gerar heróis de RPG com níveis, status e nomes gerados aleatoriamente. Os heróis podem ter gênero masculino, feminino ou gênero neutro, e cada um possui um inventário customizado correspondente ao seu nível atual.

Além disso, a API também é capaz de gerar monstros com níveis aleatórios, assim como os heróis, variando de 1 a 99. Os monstros possuem nomes gerados aleatoriamente, temperamento, e status de força e defesa.

## Endpoints

A API possui os seguintes endpoints:

- `GET /heroi`: Retorna um herói aleatório com seu nome, gênero, nível e status de força e defesa. O inventário do herói é customizado de acordo com o seu nível.

- `GET /monstro`: Retorna um monstro aleatório com seu nome, temperamento, nível e status de força e defesa.

## Exemplo de resposta

### Herói:

```json
GET /heroi

{
  "Nome": "Okirio",
  "Alcunha": "Poderoso",
  "Apresentação": "Okirio, o Poderoso",
  "Ataque": 2850,
  "Defesa": 1900,
  "Gênero": "Masculino",
  "HP": 9500,
  "Inventário": [
    "Capa da Invisibilidade",
    "Trono do Rei",
    "Espelho da Ilusão",
    "Anel da Imortalidade",
    "Elmo do Conquistador",
    "Amuleto da Sabedoria",
    "Anel da Imortalidade",
    "Elmo do Conquistador",
    "Trono do Rei",
    "Tomo dos Antigos"
  ],
  "Level": 95,
  "Stamina": 4750,
  "Temperamento": "Defensivo"
}
```

### Monstro:

```json
GET /monstro

{
  "Nome": "Putuyi",
  "Espécie": "Elemental",
  "Ataque": 2910,
  "Defesa": 1940,
  "HP": 9700,
  "Level": 97,
  "Stamina": 4850,
  "Temperamento": "Feroz"
}
```

## Contribuindo

Se você quiser contribuir para este projeto, fique à vontade para enviar pull requests ou abrir issues relatando problemas ou sugestões.

Espero que isso ajude a descrever sua API de geração de heróis de RPG! Lembre-se de personalizar e adicionar informações adicionais conforme necessário.

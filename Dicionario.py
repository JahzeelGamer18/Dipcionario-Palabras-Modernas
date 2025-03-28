import random

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    print({word}, {meme_dict[word]})
else:
    print("Lo siento, no conozco el significado de esta palabra.")

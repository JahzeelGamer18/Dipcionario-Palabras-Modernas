import discord, random, os
from discord.ext import commands
from nosee import gen_contenedores, gen_mision, gen_tips, gen_estado_ambiente, gen_eventos

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def contenedor(ctx):
    '''Te dice como se usan los contenedores'''
    await ctx.send(gen_contenedores())  
 
@bot.command()
async def misio(ctx):
    '''Te propone una mision'''
    await ctx.send(gen_mision())  

@bot.command()
async def tips(ctx):
    '''Te Muestra tips'''
    await ctx.send(gen_tips())  

@bot.command()
async def estado(ctx):
    '''Te da noticias de como se encuentra el medio ambiente'''
    await ctx.send(gen_estado_ambiente())  

@bot.command()
async def eventos(ctx):
    '''Te muesta los eventos que se generan en tu comunidad'''
    await ctx.send(gen_eventos())  

bot.run("Tu codigo aqui")










# aqui ya se divide lo que va en el bot loci




import random
import requests

def gen_contenedores():
    contenedores = [
        "♻️ ¿Dónde tiro una botella de vidrio rota? ✅ Contenedor verde (vidrio). ❌ No mezcles con cerámica o espejos.",
        "🧴 Envase de plástico limpio: Contenedor amarillo.",
        "📦 Cajas de pizza: parte limpia al contenedor azul (papel), parte manchada al gris (rechazo).",
        "🥡 Unicel (poliestireno expandido): contenedor gris (rechazo).",
        "📰 Papel mojado o sucio: contenedor gris. Solo papel limpio va al azul."
    ]
    return random.choice(contenedores)



def gen_mision():
    mision=[
        "🌱 Tu misión de hoy: 🚲 Usa transporte público o bicicleta al menos una vez. ¿Aceptas el reto? ✅",

        "🌻 Hoy planta una semilla o cuida una planta en casa.",

        "🚿 Reto exprés: Dúchate en menos de 5 minutos.",

        "🛍️ Lleva tu bolsa reutilizable al supermercado.",

        "📱 Desconéctate 1 hora y haz algo por la naturaleza.",

        "♻️ Separa tu basura correctamente hoy."

    ]
    return random.choice(mision)

def gen_tips():
    tips = [
        "💧 Cierra el grifo mientras te cepillas los dientes. Ahorras hasta 10 litros por minuto.",
        "🍽️ Evita el delivery con empaques plásticos: Cocina en casa o lleva tu recipiente.",
        "🧽 Usa vinagre y bicarbonato para limpiar: más natural y menos contaminante.",
        "🏠 Apaga las luces si no estás en la habitación.",
        "📦 Reutiliza cajas y bolsas para almacenar cosas en casa.",
        "🌅 Aprovecha la luz solar: sube las cortinas y evita encender luces innecesarias."
    ]
    return random.choice(tips)



def gen_estado_ambiente():
    estado = [
        "🏙️ Aire en tu zona: Bueno 🌿 | UV: Moderado | Residuos plásticos: Estables.",
        "🌬️ Calidad del aire: Regular PM2.5 alto. Usa mascarilla si haces ejercicio.",
        "🌫️ Contaminación atmosférica alta hoy (PM10 elevado). Evita actividades al aire libre.",
        "🌧️ Lluvia ácida reportada en zonas industriales. Cuida tus plantas y techos.",
        "☀️ Radiación UV muy alta Usa protector solar y evita exposición directa al sol."
    ]
    return random.choice(estado)


def gen_eventos():
    eventos = [
        "🧹 Limpieza de playa  Domingo 10 AM  Playa Norte.",
        "🌱 Taller de compostaje  Miércoles 17hs  EcoCentro.",
        "🌾 Feria del Trueque  Sábado 10 AM  Parque Central.",
        "🐝 Taller de huertos urbanos y polinizadores  Martes 6 PM.",
        "🍃 Caminata ecológica  Domingo 8 AM  Reserva Natural El Roble.",
        "🌎 Cine verde al aire libre  Jueves 8 PM  Plaza del Pueblo."
    ]
    return random.choice(eventos)


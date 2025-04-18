import discord
from bot_logic import gen_pass, gen_emodji, flip_coin, get_meme, get_advice, love_meter
from discord.ext import commands


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("goodBye")

@bot.command()
async def password(ctx, longitud: int):
    await ctx.send(gen_pass(longitud))

@bot.command()
async def emodji(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def meme(ctx):
    await ctx.send(get_meme())  

@bot.command()
async def advice(ctx):
    await ctx.send(get_advice())

@bot.command()
async def love(ctx):
    await ctx.send(love_meter())
   
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def bot_cool(ctx):
    await ctx.send('siii, el bot es geniall😎😎')

bot.command()
async def help(ctx):
    await ctx.send("/hello,   /bye,    /password,    /emodji,     /flip,   /meme,   /advice,    /love,    /add,    /bot_cool")

bot.run("")






#Aqui va el bot logic


import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Escudo"
    

def get_meme():
    memes = [
        "Cuando intento programar sin errores... y tengo 20 🐛.",
        "¡Ese momento en que funciona y no sabes por qué! 😅",
        "Yo después de 5 minutos de estudio: ya merezco vacaciones.",
        "Procrastinar es mi superpoder 🦸‍♂️",
            ]
    return random.choice(memes)

def get_advice():
    advice = [
        "Nunca confíes en un pato con sombrero. 🦆🎩",
        "Si la vida te da limones, pide sal y tequila. 🍋",
        "No reinicies tu PC con el pie... otra vez.",
        "Tu futuro depende de lo que hagas... después de esta siesta.",
    ]
    return random.choice(advice)

def love_meter():
    percent = random.randint(0, 100)
    return f"❤️ Amor detectado: {percent}%"

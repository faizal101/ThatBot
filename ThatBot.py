import discord, random, os, logging
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
grilinfo = ['__Ena Komiya from Just Because!__',
            '__Mizuki Usami from Kono Bijutsubu ni wa Mondai ga Aru!__',
            '__Senju Muramasa from Eromanga-Sensei__',
            '__Vigne from Gabriel Dropout__',
            '__Nishikino Maki from Love Live__',
            '__Kurisu Makise from Steins;Gate__',
            '__Ai Nanasaki from Amagami SS__',
            '__Shirayuki from Akagami no Shirayukihime__',
            '__Saya Endou from Dagashi Kashi__',
            '__Yukari Akiyama from Girls und Panzer__',
            '__Zero from Zero kara Hajimeru Mahou no Sho__',
            '__Rin Shibuya from THE iDOLM@STER__',
            '__Charlotte Dunois from Infinite Stratos__',
            '__Megumin from Kono Subarashii Sekai ni Shukufuku wo!__']

logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(type=2, name='kradness & reol'))  # type 0 = default, 1= streaming, 2=listening to 3= watching


@bot.command()
async def say(ctx, *, message: str):
    """I say what you'll say"""
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    """A simple ping command"""
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content='Pong! That took {}ms!'.format(1000*diff.total_seconds()))

@bot.command()
async def coin(ctx):
    """A simple coin flip"""
    flip = random.choice(['heads', 'tails'])
    await ctx.send(flip)

@bot.command()
async def smug(ctx):
    """Posts a random smug pic"""
    with open('pathname.txt') as f:
        lines = f.readlines()
        path = (lines[4]).split('\n')[0]
    file = str(random.randint(1, 71))
    smug = path + 'smug/' + file + '.png'
    await ctx.send(file=discord.File(smug))

@bot.command()
async def bestgril(ctx):
    """Posts a random picture of the best girl from an anime"""
    with open('pathname.txt') as f:
        lines = f.readlines()
        path = (lines[4]).split('\n')[0]
    gril = (random.randint(0, len(grilinfo) - 1))
    bestgril = path + 'bestgril/' + str(gril + 1) + '.jpg'  # added 1 because list starts at 0 and images starts at 1
    info = grilinfo[gril]
    await ctx.send(file=discord.File(bestgril), content=info)

@bot.command()
async def headpat(ctx):
    """Posts a random picture of a qt anime gril getting a headpat"""
    with open('pathname.txt') as f:
        lines = f.readlines()
        headpat_path = (lines[7]).split('\n')[0]
    headpats = random.choice(os.listdir(headpat_path))
    file = headpat_path + headpats
    await ctx.send(file=discord.File(file))

@bot.command()
async def yay(ctx):
    """owo vs omo vs umu vs uwu, winner is +o+"""
    with open('pathname.txt') as f:
        lines = f.readlines()
        path = (lines[4]).split('\n')[0]
    file = str(random.randint(0, 25))
    yahay = path + 'yay/' + '60322965_' + file + '.png'
    await ctx.send(file=discord.File(yahay))

@bot.command()
async def fight(ctx, user: discord.Member):
    """Fight a user on the server"""
    from stringChoice import fight
    await ctx.send('{} is fighting {}{}'.format(ctx.author.mention, user.mention, fight()))

@bot.command()
async def info(ctx):
    """Information about this bot"""
    servercount = len(bot.guilds)
    emb = (discord.Embed(title='{}'.format(bot.user), description=
    'A bot made for fun by Kuuhaku#4503 \nCoded in discord.py rewrite'
    '\nThis bot is in: {} servers'.format(servercount), colour=0xEC40DF))
    await ctx.send(embed=emb)

@bot.command(name='8ball')
async def _8ball(ctx, *, message: str):
    """The magic ball knows the answer to everything"""
    from stringChoice import ball
    user = str(ctx.author).split('#')[0]
    await ctx.send('{} asked: {} \n8ball: {}'.format(user, message, ball()))


bot.run('')  # token goes here

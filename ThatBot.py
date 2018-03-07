import discord, random, os, logging
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
path = 'path'  # default path goes here
headpat_path = 'headpats'  # headpats folder path goes here
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
strings = [', but instead slipped on some jam and fell right into a conveniently placed hole.',
         ' with a transformer.', ', but creates a black hole and gets sucked in.',
         ' with poutine.', ', but they slipped on a banana peel.',
         ' and in the end, the only victor was the coffin maker.',
         ', and what a fight it is! Whoa mama!', ', with two thousand blades!',
         ', but fell into a conveniently placed manhole!',
         ', but they tripped over a rock and fell in the ocean.',
         ', but they hurt themselves in confusion.', '. HADOUKEN!', ' with a pillow.',
         ' with a large fish.', ', but they stumbled over their shoelaces.', ', but they missed.',
         ' with a burnt piece of toast.', ', but it wasn\'t very effective.',
           ' and it was super effective!', ', but nothing happened.', ', while shouting out a move as if they\'re a main character from an anime.', ', but gave up halfway.']

logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(type=2, name='kradness & reol'))  # type 0 = default, 1= streaming, 2=listening to 3= watching


@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def coin(ctx):
    flip = random.choice(['heads', 'tails'])
    await ctx.send(flip)

@bot.command()
async def smug(ctx):
    file = str(random.randint(1, 71))
    smug = path + 'smug/' + file + '.png'
    await ctx.send(file=discord.File(smug))

@bot.command()
async def bestgril(ctx):
    gril = (random.randint(0, len(grilinfo) - 1))
    bestgril = path + 'bestgril/' + str(gril + 1) + '.jpg'  # added 1 because list starts at 0 and images starts at 1
    info = grilinfo[gril]
    await ctx.send(file=discord.File(bestgril), content=info)

@bot.command()
async def headpat(ctx):
    headpat = random.choice(os.listdir(headpat_path))
    file = headpat_path + headpat
    await ctx.send(file=discord.File(file))

@bot.command()
async def yay(ctx):
    file = str(random.randint(0, 25))
    yahay = path + 'yay/' + '60322965_' + file + '.png'
    await ctx.send(file=discord.File(yahay))

@bot.command()
async def fight(ctx, user: discord.Member):
    string = random.choice(strings)
    await ctx.send('{} is fighting {}{}'.format(ctx.author.mention, user.mention, string))

@bot.command()
async def info(ctx):
    servercount = len(bot.guilds)
    emb = (discord.Embed(title='{}'.format(bot.user), description=
    'A bot made for fun by Kuuhaku#4503 \nCoded in discord.py rewrite'
    '\nThis bot is in: {} servers'.format(servercount), colour=0xEC40DF))
    await ctx.send(embed=emb)

@bot.command()
async def commands(ctx):
    emb = (discord.Embed(title="List of commands: ", description=
        '.coin -Flips a coin \n.smug -Posts a smug '
        '\n.yay –umu vs uwu vs owo. winner: +o+  \n.commands \-Shows this list '
        '\n.info –Shows information about the bot \n. –Invite link to add this bot to your server if you want I guess '
        '\n.bestgril –Best gril for you may/may not be the same as mine \n.headpat –The world needs more headpats'
        '\n.fight –Fight with someone in this server', colour=0xEC40DF))
    await ctx.send(embed=emb)


bot.run('')  # token goes here

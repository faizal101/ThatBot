import discord, random, os, logging
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
grilinfo = ['Ena Komiya from Just Because!',
            'Mizuki Usami from Kono Bijutsubu ni wa Mondai ga Aru!',
            'Senju Muramasa from Eromanga-Sensei',
            'Vigne from Gabriel Dropout',
            'Nishikino Maki from Love Live',
            'Kurisu Makise from Steins;Gate',
            'Ai Nanasaki from Amagami SS',
            'Shirayuki from Akagami no Shirayukihime',
            'Saya Endou from Dagashi Kashi',
            'Yukari Akiyama from Girls und Panzer',
            'Zero from Zero kara Hajimeru Mahou no Sho',
            'Rin Shibuya from THE iDOLM@STER',
            'Charlotte Dunois from Infinite Stratos',
            'Megumin from Kono Subarashii Sekai ni Shukufuku wo!']

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

@bot.command(aliases=['flip'])
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
    await ctx.send(file=discord.File(bestgril), content='__{}__'.format(info))

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

@bot.command(aliases=['botinfo', 'botstats'])
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

@bot.command()
async def invite(ctx):
    """Invite this bot to one of your servers thank"""
    invite = 'https://discordapp.com/api/oauth2/authorize?client_id=284399078165708802&permissions=1141230657&scope=bot'
    await ctx.send('Invite me to your server! Invite link: {}'.format(invite))

@bot.command(aliases=['db', 'dan'])
async def danbooru(ctx, *, search: str):
    from pybooru import Danbooru, exceptions

    client = Danbooru('danbooru')
    try:
        posts = client.post_list(tags=search, random=True, limit=1)
    except exceptions.PybooruHTTPError:
        await ctx.send('Danbooru only allows you to search with 2 tags. Consider donating $20 if you want to search with more tags')
    url = 'https://danbooru.donmai.us/posts/'

    for post in posts:
        id = str(post['id'])
        dblink = url + id
        if str(post['file_url']).startswith('/data/'):
            file = 'https://donmai.us{}'.format(post['file_url'])
        else:
            file = post['file_url']
            if post['rating'] == "s":
                rating = 'Safe'
            elif post['rating'] == 'q':
                rating = 'Questionable'
            elif post['rating'] == 'e':
                rating = 'Explicit'
        score = post['score']
        source = post['source']

        emb = discord.Embed(
            title='Click here to view in your browser',
            url=dblink,
            colour=0xEC40DF,
            description='__Post ID: {}__'.format(id)
        )
        emb.set_image(url=file)
        emb.set_author(name='Danbooru', url='http://danbooru.donmai.us',
                       icon_url='https://qt-anime-grils.is-serious.business/555270.png')
        emb.add_field(name='Rating: ', value=rating, inline=True)
        emb.add_field(name='Score: ', value=score, inline=True)
        emb.add_field(name='Source: ', value='[Click Here]({})'.format(source), inline=False)

        await ctx.send(embed=emb)


bot.run('')  # token goes here

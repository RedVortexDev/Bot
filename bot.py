import discord
from discord.ext import commands

# Arguments for the bot to be online
TOKEN = ''
BOT_PREFIX = "'"

# Taking the argument BOT_PREFIX and puts it here
client = commands.Bot(command_prefix=BOT_PREFIX)


# Bot setup.
@client.event
async def on_ready():
    # Prints 'Bot Is Online' when bot is online and ready to use.
    print('Bot Is Online.')


# If typing a wrong command, if it will not be here it will throw an error in the console, and you don't want this.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Didn't find a command with that name, type `{BOT_PREFIX}help` for a list of commands. \u274c")


# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


# Test Command
@client.command()
async def test(ctx):
    await ctx.send("testing")
    print("test")


# Good Morning & Good Night
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Good Morning
    if message.content.lower().__contains__("good morning"):
        await message.channel.send(f"Good morning to you {message.author.mention}!")

    # Good Night
    if message.content.lower().__contains__("good night"):
        await message.channel.send(f"Good night {message.author.mention}!")

    # DO NOT TOUCH!
    await client.process_commands(message)  # This passes the message onto the commands to process after this


# Taking the argument TOKEN and puts it here
client.run(TOKEN)

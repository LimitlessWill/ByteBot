# importing OS to deal with future files at least ...
import os

# Importing discord library
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# A decorator function to start
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!\nHello World")

# A decorator function to read message the send response
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("tree "):
        msg = f"I\'m currently under-development , <@{message.author.id}> \n please try again later \n Your message content was \n ```{message.content}```\n"  
        await message.reply(msg)
        emoji = ["👋","👉","👈"]
        await message.add_reaction(emoji[0])
        await message.add_reaction(emoji[1])
        await message.add_reaction(emoji[2])

    if message.content.lower() == "tree":
        gds = [x.name for x in client.guilds]
        await message.reply( "\n".join(gds), mention_author=False )
        emoji = ["👋","👉","👈"]
        await message.add_reaction(emoji[0])
        await message.add_reaction(emoji[1])
        await message.add_reaction(emoji[2])


# Actual start logging-in
client.run(TOKEN)

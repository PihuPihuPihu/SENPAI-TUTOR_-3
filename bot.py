import os
import discord
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True  # To read messages
bot = discord.Client(intents=intents)

# Bot startup
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Reply to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore self
        return

    # Simple test command
    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {message.author.mention}! ❤️')

    # Husbando study command
    if message.content.startswith('!study'):
        await message.channel.send(
            f"{message.author.mention}, your husbando is here to help! "
            "Let’s focus for 25 minutes! 🎓✨"
        )

# Run the bot
bot.run(TOKEN)
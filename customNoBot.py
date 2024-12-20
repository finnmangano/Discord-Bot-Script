import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

print("Token loaded:", TOKEN)
if not TOKEN:
    raise ValueError("No token found!")

responses = {
    "hi": "Hello there! How’s it going?",
    "hello": "Hey! What’s up?",
    "hey": "Heyyy! What’s the vibe?",
    "howdy": "Howdy partner! Ready for some fun?",
    "what's up": "Not much, just chilling like a villain.",
    "yo": "Yo yo! What’s poppin’?",
    "good morning": "Good morning, sunshine! Ready to take on the day?",
    "good night": "Good night! Sleep tight, don’t let the bedbugs bite!",
    "thanks": "You’re welcome! I’m here all week, folks.",
    "thank you": "No problem! Happy to help.",
    "please": "Please? Is that the magic word?",
    "sorry": "No worries, we’ve all been there.",
    "goodbye": "Goodbye! Hope you have a fantastic day ahead!",
    "bye": "See ya later, alligator!",
    "what": "What? I’m confused… but in a good way!",
    "help": "Help? You’ve come to the right place! What do you need?",
    "how are you": "I’m doing fantastic! How about you?",
}

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 
intents.dm_messages = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!!!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"Message received: {message.content}")

    if isinstance(message.channel, discord.TextChannel):
        for keyword, response in responses.items():
            if keyword in message.content.lower():
                await message.channel.send(response)
                break  

    await bot.process_commands(message)

bot.run(TOKEN)

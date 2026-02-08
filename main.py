import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_MESSAGE = (
    "☁️🎉 Hey {member_name}, welcome to **Cloudline**! 🚀✨\n\n"
    "Taguchi Junnosuke here! 💖 Thank you for joining our cloud-filled community! 🌤️\n"
    "Hang out, share art, chat, and enjoy the vibes 🌈🎶\n"
    "Cloudline is your sky playground — relax and have fun ☁️✨"
)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(WELCOME_MESSAGE.format(member_name=member.display_name))

@bot.event
async def on_message(message):
    forbidden_words = ["loli", "shota", "porn"]
    
    if any(word in message.content.lower() for word in forbidden_words):
        await message.channel.send(
            f"{message.author.mention}, please avoid forbidden words 🚫"
        )

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))

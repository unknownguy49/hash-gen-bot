import discord
import hashlib
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ Logged in as {client.user}")

@tree.command(name="hash", description="Generate hash of a text")
async def hash_command(interaction: discord.Interaction, text: str, algorithm: str = "sha256"):
    try:
        algo = getattr(hashlib, algorithm.lower())
        result = algo(text.encode()).hexdigest()
        await interaction.response.send_message(
            f"**{algorithm.upper()}** of `{text}`:\n```{result}```"
        )
    except AttributeError:
        await interaction.response.send_message("❌ Unsupported algorithm")

client.run(os.getenv("BOT_TOKEN"))

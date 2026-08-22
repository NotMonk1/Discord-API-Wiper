"""
Run this ONCE to wipe all registered slash commands from Discord's API.
After it finishes, re-run your bot normally to re-register only your new commands.

Usage:
    python Discord_API_Wipe.py              # clears global commands
    python Discord_API_Wipe.py [GUILD ID]   # also clears guild-specific commands
"""

import asyncio
import sys
import discord

GUILD_ID = int(sys.argv[1]) if len(sys.argv) > 1 else None


async def clear_commands(token: str):
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)
    tree = discord.app_commands.CommandTree(bot)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}\n")

        # Global commands 
        tree.clear_commands(guild=None)
        await tree.sync()
        print("Cleared global slash commands")

        input("PRESS ENTER TO EXIT")

        # Guild-specific commands (optional)
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            tree.clear_commands(guild=guild)
            await tree.sync(guild=guild)
            print(f"Cleared guild commands for guild ID {GUILD_ID}")

            input("PRESS ENTER TO EXIT")

        await bot.close()

    await bot.start(token)


if __name__ == "__main__":
    print ("This code does NOT log your bot token. If you dont trust it use DNSpy or a code editor")
    print ("Discord API Wiper By NotMonk (@notmonk.idi0t on discord)")
    token = input("Enter your bot token: ").strip()
    if not token:
        raise ValueError("No token provided.")
    asyncio.run(clear_commands(token))

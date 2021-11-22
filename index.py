import discord
from discord.ext import commands
import os

Client = commands.Bot(command_prefix="*")

@Client.event
async def on_ready():
    print("Online")

@Client.command(aliasses=['A'])
@commands.has_permissions(manage_messages = True)
async def Clear(ctx,amount=2):
  await ctx.channel.purge(limit = amount)

Client.run(os.environ['token'])
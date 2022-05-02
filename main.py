import os
import keep_alive

from discord.ext import commands
from dotenv import load_dotenv
from replit import db
from orkify import orkify

#----------Setup----------

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

def get_prefix(bot, message):
  try:
    return db[message.guild.id]
  except:
    return "!"

bot = commands.Bot(command_prefix=get_prefix, help_command=None)

#----------Translation----------

@bot.command(name="orkify")
async def translate(ctx, *, message=None):
    if message == None:
      channel = bot.get_channel(ctx.channel.id)
      last_messages = await channel.history(limit=2).flatten()
      prev_message = last_messages[1].content
      await ctx.send(orkify(prev_message))
    else:
      await ctx.send(orkify(message))

    db["count"] = db["count"] + 1

#----------Prefixes----------

@bot.event
async def on_guild_join(guild):
  db[guild.id] = "!"

@bot.event
async def on_guild_remove(guild):
  del db[guild.id]

@bot.command(name="setprefix")
@commands.has_permissions(manage_guild=True)
async def setprefix(ctx, *, prefix):
  db[ctx.guild.id] = prefix
  await ctx.send(f"PREFIX CHANGED TA: {prefix}")

@setprefix.error
async def setprefix_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("OI, YA NEED DA \"Manage Server\" PERMISSION TA DO DAT!")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("ARGUMENT REQUIRED.  TRY AGAIN.")

#----------Count----------

@bot.command(name="count")
async def get_count(ctx):
  num = db["count"]
  await ctx.send(f"{num} MESSAGEZ 'AVE BIN TRANSLATED.")

#----------Vote----------

@bot.command(name="vote")
async def vote(ctx):
  await ctx.send("YA KAN VOTE FA DA BOT 'ERE: https://top.gg/bot/783164552044478474/vote")

#----------Help----------

@bot.command(name="help")
async def help(ctx, command=None):
  prefix = db[ctx.guild.id]
  await ctx.send(f"""```
Commands:

{prefix}orkify <text>
Translates given text into 40k Ork speech.  Can be used without an argument to translate the last message sent.

{prefix}setprefix <prefix>
Sets a new prefix.  Only people with the "Manage Server" permission can do this.

{prefix}count
Gets a count of how many messages have been translated.

{prefix}vote
Gets a link to the bot's voting page.
    
{prefix}help
Gets a list of each command and its respective purpose.```""")

#----------Run-----------

keep_alive.keep_alive()
bot.run(TOKEN)
from discord import Embed, Color, Game
from discord.ext.commands import Bot, is_owner, CommandNotFound
from discord.utils import get
import os

bot = Bot(command_prefix="?", activity=Game(name="with elements"))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(hidden=True)
@is_owner()
async def unload(ctx, *, module: str):
    """
    Unloads a module.
    """
    bot.unload_extension(module)
    e = Embed(title="Unloaded")
    e.add_field(name="Module", value=module)
    e.color = Color.from_rgb(67, 180, 129)
    await ctx.send("", embed=e)


@bot.command(hidden=True)
@is_owner()
async def load(ctx, *, module: str):
    """
    Loads a module.
    """
    bot.load_extension(module)
    e = Embed(title="Loaded")
    e.add_field(name="Module", value=module)
    e.color = Color.from_rgb(67, 180, 129)
    await ctx.send("", embed=e)


@bot.command(hidden=True)
@is_owner()
async def reload(ctx, *, module: str):
    """
    Reloads a module
    """
    bot.unload_extension(module)
    bot.load_extension(module)
    e = Embed(title="Reloaded")
    e.add_field(name="Module", value=module)
    e.color = Color.from_rgb(67, 180, 129)
    await ctx.send("", embed=e)


@bot.command(name="eval", hidden=True)
@is_owner()
async def _eval(ctx, *, inp: str):
    """
    Evaluates code
    """
    try:
        e = Embed(title="Eval Successful")
        e.add_field(name="Input", value=f"```py\n{inp}\n```", inline=False)
        e.add_field(name="Output", value=f"```py\n{eval(inp)}\n```")
        e.color = Color.from_rgb(67, 180, 129)
        await ctx.send("", embed=e)
    except Exception as error:
        e = Embed(title="Eval Error")
        e.add_field(name="Input", value=f"```py\n{inp}\n```", inline=False)
        e.add_field(name="Error", value=f"```text\n{error}\n```", inline=False)
        e.color = Color.from_rgb(240, 73, 71)
        await ctx.send("", embed=e)


@bot.event
async def on_command_error(ctx, error):
    ignored = (CommandNotFound)
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        return
    e = Embed(title="Error")
    e.add_field(name="Error", value=f"```text\n{error}\n```", inline=False)
    e.color = Color.from_rgb(240, 73, 71)
    await ctx.send("", embed=e)


bot.load_extension("utilities")
bot.load_extension("science")
bot.load_extension("mathematics")
bot.run(os.environ["SCIBOT_TOKEN"])

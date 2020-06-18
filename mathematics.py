from discord.ext import commands
from discord import Embed, Color
from discord.utils import get
import sigfig


class Mathematics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["sf", "sfs"])
    async def sigfigs(self, ctx, number: float, figures: int):
        """
        Round a number to a specified number of significant figures
        """
        result = sigfig.round(number, sigfigs=figures)

        e = Embed(title="Rounding Result")
        e.add_field(name="Original Number", value=number, inline=True)
        e.add_field(name="Figures", value=figures, inline=True)
        e.add_field(name="Result", value=result, inline=False)
        e.add_field(name="Result (Scientific Notation)", value="{:e}".format(result))
        e.color = Color.dark_blue()
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Mathematics(bot))

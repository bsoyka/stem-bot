from discord.ext import commands
from discord import Embed, Color
from discord.utils import get
import json

with open("ptable/PeriodicTableJSON.json", "rb") as f:
    periodic_table = json.load(f)


class Science(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["e", "el", "elem"])
    async def element(self, ctx, element_input):
        """
        Get a specific element by atomic number, symbol, or name
        """
        element = [el for el in periodic_table["elements"] if element_input.lower() in (
            str(el["number"]), el["name"].lower(), el["symbol"].lower())][0]
        embed = Embed(
            title=element["name"], description=element["summary"])

        fields = ["number", "symbol", "category", "appearance", "atomic_mass", "phase", "density", "boil", "melt",
                  "valence_electrons", "shells", "named_by", "electron_configuration", "electron_affinity", "electronegativity_pauling"]
        for field in fields:
            display_name = field.replace("_", " ").title()
            if field == "valence_electrons":
                embed.add_field(name=display_name,
                                value=element["shells"][-1], inline=True)
            elif type(element[field]) == list:
                embed.add_field(name=display_name,
                                value=", ".join(map(str, element[field])), inline=True)
            elif element[field] == None:
                pass
            else:
                embed.add_field(name=display_name,
                                value=element[field], inline=True)

        embed.set_footer(text=f"Source: {element['source']}")
        embed.color = Color.dark_blue()

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Science(bot))

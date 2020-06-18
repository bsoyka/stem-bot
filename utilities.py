from discord.ext import commands
from discord import Embed, Color, Emoji
import wikipedia
import aiohttp
import asyncio


async def fetch_img(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        return await response.read()


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pong"])
    async def ping(self, ctx):
        """
        Check the bot's latency
        """
        e = Embed(title="Pong!")
        e.add_field(name=f"{self.bot.get_emoji(721097479508197479)} Latency",
                    value=f"{int(self.bot.latency * 1000)} ms")
        e.color = Color.dark_blue()
        await ctx.send("", embed=e)

    @commands.command(aliases=["wikipedia", "wp", "w"])
    async def wiki(self, ctx, *, search_term: str):
        """
        Get a summary from Wikipedia
        """
        wiki_page = wikipedia.page(search_term)
        e = Embed(title=wiki_page.title, description=wikipedia.summary(
            search_term, chars=2000), url=wiki_page.url)
        e.color = Color.dark_blue()
        await ctx.send("", embed=e)

    @commands.command()
    @commands.has_permissions(add_reactions=True, external_emojis=True, manage_emojis=True)
    @commands.bot_has_permissions(manage_emojis=True)
    async def steal(self, ctx):
        """
        Steal a custom emoji
        """
        e = Embed(title="Steal Command", description="React to this message with the emoji you'd like to steal within 60 seconds.")
        e.color = Color.dark_blue()
        statusmsg = await ctx.send(embed=e)

        def check(reaction, user):
            return user == ctx.author

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            e = Embed("Timed Out")
            e.color = Color.from_rgb(240, 73, 71)
            await statusmsg.edit(embed=e)
            return

        await statusmsg.clear_reactions()

        e = Embed(title="Stealing In Progress", description="This may take a few seconds...")
        e.color = Color.gold()
        await statusmsg.edit(embed=e)

        async with aiohttp.ClientSession() as session:
            img = await fetch_img(session, str(reaction.emoji.url))

        emoji = await ctx.guild.create_custom_emoji(name=reaction.emoji.name, image=img)

        e = Embed(title="Stole Emoji")
        e.add_field(name="Emoji", value=str(emoji))
        e.add_field(name="Name", value=emoji.name)
        e.color = Color.from_rgb(67, 180, 129)
        await statusmsg.edit(embed=e)


def setup(bot):
    bot.add_cog(Utilities(bot))

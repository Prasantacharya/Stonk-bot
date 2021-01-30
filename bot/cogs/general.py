import discord
from discord import Colour
from discord.ext import commands


REPO_TEXT = "GitHub"
REPO_URL = "https://github.com/RPITechTalks/BoilerplateDiscordBot"
CODE_LICENSE = "MIT License"


class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['about'])
    async def info(self, ctx):
        """
        Shows info about the bot
        """

        bot_name = bot.user.name

        embed = discord.Embed(
            title=f'About {bot_name}',
            description=self.bot.description,
            colour=Colour.blue()
        ).add_field(
            name='Contributing',
            value=f'Check out the source on [{REPO_TEXT}]({GITHUB_URL})',
            inline=False
        ).add_field(
            name='License',
            value=f'{bot_name} is released under the {CODE_LICENSE}',
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """
        Check latency
        """

        await ctx.send(f'**Pong!** Current ping is {self.bot.latency*1000:.1f} ms')


def setup(bot):
    bot.add_cog(GeneralCog(bot))

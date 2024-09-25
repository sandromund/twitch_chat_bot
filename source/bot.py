import logging

from twitchio.ext import commands
from twitchio.ext import routines

from source.base import Config


class Bot(commands.Bot):
    def __init__(self,
                 config: Config):
        super().__init__(
            token=config.demo.token,
            prefix="?",
            initial_channels=[config.demo.channel], )
        self.config = config

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        self.bot_attack.start()

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello {ctx.author.name}!")

    async def event_message(self, message):
        if message.echo:
            return
        m = message
        print(f"#{message.author.channel.name}-{message.author.name}({message.timestamp}): {message.content}")
        await self.handle_commands(message)

    @routines.routine(seconds=30.0, iterations=5)
    async def bot_attack(self):
        channel = self.get_channel(self.config.demo.channel)
        if channel:
            await channel.send('?attack')
        logging.error("Channel not found!")

"""
This module defines a custom Twitch bot that interacts with Twitch chat and an AI system.
The bot can respond to chat commands, interact with an AI module, and execute routines.
"""

import logging

from twitchio.ext import commands, routines

from source.ai import AI
from source.base import Config


class Bot(commands.Bot):
    """
    A custom Twitch bot that interacts with an AI and responds to chat commands.

    Attributes:
        config (Config): Configuration object with Twitch and AI settings.
        ai (A
    """

    def __init__(self, config: Config):
        """
        Initialize the bot with the given configuration.

        Args:
            config (Config): The configuration object containing Twitch and AI settings.
        """
        self.config = config
        super().__init__(
            token=self.config.twitch.token,
            prefix=self.config.twitch.prefix,
            initial_channels=[self.config.twitch.channel],
        )
        self.ai = AI(config=config.ai)

    async def event_ready(self):
        """
        Event handler triggered when the bot is ready and connected to Twitch.
        Prints bot information and starts the bot_attack routine.
        """
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        self.bot_attack.start()

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """
        Responds to the hello command with a greeting.

        Args:
            ctx (commands.Context): The context of the command.
        """
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def get(self, ctx: commands.Context):
        """
        Responds with the current AI personality.

        Args:
            ctx (commands.Context): The context of the command.
        """
        await ctx.send(self.ai.personality)

    @commands.command()
    async def help(self, ctx: commands.Context):
        """
        Sends a list of available commands.

        Args:
            ctx (commands.Context): The context of the command.
        """
        cmds = " ".join(
            [
                self.config.twitch.prefix + s
                for s in ["get", "set", "hello", "promt", "help"]
            ]
        )
        await ctx.send("Commands: " + cmds)

    @commands.command()
    async def promt(self, ctx: commands.Context):
        """
        Processes the user's input through the AI and sends the response.

        Args:
            ctx (commands.Context): The context of the command.
        """
        promt_text = str(ctx.message.content).replace(
            self.config.twitch.prefix + "promt ", ""
        )
        answer: str = self.ai.respond(prompt=promt_text)
        await ctx.send(answer[:500])

    @commands.command()
    async def set(self, ctx: commands.Context):
        """
        Sets the AI personality based on user input.

        Args:
            ctx (commands.Context): The context of the command.
        """
        self.ai.personality = str(ctx.message.content).replace(
            self.config.twitch.prefix + "set ", ""
        )

    async def event_message(self, message):
        """
        Event handler for incoming chat messages.
        Logs message details and processes any commands.

        Args:
            message: The incoming message from Twitch chat.
        """
        if message.echo:
            return
        logging.info(
            "#%s-%s(%s): %s",
            message.author.channel.name,
            message.author.name,
            message.timestamp,
            message.content,
        )
        await self.handle_commands(message)

    @routines.routine(seconds=30.0, iterations=5)
    async def bot_attack(self):
        """
        Routine that sends an attack command to the Twitch channel every 30 seconds.
        It runs for 5 iterations.

        Logs an error if the channel is not found.
        """
        channel = self.get_channel(self.config.twitch.channel)
        if channel:
            await channel.send("?attack")
        logging.error("Channel not found!")

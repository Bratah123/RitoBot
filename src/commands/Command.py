import discord
from discord import Color

from src.commands.CommandDecorator import command
from src.settings import Config


class Command:

    @staticmethod
    @command(
        cmd=["help", "commands"]
        # channel = ""
        # role = ""
        # so other examples for args
    )
    async def handle_help(client, txt_channel, author, msg)\
            -> "Show All Commands": # Standard Help Command to start it off
        reply = "Commands are prefixed with a {}\n\n".format(Config.PREFIX)

        cmds = [func for func in dir(Command) if callable(getattr(Command, func)) and not func.startswith("__")]
        for cmd in sorted(cmds):
            f = getattr(Command, cmd)
            annotations = f.__annotations__
            decorators = f.dec
            if "role" in decorators.keys():
                continue
            help_txt = annotations['return']
            cmd_txt = "/".join(decorators['cmd']) if isinstance(decorators['cmd'], list) else decorators['cmd']
            reply += "{} - {}\n".format(cmd_txt, help_txt)

        await txt_channel.send(reply)
        return True

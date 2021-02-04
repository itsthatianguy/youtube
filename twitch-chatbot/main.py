from twitchio.ext import commands
from twitchio.client import Client
import os


bot = commands.Bot(
    irc_token=os.environ['TWITCH_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    nick='incompetent_robot',
    prefix='!',
    initial_channels=['incompetent_ian'],
)


client = Client(
    client_id=os.environ['TWITCH_CLIENT_ID'],
    client_secret=os.environ['TWITCH_CLIENT_SECRET'],
)


@bot.event
async def event_message(ctx):
    print(ctx.author)
    print(ctx.content)
    await bot.handle_commands(ctx)


@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("this is a test response")


@bot.command(name='who')
async def get_chatters(ctx):
    chatters = await client.get_chatters('incompetent_ian')
    all_chatters = ' '.join(chatters.all)
    await ctx.send(f"In chat: {all_chatters}")


if __name__ == '__main__':
    bot.run()

import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
import os
import os

#import all of the cogs
from main_cog import main_cog
from music_cog import music_cog
TOKEN="OTAwMzM4MjU1MjQ4MTIxODg2.YW_3Vw.bW44n6RcbSokdO58XxaUAUOHgXk"
bot = commands.Bot(command_prefix='Z')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token

@bot.event
async def on_ready():
    print('Hello, I am your music bot {0.user}'
    .format(bot))
    generel_channel= bot.get_channel(882939306870714408) #897442493338124328

    await generel_channel.send('Yo! Wot bussin? GenZ here.Type Zhelp for further info.'
    .format(bot))
@bot.event
async def on_message(message):
    if message.content.startswith('Zgo'): # bot leave channel
        if (message.guild.voice_client): # If the bot is in a voice channel 
            await message.guild.voice_client.disconnect() # Leave the channel
            await message.channel.send('Peace out, brother.')
        else: # But if it isn't
            await message.channel.send("I'm not in a voice channel, shawty. Play something. Use Zhelp. It helps.")
    await bot.process_commands(message) # commands work properly
bot.run(TOKEN)
#bot.run(os.getenv("TOKEN"))

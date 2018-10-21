import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os

bot = discord.Client()
bot_prefix="nn@"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(str(len(bot.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!")
    await bot.change_presence(game=discord.Game(name='OnrcNN ile '))

@bot.command(pass_context=True)
async def onurcan(ctx) :
    await bot.say("Allah")

@bot.command(pass_context=True)
async def berkay(ctx) : 
    await bot.say("Yıkık bir orospu çoçu")
                                                
@bot.command(pass_context=True)
async def sarıl(ctx, member:discord.Member):
    urll = ["https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
            "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif" ,
           "https://78.media.tumblr.com/680b69563aceba3df48b4483d007bce3/tumblr_mxre7hEX4h1sc1kfto1_500.gif" ,
           "https://66.media.tumblr.com/18fdf4adcb5ad89f5469a91e860f80ba/tumblr_oltayyHynP1sy5k7wo1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name )
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def öp(ctx, member:discord.Member):
    url2 = ["https://acegif.com/wp-content/uploads/anime-kiss-m.gif" , 
            "https://i.gifer.com/B82h.gif" ,
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8QSSLGa6XIY2Jplh8T7iGoq6vtBaf_-WcCPxisKSBuWyRGcHU" ,
           "https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " seni öpüyor muck " + member.name )
    embed.set_image(url=random.choice(url2))
    await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def atam(ctx):
    url3 = ["https://img-s2.onedio.com/id-581d72669489d62f2420acbb/rev-0/w-635/f-jpg-gif-webp-webm-mp4/s-73c0f39431fd28c2b44c7d5b30b86b57eacd40c8.gif" , 
            "https://i.pinimg.com/originals/df/44/73/df4473e848fb97ba2a38e82b26ed4871.gif" ,
           "https://2.bp.blogspot.com/-4e7Vbu42i0w/WHHaQmlYQAI/AAAAAAAAB0U/xQPcRLzjNcQUdBnX4XbgX0EC25dNeJDVACLcB/s1600/atagif1.gif"]
    embed = discord.Embed(title=ctx.message.author.name)
    embed.set_image(url=random.choice(url3))
    await bot.say(embed=embed)

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

bot.run(os.environ.get('token'))

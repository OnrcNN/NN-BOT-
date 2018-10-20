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
    await bot.change_presence(game=discord.Game(name='OnrcNN''ın Haşmetlisi ile!'))

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
    url9 = ["https://thumbs.gfycat.com/FondEvergreenIcterinewarbler-max-1mb.gif" , 
            "https://i.gifer.com/B82h.gif" ,
           "https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657" ,
           "https://perspectivaypercepcion.files.wordpress.com/2016/04/tumblr_o4u84jvodk1s5wiico1_500.gif?w=662" ,
           "http://31.media.tumblr.com/fa20ef0dc64981e7d5df01e657fe82ad/tumblr_mofnbpnM291rgn0hpo1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " seni öpüyor " + member.name )
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def atam(ctx):
    url4 = ["https://img-s2.onedio.com/id-581d72669489d62f2420acbb/rev-0/w-635/f-jpg-gif-webp-webm-mp4/s-73c0f39431fd28c2b44c7d5b30b86b57eacd40c8.gif" , 
            "https://i.pinimg.com/originals/df/44/73/df4473e848fb97ba2a38e82b26ed4871.gif" ,
           "https://2.bp.blogspot.com/-4e7Vbu42i0w/WHHaQmlYQAI/AAAAAAAAB0U/xQPcRLzjNcQUdBnX4XbgX0EC25dNeJDVACLcB/s1600/atagif1.gif"]
    embed = discord.Embed(title=ctx.message.author.name)
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

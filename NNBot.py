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
           "https://78.media.tumblr.com/680b69563aceba3df48b4483d007bce3/tumblr_mxre7hEX4h1sc1kfto1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name )
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def sakso(ctx, member:discord.Member):
    url3 = ["http://3.bp.blogspot.com/-sogECXRDIQY/VthJpSqm43I/AAAAAAAAACM/7xzi5vgJH7Q/s1600/01.gif" , 
            "http://www.fairytailhentaidb.com/upload/2016/08/08/20160808103633-4c3e44bd.gif" ,
           "https://i.pinimg.com/originals/b9/bf/7b/b9bf7b4e38e86fdaaccb54c6e60c51e6.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " gloglolgogloglo " + member.name )
    embed.set_image(url=random.choice(url3))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def sik(ctx, member:discord.Member):
    url2 = ["http://www.dna2008.com/wp-content/uploads/cache-17904550a8d0bf1e019a5df2d3979fdf/2016/01/nt9byhyX5s1ue0mfso8_500.gif" , 
            "http://33.media.tumblr.com/dd7e4f6b177474afebe5392ae14fdd4c/tumblr_nfm5svfj8c1sjyos5o1_500.gif" ,
           "https://78.media.tumblr.com/tumblr_lhtimuSrzj1qgmrilo1_500.gif"]
    embed = discord.Embed(title=ctx.message.author.name + " seni çatur çutur sikiyor " + member.name )
    embed.set_image(url=random.choice(url2))
    await bot.say(embed=embed)    
    

@bot.command(pass_context=True)
async def sil (ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(x)
    await bot.delete_messages(mgs)

bot.run(os.environ.get('token'))

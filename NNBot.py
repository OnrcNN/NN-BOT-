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
    await bot.say("Buranın tanrısı")

@bot.command(pass_context=True)
async def yamur(ctx) :
    await bot.say("Best kankam")
                  
@bot.command(pass_context=True)
async def yağmur(ctx) :
    await bot.say("Best kankam")
                  
@bot.command(pass_context=True)
async def berkay(ctx) : 
    await bot.say("Yıkık biri")
                                                
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
async def soyle(ctx, *,content) :
    """Komuttan sonra yazdığınız şeyi bottan yazar"""
    await bot.delete_message(ctx.message)
    await bot.say(content)
    
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


@bot.command(pass_context=True)
async def inori(ctx):
    url6 = ["https://66.media.tumblr.com/a0cf0a8f45a4adae1d570759d66689f5/tumblr_oo7qio51KI1tlypw3o1_500.gif" ,
            "https://media.giphy.com/media/zv9JddBUO0V9e/giphy.gif" ,
            "https://66.media.tumblr.com/3b7452c2751d04ea45aef98ca0878915/tumblr_o4gooxHNdv1sfqz8qo6_r1_500.gif" ,
            "https://66.media.tumblr.com/3481d0b3f8bd4a35bb7d51b1d190c850/tumblr_oswj6gdzdr1v14hqvo1_500.gif" ,
            "https://66.media.tumblr.com/1f8c15ffb636d73530541d4356ce9aa3/tumblr_os3q8iWAO51wn2b96o1_500.gif " ,
            "https://data.whicdn.com/images/26749996/original.gif" ,
            "https://pa1.narvii.com/6439/5066d7796e9e894c0201d020cf645d201ff183e3_hq.gif" ,
            "https://media.giphy.com/media/MYIYxlikuTAUU/giphy.gif" ,
            "https://thumbs.gfycat.com/SorrowfulLittleChicken-size_restricted.gif" ,
            "https://thumbs.gfycat.com/LeftCoordinatedCrossbill-size_restricted.gif" ,
            "http://24.media.tumblr.com/be5f000b7e167c9f1bd43277c0f8da00/tumblr_mz0ba9SjN01qitjclo1_500.gif"]
    embed = discord.Embed(title="Yuzuriha Inori :heart:")
    embed.set_image(url=random.choice(url6))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def neko(ctx):
    url7 = ["https://media1.tenor.com/images/21515181b13a4dd39202662ebd50e558/tenor.gif?itemid=9780123" ,
            "https://data.whicdn.com/images/216019175/original.gif" ,
            "https://media1.tenor.com/images/6908f3de8ce18b0e368251a6392adc87/tenor.gif?itemid=5036492" ,
            "https://pa1.narvii.com/5922/d781e657a65e3f88c1cb3e4a4a721db64b026ece_hq.gif" ,
            "https://media.giphy.com/media/J7dZvJh4gOMve/giphy.gif" ,
            "https://data.whicdn.com/images/138118590/original.gif" ,
            "https://media.giphy.com/media/nHOxOhjR837fW/giphy.gif" ,
            "https://media1.tenor.com/images/3fab0026a18a647c790890fdd6badde2/tenor.gif?itemid=5615368" ,
            "https://vignette.wikia.nocookie.net/slaveleiafanfiction/images/6/6b/Cute_Mew.gif/revision/latest?cb=20180314185712" ,
            "https://data.whicdn.com/images/176566371/original.gif" ,
            "https://media1.tenor.com/images/f93e8ad496feac35d48a0d01f94dc871/tenor.gif?itemid=7861837" ,
            "https://data.whicdn.com/images/302452164/original.gif" ,
            "https://thumbs.gfycat.com/BlandFairInchworm-max-1mb.gif" ,
            "https://media3.giphy.com/media/jCaU8WfesJfH2/giphy.gif?cid=3640f6095be813e5476c6c446728ee46" ,
            "https://media1.giphy.com/media/eenSsRGbw8C4g/giphy.gif?cid=3640f6095be813e5476c6c446728ee46"]
    embed = discord.Embed(title="Neko")
    embed.set_image(url=random.choice(url7))
    await bot.say(embed=embed)
    
bot.run(os.environ.get('token'))    

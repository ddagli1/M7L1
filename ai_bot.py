import discord  # Discord kütüphanesini içe aktarıyoruz
from discord.ext import commands  # Komut sistemi için gerekli modülü içe aktarıyoruz
import os 
#🚀 pip install pipenv, pipenv --python 3.11 -> pipenv shell

# Botun çalışması için gerekli izinleri belirliyoruz
intents = discord.Intents.default()
intents.messages = True  # Mesajları okuyabilmesi için izin veriyoruz
intents.guilds = True  # Sunuculara erişim izni veriyoruz
intents.message_content = True  # Mesaj içeriğini okuyabilmesi için gerekli izin

# Botu oluşturuyoruz ve komut ön ekini '!' olarak belirliyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

#GÖRSELLER İÇİN KLASÖRÜ OLUŞTURUYORUZ
IMAGE_DIR="images"
os.makedirs(IMAGE_DIR,exist_ok=True) 

@bot.event
async def on_ready():
    print(f"Bot {bot.user} olarak giriş yaptı!")


@bot.command()
async def hello(ctx):
    await ctx.send("Merhaba! Ben bir AI botuyum. Size nasıl yardımcı olabilirim?")



@bot.command()
async def check(ctx):
    if ctx.message.attachments: # kullanıcının gönderdiği mesajda ekler(dosyalar) varsa
        for attachment in ctx.message.attachments:
            file_name = attachment.filename

            file_path= os.path.join(IMAGE_DIR, file_name)
            await attachment.save(file_path) 
            await ctx.send("Görseliniz başarılı şekilde kaydoldu:))")
    else:
        await ctx.send("Maalesef görsel göndermeyi unuttun, tekrar dene:))")



# Token ile botu çalıştır (Kendi token'ını buraya eklemelisin)
bot.run("TOKEN")

import discord  # Discord kütüphanesini içe aktarıyoruz
from discord.ext import commands  # Komut sistemi için gerekli modülü içe aktarıyoruz
import os  # Dosya işlemleri için os modülünü içe aktarıyoruz

# Botun çalışması için gerekli izinleri belirliyoruz
intents = discord.Intents.default()
intents.messages = True  # Mesajları okuyabilmesi için izin veriyoruz
intents.guilds = True  # Sunuculara erişim izni veriyoruz
intents.message_content = True  # Mesaj içeriğini okuyabilmesi için gerekli izin

# Botu oluşturuyoruz ve komut ön ekini '!' olarak belirliyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# Görsellerin kaydedileceği klasörü belirliyoruz
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)  # Klasör yoksa oluştur

# 'check' komutu tanımlıyoruz, bu komut görselleri kontrol edip kaydedecek
@bot.command()
async def check(ctx):
    # Mesajın ekli bir dosya içerip içermediğini kontrol ediyoruz
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:  # Mesajdaki tüm ekleri döngüyle kontrol ediyoruz
            file_name = attachment.filename  # Dosya adını alıyoruz
            file_ext = file_name.split(".")[-1].lower()  # Dosya uzantısını küçük harfe çeviriyoruz

            # Desteklenen dosya uzantılarını belirliyoruz
            allowed_extensions = ["png", "jpg", "jpeg"]
            if file_ext not in allowed_extensions:  # Eğer dosya formatı desteklenmiyorsa
                await ctx.send(f"❌ Geçersiz dosya formatı! Sadece {', '.join(allowed_extensions)} uzantıları desteklenmektedir.")
                return  # Komutu sonlandır

            # Dosyanın kaydedileceği yolu oluşturuyoruz
            file_path = os.path.join(IMAGE_DIR, file_name)

            try:
                await attachment.save(file_path)  # Dosyayı belirtilen klasöre kaydediyoruz
                await ctx.send(f"✅ Görsel başarıyla kaydedildi: `{file_path}`")  # Kullanıcıya başarı mesajı gönderiyoruz
            except Exception as e:  # Eğer bir hata oluşursa
                await ctx.send(f"⚠️ Görsel kaydedilirken hata oluştu: {str(e)}")  # Kullanıcıya hata mesajı gönderiyoruz
    else:
        await ctx.send("⚠️ Görsel yüklemeyi unuttun!")  # Kullanıcıya görsel yüklemesi gerektiğini hatırlatıyoruz


# Token ile botu çalıştır (Kendi token'ını buraya eklemelisin)
bot.run("TOKEN")

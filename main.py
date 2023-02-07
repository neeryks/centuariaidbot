import discord
from process import Responder


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(".i"):
        data = Responder()
        data.img_complete(f"{message.content[2::]}")
        with open("img.jpg","rb") as imager:
            pic = discord.File(imager)
            await message.channel.send(file = pic)

    elif message.content.startswith(''):
        data = Responder()
        ndat = data.text_complete(f"{message.content}")
        await message.channel.send(f'{ndat.choices[0].text}')



client.run('MTA3MjQ3MTI2ODE0MzY4MTYxNw.GDsp2m.DyxCXG5ZlwSoHWUugbD-TzMBDXLrbhTfNmxHR4')
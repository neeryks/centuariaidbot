import discord
from process import Responder
import people_also_ask
import os
from dman import DataExtractor
from blogwrite import BlogAi
from auth import Auth

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
    
    if message.content.startswith("/i"):
        data = Responder()
        data.img_complete(f"{message.content[2::]}")
        with open("img.jpg","rb") as imager:
            pic = discord.File(imager)
            await message.channel.send(file = pic)

    elif message.content.startswith("/c"):
        data = Responder()
        await message.channel.send("From Codex...")
        ndat = data.code_complete(f"{message.content[2::]}")
        await message.channel.send(f'{ndat.choices[0].text}')

    elif message.content.startswith('/t'):
        data = Responder()
        ndat = data.text_complete(f"{message.content[2::]}")
        await message.channel.send(f'{ndat.choices[0].text}')
    
    elif message.content.startswith('/blog'):
        textfile = discord.File(BlogAi(message.content[6::]).section_writer())
        await message.channel.send(file=textfile)
        
# Added Support for PAA
    elif message.content.startswith("/paa"):
        if message.content[-1].isdigit():
            if message.content[4:8]=="-txt":
                q =  people_also_ask.get_related_questions(f"{message.content[8:-2]}",int(message.content[-2::]) )
                for i in q:
                    with open("kwd-paa.txt","a+") as fl:
                        fl.write(f"{i}\n")
                txtfile = discord.File("kwd-paa.txt")
                await message.channel.send(file=txtfile)
                f = open("kwd-paa.txt","r+")
                f.truncate()

            else:
                q =  people_also_ask.get_related_questions(f"{message.content[5:-2]}",int(message.content[-2::]) )
                for i in q:
                    await message.channel.send(i)

        elif message.content[4:9]=="-list":
            path = "dataset/paa"
            dir_list = os.listdir(path)
            await message.channel.send(dir_list)
            await message.channel.send("To View PAA's Enter : .paa-ds [filename] [Number of Queries]")

        elif message.content[4:7]=="-ds":
            contline = message.content.split(" ")
            datset = DataExtractor()
            await message.channel.send(datset.file_reader(contline[1],contline[2]))
            
        else:
            q =  people_also_ask.get_related_questions(f"{message.content[5::]}")
            for i in q:
                await message.channel.send(i)
        await message.channel.send("Request Processed, Ask Another After 5min from .paa")

    elif message.content.startswith("/ask"):
        q= people_also_ask.get_simple_answer(f"{message.content[5::]}")
        await message.channel.send(q)
        await message.channel.send("Request Processed, Ask Another After 15sec from .ask")
    
    elif message.content.startswith("/update"):
        os.system("cd ~/")
        os.system("./update.sh")
        


client.run(Auth.discord_token())

    


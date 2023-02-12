import discord
from process import Responder
import people_also_ask
import time
import os


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
@people_also_ask.generate_related_questions
def slp():
    return time.sleep(3)

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

    elif message.content.startswith(".c"):
        data = Responder()
        await message.channel.send("From Codex...")
        ndat = data.code_complete(f"{message.content[2::]}")
        await message.channel.send(f'{ndat.choices[0].text}')

    elif message.content.startswith('.t'):
        data = Responder()
        ndat = data.text_complete(f"{message.content[2::]}")
        await message.channel.send(f'{ndat.choices[0].text}')
    
    elif message.content.startswith('.blog'):
        data = Responder()
        meta_title = data.text_complete(f"meta title on {message.content[6::]}").choices[0].text
        cont_outline = data.text_complete(f"blog outlne on {meta_title}").choices[0].text
        #print(cont_outline)
        cont_list = list(cont_outline.split("\n"))
        with open(f"blog.txt","a+") as blog_file:
            blog_file.write(f"<h1>{cont_outline}</h1>\n")
            for li in cont_list:
                section = data.text_complete(f"blog section on {li}").choices[0].text
                blog_file.write(f"<h2>{li}</h2>\n")
                blog_file.write(f"{section}\n")
        textfile = discord.File("blog.txt")
        await message.channel.send(file=textfile)
        f= open("blog.txt","+r")
        f.truncate(0)
# Added Support for PAA
    elif message.content.startswith(".paa"):
        if message.content[-1].isdigit():
            if message.content[4:8]=="-txt":
                q =  people_also_ask.get_related_questions(f"{message.content[8:-2]}",int(message.content[-2::]) )
                for i in q:
                    with open("kwd-paa.txt","+a") as fl:
                        fl.write(f"{i}\n")
                txtfile = discord.File("kwd-paa.txt")
                await message.channel.send(file=txtfile)
                f = open("kwd-paa.txt","+r")
                f.truncate()

            else:
                q =  people_also_ask.get_related_questions(f"{message.content[5:-2]}",int(message.content[-2::]) )
                for i in q:
                    await message.channel.send(i)
        else:
            q =  people_also_ask.get_related_questions(f"{message.content[5::]}")
            for i in q:
                await message.channel.send(i)
        await message.channel.send("Request Processed, Ask Another After 5min from .paa")

    elif message.content.startswith(".askme"):
        q= people_also_ask.get_simple_answer(f"{message.content[5::]}")
        await message.channel.send(q)
        await message.channel.send("Request Processed, Ask Another After 15sec from .ask")
    
    elif message.content.startswith(".update"):
        os.system("cd")
        os.system("python3 update.py")
        



client.run('MTA3MjQ3MTI2ODE0MzY4MTYxNw.GDsp2m.DyxCXG5ZlwSoHWUugbD-TzMBDXLrbhTfNmxHR4')
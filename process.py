
import os
import openai
import requests
from auth import Auth
class Responder(Auth):
    def __init__(self,Auth) -> None:
        token = Auth()
        token.openai_token()
    
    
    def text_complete(self,rpr):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Seo optimised article writer"},
        {"role": "assistant", "content":"write an article with blog outline explaining each section and 5 people also ask question with answers in HTML using H1,H2,H3,bold,list"},
        {"role": "user", "content": rpr}
        ])
        return response['choices'][0]['message']['content']
    
    def article_complete(self,rpr):
        print("trying")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Seo optimised article writer"},
        {"role": "assistant", "content":"write an article with blog outline explaining each section and 5 people also ask question with answers in HTML using H1,H2,H3,bold,list"},
        {"role": "user", "content": f"write a fully optimised article on {rpr} and 5 questions with answers form people also asked section"}
        ])
        print("tried")
        return response['choices'][0]['message']['content']

    def meta_complete(self,rpr):
        print("trying01")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Seo optimised article writer"},
        {"role": "assistant", "content":"write an article with blog outline explaining each section and 5 people also ask question with answers in HTML using H1,H2,H3,bold,list"},
        {"role": "user", "content": f"write a meta section on {rpr}"}
        ])
        print("tried01")
        return response['choices'][0]['message']['content']
    
    def title_complete(self,rpr):
        print("trying02")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Seo optimised article writer"},
        {"role": "assistant", "content":"write an article with blog outline explaining each section and 5 people also ask question with answers in HTML using H1,H2,H3,bold,list"},
        {"role": "user", "content": f"3 Seo optimised title on {rpr}"}
        ])
        print("tried02")
        return response['choices'][0]['message']['content']
    
    def outline_complete(self,rpr):
        print("trying03")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Seo optimised article writer"},
        {"role": "assistant", "content":"write an article with blog outline explaining each section and 5 people also ask question with answers in HTML using H1,H2,H3,bold,list"},
        {"role": "user", "content": f"Seo optimised blog outline and sections on {rpr}"}
        ])
        print("tried03")
        return response['choices'][0]['message']['content']

    def img_complete(self,rpr):
        response = openai.Image.create(
        prompt=f"""{rpr}""",
        n=1,
        size="256x256"
        )   
        image_url = response['data'][0]['url']
        img = requests.get(image_url)
        open("img.jpg","wb").write(img.content)
        return 0

if __name__ == "__main__":
    obj1 = Responder()
    inp = input("Which Mode :> Text or Image or code: T/I/C ")
    while 5 < 6:
        newin = input(":>")
        if inp == "T":
            newdo = obj1.text_complete(f"{newin}")
            print(newdo)
        elif inp == "I":
            newdo = obj1.img_complete(f"{newin}")
            print(newdo)


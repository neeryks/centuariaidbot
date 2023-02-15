
import os
import openai
import requests
from auth import Auth
class Responder():
    def __init__(self) -> None:
        openai.api_key = Auth.openai_token()
    
    def text_complete(self,rpr):
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"""{rpr}""",
        temperature=0.7,
        max_tokens=800
        )

        return response

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
    
    def code_complete(self,rpr):
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=f"""{rpr}""",
            #temprature=0.5,
            max_tokens=800  
        )
        return response
    def test():
        pass


if __name__ == "__main__":
    obj1 = Responder()
    inp = input("Which Mode :> Text or Image or code: T/I/C ")
    while 5 < 6:
        newin = input(":>")
        if inp == "T":
            newdo = obj1.text_complete(f"{newin}")
            print(newdo.choices[0].text)
        elif inp == "I":
            newdo = obj1.img_complete(f"{newin}")
            print(newdo)
        elif inp == "C":
            newdo = obj1.code_complete(f"{newin}")
            print("In Code Mode")
            print(newdo.choices[0].text)

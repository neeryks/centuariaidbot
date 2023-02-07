
import os
import openai
import requests

class Responder():
    def __init__(self) -> None:
        openai.api_key = "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"
    
    def text_complete(self,rpr):
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"{rpr}",
        temperature=0.7,
        max_tokens=709)

        return response

    def img_complete(self,rpr):
        response = openai.Image.create(
        prompt=f"{rpr}",
        n=1,
        size="256x256"
        )   
        image_url = response['data'][0]['url']
        img = requests.get(image_url)
        open("img.jpg","wb").write(img.content)
        return 0
    def code_complete():
        pass
    def test():
        pass


if __name__ == "__main__":
    obj1 = Responder()
    inp = input("Which Mode :> Text or Image: T/I ")
    while 5 < 6:
        newin = input(":>")
        if inp == "T":
            newdo = obj1.text_complete(f"{newin}")
            print(newdo.choices[0].text)
        elif inp == "I":
            newdo = obj1.img_complete(f"{newin}")
            print(newdo)

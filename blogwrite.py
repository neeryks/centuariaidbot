from process import Responder
import openai

class BlogAi(Responder):
    def __init__(self,topic) -> None:
        self.topic = topic
        openai.api_key = "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"

    def outline_maker(self):

        outline = self.text_complete(f"blog outline on {self.topic}").choices[0].text
        return outline.split("\n")
    
    def section_writer(self):
        list_data = self.outline_maker()
        with open(f"dataset/paa/{self.topic}.txt","+a") as blog_post:
            blog_post.write(self.topic)
            for i in list_data:
                if i == '':
                    blog_post.write("\n")
                elif i.startswith("-"):
                    i = i[1::]
                    blog_post.write(f"\n")
                    blog_post.write(f"{i}")
                    blog_section = self.text_complete(f"write a blog section on {i}").choices[0].text
                    blog_post.write(f"{blog_section}\n")
                else: 
                    blog_section = self.text_complete(f"write a blog section on {i}").choices[0].text
                    blog_post.write(f"{i}\n")
                    blog_post.write(f"{blog_section}\n")
        return f"dataset/{self.topic}.txt"

 

if __name__ == "__main__":
    object1 = BlogAi("Artificial Intelligence")
    print(object1.outline_maker())
        




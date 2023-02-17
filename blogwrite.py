from process import Responder
from auth import Auth
import openai

class BlogAi(Responder,Auth):
    def __init__(self,topic) -> None:
        self.topic = topic
        openai.api_key = self.openai_token()     

    def outline_maker(self):

        outline = self.text_complete(f"blog outline on {self.topic}").choices[0].text
        return outline
       
    def section_writer_txt(self):
        list_data = self.outline_maker().split("\n")
        with open(f"dataset/saved_blogs/{self.topic}.txt","a+") as blog_post:
            blog_title = self.title()
            blog_post.write(blog_title)
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
        return f"dataset/saved_blogs/{self.topic}.txt"
        
    def title(self):
        blog_title = self.text_complete(f"write a blog title on {self.topic}").choices[0].text
        return blog_title
    
def section_maker(section_topic):
    if section_topic == "" and section_topic.startswith("-"):
        blog_section = "-----------------"
    else:
        obj = Responder()
        blog_section = obj.text_complete(f"write a blog section on {section_topic}").choices[0].text
    return blog_section



 

if __name__ == "__main__":
    object1 = BlogAi("Artificial Intelligence")
    print(object1.outline_maker())
        




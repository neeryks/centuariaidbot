import gradio as gr
from process import Responder
from auth import Auth

class cbot(Responder,Auth):
    def __init__(self) -> None:
        token = Auth()
        token.openai_token()

    def blog_write(self,title,mode):
        print(mode,title)
        if mode == "Write Article":
            obj1 = self.article_complete(title)
        elif mode == "Write Meta":
            obj1 = self.meta_complete(title)
        elif mode == "Write Title":
            obj1 = self.title_complete(title)
        elif mode == "Write Outline":
            obj1 = self.outline_complete(title)
        else:
            obj1 = self.text_complete(title)

        return obj1
    
    def output(self):
        demo = gr.Interface(fn=self.blog_write,inputs=["text",gr.Dropdown(["Write Article","Write Meta","Write Title","Write Outline"],label="Choose Mode")],outputs="text")
        return demo.launch()
    

if __name__ == "__main__":
    display = cbot()
    display.output()


    
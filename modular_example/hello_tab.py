import gradio as gr

def hello_world(name):
    return "Hello " + name

hello_interface = gr.Interface(hello_world, "text", "text")
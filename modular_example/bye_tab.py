import gradio as gr

def bye_world(name):
    return "Bye " + name

bye_interface = gr.Interface(bye_world, "text", "text")
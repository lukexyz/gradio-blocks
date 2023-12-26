import gradio as gr
from hello_tab import hello_interface
from bye_tab import bye_interface

demo = gr.TabbedInterface([hello_interface, bye_interface], ["Hello World", "Bye World"])

if __name__ == "__main__":
    demo.launch()

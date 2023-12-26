import gradio as gr
from hello_tab import hello_block
from bye_tab import bye_block

def main():
    with gr.Blocks() as app:
        gr.Markdown("### Multi-Tab Gradio App")
        with gr.Tabs():
            with gr.Tab("Hello World"):
                hello_block()
            with gr.Tab("Bye World"):
                bye_block()

    app.launch()

if __name__ == "__main__":
    main()

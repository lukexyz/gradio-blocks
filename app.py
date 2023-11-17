import gradio as gr
from gradio import components

def enhance_text(text1, text2):
    return text1 + text2

with gr.Blocks() as interface:
    gr.Markdown(f"Gradio demos using version {gr.__version__}")
    with gr.Tab("Text Enhancer"):
        text_input1 = gr.Textbox(label="Input 1")
        text_input2 = gr.Textbox(label="Input 2")
        text_output = gr.Textbox()

        text_input1.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)
        text_input2.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)

    with gr.Tab("Tab 2"):
        with gr.Accordion("Open for more tab 2"):
            gr.Markdown("coming soon...")

    with gr.Tab("Tab 3"):
        gr.Markdown("# Greetings from Gradio!")
        inp = gr.Textbox(placeholder="What is your name?", label="inp")
        out = gr.Textbox()

        inp.change(fn=lambda x: f"Welcome, {x}!",
                inputs=inp,
                outputs=out)

if __name__ == "__main__":
    interface.launch()

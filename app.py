import gradio as gr

def enhance_text(text1, text2):
    return text1 + " " + text2


with gr.Blocks() as demo:
    gr.Markdown(f"🎨 Gradio demos with `gradio {gr.__version__}`")
    with gr.Tab("📡 1. Event Listener"):
        with gr.Column():
            text_input1 = gr.Textbox(label="text_input1")
            text_input2 = gr.Textbox(label="text_input2")
            gr.Markdown("↓ (The texts above are processed and combined here) ↓")
        with gr.Column():
            text_output = gr.Textbox(label="Output: Enhanced Text")

        text_input1.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)
        text_input2.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)

    with gr.Tab("🗂️ 2. Tab 2"):
        with gr.Accordion("Open for more tab 2"):
            gr.Markdown("coming soon...")

    with gr.Tab("🧩 3. Tab 3"):
        gr.Markdown("# Tab 3 features")
        inp = gr.Textbox(placeholder="What is your name?", label="inp")
        out = gr.Textbox()

        inp.change(fn=lambda x: f"Welcome, {x}!",
                inputs=inp,
                outputs=out)



if __name__ == "__main__":
    demo.launch()
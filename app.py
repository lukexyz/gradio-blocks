import gradio as gr
import os

def enhance_text(text1, text2):
    return text1 + " " + text2

def combine(a, b):
    return a + " " + b


def mirror(x):
    return x

with gr.Blocks() as demo:
    gr.Markdown(f"🎨 Gradio demos with `gradio {gr.__version__}`")
    with gr.Tab("📡 1. Event Listener"):
        with gr.Row():
            with gr.Column():
                text_input1 = gr.Textbox(label="text_input1")
                text_input2 = gr.Textbox(label="text_input2")
            with gr.Column():
                gr.Markdown("↓ (The texts above are processed and combined here) ↓")
                text_output = gr.Textbox(label="Output: Enhanced Text")

                text_input1.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)
                text_input2.change(enhance_text, inputs=[text_input1, text_input2], outputs=text_output)

    with gr.Tab("🗂️ 2. Tab 2"):

        txt = gr.Textbox(label="Input", lines=2)
        txt_2 = gr.Textbox(label="Input 2")
        txt_3 = gr.Textbox(value="", label="Output")
        btn = gr.Button(value="Submit")
        btn.click(combine, inputs=[txt, txt_2], outputs=[txt_3])

        with gr.Row():
            im = gr.Image()
            im_2 = gr.Image()

        btn = gr.Button(value="Mirror Image")
        btn.click(mirror, inputs=[im], outputs=[im_2])

        gr.Markdown("## Text Examples")
        gr.Examples(
            [["hi", "Adam"], ["hello", "Eve"]],
            [txt, txt_2],
            txt_3,
            combine,
            cache_examples=True,
        )
        gr.Markdown("## Image Examples")
        gr.Examples(
            examples=[os.path.join(os.path.dirname(__file__), "lion.jpg")],
            inputs=im,
            outputs=im_2,
            fn=mirror,
            cache_examples=True,
        )



    with gr.Tab("🧩 3. Tab 3"):
        gr.Markdown("# Tab 3 features")
        inp = gr.Textbox(placeholder="What is your name?", label="inp")
        out = gr.Textbox()

        inp.change(fn=lambda x: f"Welcome, {x}!",
                inputs=inp,
                outputs=out)

if __name__ == "__main__":
    demo.launch()
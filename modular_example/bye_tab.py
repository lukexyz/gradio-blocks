import gradio as gr

def bye_block():
    with gr.Blocks() as bye_world_tab:
        with gr.Row():
            name_input = gr.Textbox(label="Your Name")
            bye_button = gr.Button("Say Bye")
        output = gr.Textbox(label="Farewell")

        bye_button.click(fn=lambda name: f"Bye {name}", inputs=name_input, outputs=output)

    return bye_world_tab

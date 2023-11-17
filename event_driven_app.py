import gradio as gr

def update_text(input_text, additional_text):
    # Concatenates the input text with the additional text
    return input_text + additional_text

def main():
    with gr.Blocks() as demo:
        with gr.Row():
            input_box1 = gr.Textbox(label="Input Box 1", placeholder="Type here...")
            additional_text_box = gr.Textbox(label="Additional Text", placeholder="Add extra text here...")
        
        # Text component to display the result
        result_text = gr.Text(label="Concatenated Result")

        # Function to update the result text based on the inputs
        def on_text_change(change_event):
            updated_text = update_text(change_event["new"], additional_text_box.value)
            result_text.update(value=updated_text)

        # Attach the change event listener to the first input box
        input_box1.change(on_text_change, inputs=[input_box1, additional_text_box], outputs=[result_text])

    demo.launch()

if __name__ == "__main__":
    main()
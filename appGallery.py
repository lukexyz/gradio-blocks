import gradio as gr
import json
import numpy as np

# pip install -r requirements-gradio-2.5.txt

def all_features(
    text_input: str, slider_input: int, checkbox_input: bool, 
    radio_input: str, dropdown_input: str, image_input: np.ndarray,
    webcam_input: np.ndarray, 
     date_input: str):
    
    # Create a dictionary to hold all the inputs
    all_inputs = {
        "text_input": text_input,
        "slider_input": slider_input,
        "checkbox_input": checkbox_input,
        "radio_input": radio_input,
        "dropdown_input": dropdown_input,
        "image_input": image_input.tolist(),
        "webcam_input": webcam_input.tolist(),

        "date_input": date_input
    }

    # For demonstration, just return the inputs in various formats
    return text_input, radio_input, [["Header1", "Header2"], [slider_input, checkbox_input]], image_input, file_input, audio_input, json.dumps(all_inputs, indent=4)

# Define the interface
demo = gr.Interface(
    fn=all_features, 
    inputs=[
        gr.inputs.Textbox(label="Text Input"),
        gr.inputs.Slider(minimum=0, maximum=10, label="Slider Input"),
        gr.inputs.Checkbox(label="Checkbox Input"),
        gr.inputs.Radio(["Option 1", "Option 2"], label="Radio Input"),
        gr.inputs.Dropdown(["Choice 1", "Choice 2"], label="Dropdown Input"),
        gr.inputs.Webcam(label="Webcam Input"),
        gr.inputs.Date(label="Date Input")
    ], 
    outputs=[
        gr.outputs.Textbox(label="Text Output"),
        gr.outputs.Label(label="Label Output"),
        gr.outputs.Table(label="Table Output"),
        gr.outputs.Image(label="Image Output"),
        gr.outputs.Json(label="Json Output")
    ],
    layout=[
        gr.Row([
            gr.Column([
                "text_input", "slider_input", "checkbox_input",
                "radio_input", "dropdown_input"
            ]),
            gr.Column([
                "image_input", "webcam_input",
                "file_input", "audio_input", "date_input"
            ])
        ]),
        gr.Row([
            gr.Column([
                "Textbox Output", "Label Output", "Table Output"
            ]),
            gr.Column([
                "Image Output", "File Output", "Audio Output", "Json Output"
            ])
        ])
    ]
)

demo.launch(share=False)

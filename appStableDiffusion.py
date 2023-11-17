import gradio as gr

# Dropdown for the checkpoint
checkpoint_dropdown = gr.inputs.Dropdown(["protogenX340ficial@..."], label="Stable Diffusion checkpoint")

# Textbox for the negative prompt
negative_prompt = gr.inputs.Textbox(lines=3, placeholder="Negative prompt")

# Dropdown for the sampling method
sampling_method = gr.inputs.Dropdown(["Euler a"], label="Sampling method")

# Slider for the sampling steps
sampling_steps = gr.inputs.Slider(minimum=1, maximum=100, default=20, label="Sampling steps")

# Dropdown for the script selection
script = gr.inputs.Dropdown(["None"], label="Script")

# Checkboxes
checkboxes = gr.inputs.Radio(
    options=["Restore faces", "Tiling", "Hires. fix"], 
    type="checkbox",
    label="Options"
)

# Numeric Input fields for Width, Height, Batch count, Batch size
width = gr.inputs.Number(default=512, label="Width")
height = gr.inputs.Number(default=512, label="Height")
batch_count = gr.inputs.Number(default=4, label="Batch count")
batch_size = gr.inputs.Number(default=1, label="Batch size")

# Slider for CFG Scale
cfg_scale = gr.inputs.Slider(minimum=1, maximum=100, default=12, label="CFG Scale")

# Numeric Input for Seed
seed = gr.inputs.Number(default=144178169, label="Seed")

# Image output and style selectors
image_output = gr.outputs.Image()
style_1 = gr.inputs.Dropdown(["None"], label="Style 1")
style_2 = gr.inputs.Dropdown(["None"], label="Style 2")

# Dummy function to pass into Interface
def dummy_function(*args):
    return "https://via.placeholder.com/512"

# Create the Gradio Interface
interface = gr.Interface(
    fn=dummy_function,
    inputs=[
        checkpoint_dropdown, negative_prompt, sampling_method, sampling_steps, script,
        checkboxes, width, height, batch_count, batch_size, cfg_scale, seed, style_1, style_2
    ],
    outputs=image_output,
    live=True
)

interface.launch()

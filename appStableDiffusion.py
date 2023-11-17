import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import random

def generate_image(prompt, sampling_method, sampling_steps, width, height):
    # Generate random RGB values for a shade of pink or purple
    R = random.randint(200, 255)
    G = random.randint(100, 192)
    B = random.randint(180, 255)
    img = Image.new('RGB', (width, height), (R, G, B))
    draw = ImageDraw.Draw(img)
    
    # Set font size and type (use a default PIL font as an example; you can specify a different TTF font)
    font_size = 40
    try: font = ImageFont.truetype("arial.ttf", font_size)
    except IOError: font = ImageFont.load_default()
    
    # Add text to image
    text_color = (255 - R, 255 - G, 255 - B)  # Use complementary color for visibility
    draw.text((10, 10), prompt, font=font, fill=text_color)
    
    return img

with gr.Blocks() as demo:
    gr.Markdown("Image Generation with Gradio")
    prompt = gr.Textbox(lines=3, label="Your Prompt")
    with gr.Row():
        with gr.Column():
            negative_prompt = gr.Textbox(lines=3, label="Negative Prompt")
            steps = gr.Slider(label='Inference Steps',value=25,
                              info="How many denoising steps?")
            guidance = gr.Slider(label='Guidance Scale', minimum=1, maximum=20, value=7,
                              info="Controls how much the text prompt influences the result.")
            width = gr.Slider(label='Width', minimum=64, maximum=512, step=64, value=512)
            height = gr.Slider(label='Height', minimum=64, maximum=512, step=64, value=512)
            btn = gr.Button("Submit")
        with gr.Column():
            output = gr.Image(label='Result')

        btn.click(fn=generate_image, inputs=[prompt, steps, guidance, width, height], outputs=[output])
    demo.launch(share=False)
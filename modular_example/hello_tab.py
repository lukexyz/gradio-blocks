import gradio as gr
import altair as alt
import pandas as pd
import numpy as np

def generate_plot(num_points, point_color, add_trend_line):
    # Generate random data
    data = pd.DataFrame({
        'x': np.random.rand(num_points),
        'y': np.random.rand(num_points)
    })

    # Create a scatter plot
    scatter_plot = alt.Chart(data).mark_circle(color=point_color).encode(
        x='x',
        y='y'
    )

    # Optionally add a trend line
    if add_trend_line:
        scatter_plot = scatter_plot + scatter_plot.transform_regression('x', 'y').mark_line()

    return scatter_plot.to_json()

def hello_block():
    with gr.Blocks() as hello_world_tab:
        gr.Markdown("### Generate a Scatter Plot")
        with gr.Row():
            num_points = gr.Slider(minimum=10, maximum=100, value=50, label="Number of Points")
            point_color = gr.Dropdown(choices=['blue', 'green', 'red', 'orange'], value='blue', label="Point Color")
            add_trend_line = gr.Checkbox(value=False, label="Add Trend Line")
            submit_button = gr.Button("Generate Plot")
        plot_output = gr.Plot()

        submit_button.click(
            fn=generate_plot, 
            inputs=[num_points, point_color, add_trend_line], 
            outputs=plot_output
        )

    return hello_world_tab

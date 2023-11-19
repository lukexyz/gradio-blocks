import gradio as gr

# Define functions for each tab
def interface_example():
    return "Interface Example"

def chat_interface_example():
    return "Chat Interface Example"

def tabbed_interface_example():
    return "Tabbed Interface Example"

def blocks_example():
    return "Blocks Example"

def components_example():
    return "Components Example"

def helpers_example():
    return "Helpers Example"

def modals_example():
    return "Modals Example"

def routes_example():
    return "Routes Example"

def other_example():
    return "Other Example"

# Create interfaces for each tab
interface_tab = gr.Interface(fn=interface_example, inputs=[], outputs="text")
chat_interface_tab = gr.Interface(fn=chat_interface_example, inputs=[], outputs="text")
tabbed_interface_tab = gr.Interface(fn=tabbed_interface_example, inputs=[], outputs="text")
blocks_tab = gr.Interface(fn=blocks_example, inputs=[], outputs="text")
components_tab = gr.Interface(fn=components_example, inputs=[], outputs="text")
helpers_tab = gr.Interface(fn=helpers_example, inputs=[], outputs="text")
modals_tab = gr.Interface(fn=modals_example, inputs=[], outputs="text")
routes_tab = gr.Interface(fn=routes_example, inputs=[], outputs="text")
other_tab = gr.Interface(fn=other_example, inputs=[], outputs="text")

# Create a TabbedInterface with all the tabs
demo = gr.TabbedInterface(
    interfaces=[
        interface_tab, 
        chat_interface_tab, 
        tabbed_interface_tab, 
        blocks_tab, 
        components_tab, 
        helpers_tab, 
        modals_tab, 
        routes_tab, 
        other_tab
    ],
    tab_names=[
        "Interface", 
        "Chat Interface", 
        "Tabbed Interface", 
        "Blocks", 
        "Components", 
        "Helpers", 
        "Modals", 
        "Routes", 
        "Other"
    ]
)

demo.launch()

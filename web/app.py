import gradio as gr

def sentence_builder(prompt, target_audience, format, tone, active_tab):
    return f"""Target:: {target_audience} \n Format:: {format} & Tone:: {tone} \n Active Tab:: {active_tab} \n\n Prompt:: {prompt}"""


with gr.Blocks() as app:
    gr.Markdown("# Expressly - Text Transformation App")
    
    with gr.Row():
        # Left Column for Inputs
        with gr.Column(scale=1):
            prompt = gr.Textbox(label="Message Expressly", max_length=1024, lines=3)
            
            # Create a state variable to store active tab
            active_tab = gr.State("target_audience")
            
            with gr.Tab("Target Audience", id="tab_audience") as tab1:
                target_audience = gr.Dropdown(
                    ["LinkedIn Post", "WhatsApp Message", "Tweet", "News Article", "Technical Blog", 
                     "Formal Email", "Instagram Post", "Website Content", "Marketing Email", 
                     "Job Application", "Customer Support Response"], 
                    label="Target Audience", 
                    info="Pick a Target Audience to specify the purpose or platform."
                )
                # Update state when this tab is selected
                tab1.select(lambda: "target_audience", None, active_tab)
            
            with gr.Tab("Format & Tone", id="tab_format") as tab2:
                format = gr.Dropdown(
                    ["Post", "Chat", "Tweet", "Email", "Blog", "Article", "Report", "Product Description"], 
                    label="Format", 
                    info="Choose a Format to define the type of content."
                )
                tone = gr.Dropdown(
                    ["Professional", "Casual", "Straightforward", "Confident", "Friendly", "Neutral", 
                     "Storytelling", "Inspirational"], 
                    label="Tone", 
                    info="Select a Tone to set the communication style."
                )
                # Update state when this tab is selected
                tab2.select(lambda: "format_tone", None, active_tab)
            
            btn_submit = gr.Button("Submit")

        # Right Column for Output
        with gr.Column(scale=1):
            results = gr.Textbox(label="Result", lines=16)
    
    btn_submit.click(
        fn=sentence_builder, 
        inputs=[prompt, target_audience, format, tone, active_tab], 
        outputs=[results]
    )

if __name__ == "__main__":
    app.queue(max_size=10).launch()

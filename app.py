import gradio as gr
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
import requests
from PIL import Image
import torch, os, re, json
import spaces

torch.hub.download_url_to_file('https://raw.githubusercontent.com/vis-nlp/ChartQA/main/ChartQA%20Dataset/test/png/74801584018932.png', 'chart_example_1.png')
torch.hub.download_url_to_file('https://raw.githubusercontent.com/vis-nlp/ChartQA/main/ChartQA%20Dataset/val/png/multi_col_1229.png', 'chart_example_2.png')



model = PaliGemmaForConditionalGeneration.from_pretrained("lithi/Chartvision")
processor = AutoProcessor.from_pretrained("lithi/Chartvision")


@spaces.GPU
def predict(image, input_text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    image = image.convert("RGB")

    inputs = processor(text=input_text, images=image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    prompt_length = inputs['input_ids'].shape[1]
    
    # Generate
    generate_ids = model.generate(**inputs, max_new_tokens=512)
    output_text = processor.batch_decode(generate_ids[:, prompt_length:], skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

    return output_text

   
image = gr.components.Image(type="pil", label="Chart Image")
input_prompt = gr.components.Textbox(label="Input Prompt")
model_output = gr.components.Textbox(label="Model Output")
examples = [["chart_example_1.png", "Describe the trend of the mortality rates for children before age 5"],
            ["chart_example_2.png", "What is the share of respondants who prefer Facebook Messenger in the 30-59 age group?"]]

title = "ChartVision"
interface = gr.Interface(fn=predict, 
                         inputs=[image, input_prompt], 
                         outputs=model_output, 
                         examples=examples, 
                         title=title,
                         theme='gradio/soft')

interface.launch()
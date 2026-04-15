import os
import uuid
import gradio as gr
from piper import PiperVoice
import wave

# create outputs folder
os.makedirs("outputs", exist_ok=True)

# load voice
voice = PiperVoice.load("models/en_US-lessac-medium.onnx")

def generate_speech(text):
    if not text.strip():
        return None

    file_name = f"outputs/{uuid.uuid4()}.wav"

    with wave.open(file_name, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    return file_name

# UI
with gr.Blocks() as demo:
    gr.Markdown("# Multilingual TTS Demo")
    gr.Markdown("Type text and generate speech")

    text_input = gr.Textbox(
        label="Enter Text",
        placeholder="Type here..."
    )

    generate_btn = gr.Button("Generate Speech")

    audio_output = gr.Audio(
        label="Generated Audio",
        type="filepath"
    )

    generate_btn.click(
        fn=generate_speech,
        inputs=text_input,
        outputs=audio_output
    )

demo.launch()
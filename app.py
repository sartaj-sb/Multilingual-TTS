import os
import uuid
import wave
import gradio as gr
from piper import PiperVoice

# folders
os.makedirs("outputs", exist_ok=True)

# load voices
voices = {
    "English": PiperVoice.load("models/en_US-lessac-medium.onnx"),
    "Hindi": PiperVoice.load("models/hi_IN-pratham-medium.onnx"),
    "Telugu": PiperVoice.load("models/te_IN-venkatesh-medium.onnx"),
    # "Kannada": PiperVoice.load("models/kn_IN-xxxx-medium.onnx")  # add when downloaded
}

def generate_speech(text, language):
    if not text.strip():
        return None

    file_name = f"outputs/{uuid.uuid4()}.wav"

    voice = voices[language]

    with wave.open(file_name, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    return file_name

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ Multilingual Expressive TTS")
    gr.Markdown("Convert text into natural speech")

    text_input = gr.Textbox(
        label="Enter Text",
        placeholder="Type your text here...",
        lines=5
    )

    language_dropdown = gr.Dropdown(
        choices=list(voices.keys()),
        value="English",
        label="Select Language"
    )

    with gr.Row():
        generate_btn = gr.Button("Generate Speech", variant="primary")
        clear_btn = gr.Button("Clear")

    audio_output = gr.Audio(
        label="Generated Audio",
        type="filepath"
    )

    generate_btn.click(
        fn=generate_speech,
        inputs=[text_input, language_dropdown],
        outputs=audio_output
    )

    clear_btn.click(
        fn=lambda: ("", None),
        inputs=[],
        outputs=[text_input, audio_output]
    )

demo.launch()
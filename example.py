import os
from TTS.api import TTS
import gradio as gr


def convert(source_file, target_file):
    print(source_file.name)
    print(target_file.name)
    tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False, gpu=False)
    tts.voice_conversion_to_file(source_wav=source_file.name, target_wav=target_file.name, file_path="output.wav")
    print("Done")
    return "output.wav"

# folder = "/Users/nghind/workspace/data/cv-corpus-14.0-delta-2023-06-23/vi/clips"
# convert(os.path.join(folder, "common_voice_vi_37404546.mp3"), os.path.join(folder, "common_voice_vi_37286600.mp3"))


inputs = [
    gr.inputs.File(type="file", label="Source"),
    gr.inputs.File(type="file", label="Target")

]


def convert(source_audio, target_audio):
    print(source_audio)
    source_audio_path = "source.wav"
    target_audio_path = "target.wav"

    source_audio.save(source_audio_path)
    target_audio.save(target_audio_path)

    tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False, gpu=False)
    output_file_path = "output.wav"

    tts.voice_conversion_to_file(source_wav=source_audio_path, target_wav=target_audio_path, file_path=output_file_path)

    return output_file_path


inputs = [
    gr.inputs.Audio(source="microphone", type="filepath", optional=True, label="Speaker #1"),
    gr.inputs.Audio(source="microphone", type="filepath", optional=True, label="Speaker #2"),
]

output = gr.outputs.Audio(type="filepath", label="Converted Audio")


description = (
    "This demo from Microsoft will compare two speech samples and determine if they are from the same speaker. "
    "Try it with your own voice!"
)
article = (
    "<p style='text-align: center'>"
    "<a href='https://huggingface.co/microsoft/unispeech-sat-large-sv' target='_blank'>🎙️ Learn more about UniSpeech-SAT</a> | "
    "<a href='https://arxiv.org/abs/2110.05752' target='_blank'>📚 UniSpeech-SAT paper</a> | "
    "<a href='https://www.danielpovey.com/files/2018_icassp_xvectors.pdf' target='_blank'>📚 X-Vector paper</a>"
    "</p>"
)
folder = "/Users/nghind/workspace/data/cv-corpus-14.0-delta-2023-06-23/vi/clips"
examples = [
    [os.path.join(folder, "common_voice_vi_37404546.mp3"), os.path.join(folder, "common_voice_vi_37286600.mp3")],
    [os.path.join(folder, "common_voice_vi_37327679.mp3"), os.path.join(folder, "common_voice_vi_37469552.mp3")],
]

interface = gr.Interface(
    fn=convert,
    inputs=inputs,
    outputs=output,
    layout="horizontal",
    allow_flagging=False,
    live=False,
    examples=examples,
    cache_examples=False
)
interface.launch()

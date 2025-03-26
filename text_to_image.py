# -*- coding: utf-8 -*-
"""text to image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/134EZMEcu9c8pPGL1K03-37HI1aAEnF89
"""

import torch
from diffusers import StableDiffusionPipeline

def generate_image(prompt, model_name="runwayml/stable-diffusion-v1-5", output_path="output.png"):
    # Check for GPU availability
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the Stable Diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(model_name)
    pipe.to(device)

    print("Generating image for prompt:", prompt)

    # Generate the image
    image = pipe(prompt).images[0]

    # Save the generated image
    image.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    generate_image(user_prompt)
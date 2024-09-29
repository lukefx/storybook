from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
pipeline.load_lora_weights("alvdansen/littletinies")
# pipe = pipeline.to("mps")


def generate_illustration(text: str):
    picture = pipeline(text).images[0]
    return picture

from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="fal-ai",
    api_key="",
)

with open("retro_cars.png", "rb") as image_file:
   input_image = image_file.read()

# output is a PIL.Image object
image = client.image_to_image(
    input_image,
    prompt="Поверни все машины левым боком",
    model="Qwen/Qwen-Image-Edit",
)

print('a')
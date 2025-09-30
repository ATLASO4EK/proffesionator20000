from diffusers import StableDiffusionPipeline
import torch

class AIagent():
    def __init__(self):
        self.model_id = "prompthero/openjourney"
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        self.base_prompt = "retro se.rie of different cars with different colors and shapes, mdjrny-v4 style"

    def getimg(self, prompt:str, image=None):
        image = self.pipe(self.base_prompt + prompt).images[0]
        return image
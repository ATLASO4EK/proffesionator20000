from config import get_key
from huggingface_hub import InferenceClient

class AIagent():
    def __init__(self):
        self.model = "Qwen/Qwen-Image-Edit"
        self.client = InferenceClient(
            provider="fal-ai",
            api_key=get_key(),
        )

    def getimg(self, prof:str, prof_disc:str, image):
        out_image = self.client.image_to_image(
            image,
            prompt=f"Изобрази как этот человек бы выглядел, если бы его профессия была {prof}, вот немного сведений о ней: {prof_disc}",
            model=self.model,
        )
        return out_image
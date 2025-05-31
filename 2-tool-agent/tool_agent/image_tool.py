from typing import Dict
from vertexai.preview.vision_models import ImageGenerationModel
import base64
import vertexai

# Initialize Vertex AI
vertexai.init(project="adk-rag-project", location="us-central1")

# Load model once
generation_model = ImageGenerationModel.from_pretrained("imagen-4.0-generate-preview-05-20")

def generate_image(prompt: str) -> Dict[str, str]:
    """
    Generate an image using Vertex AI and return it as a base64-encoded PNG.
    """
    images = generation_model.generate_images(
        prompt=prompt,
        number_of_images=1,
        aspect_ratio="1:1",
        add_watermark=False,
    )

    # Convert image to base64 string
    pil_image = images[0]._pil_image.convert("RGB")
    from io import BytesIO
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return {
        "image_base64": img_str,
        "format": "png"
    }

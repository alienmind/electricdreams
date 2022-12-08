import torch
from diffusers import StableDiffusionPipeline
import os
import tempfile
from .hasher import Hasher
import pkg_resources

class Painter:

    # Default image if CUDA not available
    DEFAULT_IMAGE = pkg_resources.resource_string('electricdreams-api', 'img/default.jpg')

    def __init__(self, cache_dir = '/tmp'):
        """
        Initialize painter class. This will set up a SD pipeline, a temporary dir for caching and some other stuff
        """
        # Cache dir
        self.tmpdir = cache_dir

        # Without CUDA we will just return a default image
        if not torch.cuda.is_available():
            self.pipe = None
            return

        # Pipeline
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16,
                                                       use_auth_token = os.getenv('HUGGINGFACE_API_KEY'))
        pipe = pipe.to("cuda")
        self.pipe = pipe

        # Hasher
        self.hasher = Hasher()


    def paint(self, prompt : str):
        imagepath : str = None

        if self.pipe != None:
            hash = self.hasher.sha256(prompt) # The cache entry is given by the prompt hash
            imagepath = self.tmpdir + "/" + hash + ".png"
            if os.path.isfile(imagepath) == False:
                image = self.pipe(prompt).images[0]  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
                # Now to display an image you can do either save it such as:
                image.save(imagepath)
        else:
            imagepath = self.tmpdir + "/default.jpg"
            with open(imagepath,"wb") as f:
                f.write(self.DEFAULT_IMAGE)

        return imagepath

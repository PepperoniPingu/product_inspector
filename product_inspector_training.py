import numpy
from matplotlib import pyplot
from PIL import Image
from pytorch_lightning import Trainer
from torchvision.transforms import ToPILImage

from anomalib.config import get_configurable_parameters
from anomalib.data import get_datamodule
from anomalib.data.utils import read_image
from anomalib.models import get_model
from anomalib.utils.callbacks import LoadModelCallback, get_callbacks


# Load config
CONFIG_PATH = "config_padim.yaml"
config = get_configurable_parameters(config_path = CONFIG_PATH)

# Load training data
datamodule = get_datamodule(config)
datamodule.setup()  # Create train/val/test/prediction sets

# Start training
trainer = Trainer(**config.trainer, callbacks = get_callbacks(config))
trainer.fit(model = get_model(config), datamodule = datamodule)
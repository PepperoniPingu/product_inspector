# Load config
# Load model
# Load inferencer

# Wait for DUT
#   Take picture
#   Analyze
#   Visualize
#   Alarm?
# Repeat

from anomalib.config import get_configurable_parameters
from anomalib.models import get_model
from anomalib.utils.callbacks import get_callbacks
from anomalib.deploy import TorchInferencer
from anomalib.post_processing import Visualizer
from anomalib.data.utils import read_image
from matplotlib import pyplot
from PIL import Image


# Load config
CONFIG_PATH = "config_padim.yaml"
config = get_configurable_parameters(config_path = CONFIG_PATH)

# Lad weights in to inferencer
inferencer = TorchInferencer(path = "./results/padim/mvtec_test/transistor/run/weights/torch/model.pt", device = "auto")

# Test image
image_path = "./datasets/MVTec/bottle/test/broken_large/000.png"
image = read_image(path = "./datasets/MVTec/bottle/test/broken_large/000.png")
prediction = inferencer.predict(image = image)
pyplot.imshow(prediction.anomaly_map)
pyplot.show()
from pytorch_lightning import Trainer
from anomalib.config import get_configurable_parameters
from anomalib.data import get_datamodule
from anomalib.models import get_model
from anomalib.utils.callbacks import LoadModelCallback, get_callbacks


# Load config
CONFIG_PATH = "config_padim.yaml"
config = get_configurable_parameters(config_path = CONFIG_PATH)

# Load training data
datamodule = get_datamodule(config)
datamodule.setup()  # Create train/val/test/prediction sets

# Start training
model = get_model(config)
trainer = Trainer(**config.trainer, callbacks = get_callbacks(config))
trainer.fit(model = model, datamodule = datamodule)
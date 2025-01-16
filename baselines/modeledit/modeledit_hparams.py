from dataclasses import dataclass
from typing import List

from util.hparams import HyperParams


@dataclass
class ModelEditHyperParams(HyperParams):
    layer_to_modify_until: int
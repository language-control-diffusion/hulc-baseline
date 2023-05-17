import torch
import pytorch_lightning as pl
from typing import Any


class Dummy(pl.LightningModule):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.dummy = torch.nn.Parameter(torch.tensor(0.0))
        self.register_buffer("plan", torch.zeros((256, 64, 7)))  # [batch_size, horizon, action_dim]

    def training_step(self, *args, **kwargs):
        self.log("training/loss", 0.0, on_step=True)
        pass

    def validation_step(self, *args, **kwargs):
        pass

    def get_plan(self, *args, **kwargs):
        return self.plan

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())

    def reset(self):
        pass

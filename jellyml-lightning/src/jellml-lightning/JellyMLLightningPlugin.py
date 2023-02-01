from pytorch_lightning.plugins import TorchCheckpointIO
import jellyml


class JellyMLLightningPlugin(TorchCheckpointIO):
    """
    Save a snapshot of the model with the checkpoint.
    Snapshot is created when the Plugin is initialized.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.snapshot = jellyml.create_snapshot(*args, **kwargs)

    def save_checkpoint(self, checkpoint, path, storage_options):
        super().save_checkpoint(checkpoint=checkpoint | self.snapshot,
                                path=path, storage_options=storage_options)

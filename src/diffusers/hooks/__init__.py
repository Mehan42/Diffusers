from ..utils import is_torch_available


if is_torch_available():
    from .layerwise_casting import apply_layerwise_casting, apply_layerwise_casting_hook

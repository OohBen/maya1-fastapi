"""Device detection utilities for PyTorch with MPS (Mac) support."""
import torch


def get_optimal_device() -> str:
    """
    Detect the best available device for PyTorch operations.

    Priority order: CUDA (NVIDIA) > MPS (Apple Silicon) > CPU

    Returns:
        str: Device string ("cuda", "mps", or "cpu")
    """
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"


def get_device_info() -> dict:
    """
    Get detailed information about available devices.

    Returns:
        dict: Device information including type, count, and capabilities
    """
    info = {
        "device": get_optimal_device(),
        "cuda_available": torch.cuda.is_available(),
        "mps_available": torch.backends.mps.is_available(),
    }

    if info["cuda_available"]:
        info["cuda_device_count"] = torch.cuda.device_count()
        info["cuda_device_name"] = torch.cuda.get_device_name(0) if torch.cuda.device_count() > 0 else None

    return info

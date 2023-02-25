# @title ## 2.1. Download ControlNet Model
from pathlib import Path
import os
import subprocess

model_dir = Path("./models")
model_dir.mkdir(exist_ok=True)


modelUrl = [
    "",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_canny.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_depth.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_hed.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_mlsd.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_normal.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_openpose.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_scribble.pth",
    "https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_seg.pth",
]
modelList = [
    "",
    "control_sd15_canny",
    "control_sd15_depth",
    "control_sd15_hed",
    "control_sd15_mlsd",
    "control_sd15_normal",
    "control_sd15_openpose",
    "control_sd15_scribble",
    "control_sd15_seg",
]
installModels = ["control_sd15_canny", "control_sd15_hed", "control_sd15_scribble"]

hf_token = os.environ["HF_TOKEN"]
user_header = f'"Authorization: Bearer {hf_token}"'


def install(checkpoint_name):
    url = modelUrl[modelList.index(checkpoint_name)]
    ext = "pth" if url.endswith(".pth") else "pt"

    command = (
        f"aria2c --console-log-level=error "
        + f"--summary-interval=10 --header={user_header} "
        + "-c -x 16 -k 1M -s 16 -d ./models "
        + f'-o {checkpoint_name}.{ext} "{url}"'
    )
    subprocess.call(command, shell=True)


mandatory = [
    "body_pose_model.pth",
    "dpt_hybrid-midas-501f0c75.pt",
    "hand_pose_model.pth",
    "mlsd_large_512_fp32.pth",
    "mlsd_tiny_512_fp32.pth",
    "network-bsds500.pth",
    "upernet_global_small.pth",
]


for model in mandatory:

    command = (
        "aria2c --console-log-level=error --summary-interval=10 --header={user_header} "
        + "-c -x 16 -k 1M -s 16 -d ./annotator/ckpts "
        + f"-o {model} "
        + f"https://huggingface.co/lllyasviel/ControlNet/resolve/main/annotator/ckpts/{model}"
    )
    print(model)
    subprocess.call(command, shell=True)


# for model in installModels:
#     install(model)

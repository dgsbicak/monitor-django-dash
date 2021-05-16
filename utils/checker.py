import os

DISK_SPACE_LEFT_THRESH=float(os.environ.get("DISK_SPACE_LEFT_THRESH"))

def disk_space_filled(diskspaceleft) -> bool:
    return diskspaceleft < DISK_SPACE_LEFT_THRESH
import os
import datetime
import string
import random


def get_file_name(filepath):
    size = 8
    chars = string.ascii_uppercase + string.digits
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    name = ''.join(random.choice(chars) for _ in range(size))
    return name, ext


def upload_image_path(instance, filename):
    date = datetime.datetime.now()
    name, ext = get_file_name(filename)
    new_name = f"{name}{ext}"
    return f"{type(instance).__name__}/{date.year}/{date.month}/{date.day}/{new_name}"


def upload_video_path(instance, filename):
    date = datetime.datetime.now()
    name, ext = get_file_name(filename)
    new_name = f"{name}{ext}"
    return f"videos/{date.year}/{date.month}/{date.day}/{new_name}"

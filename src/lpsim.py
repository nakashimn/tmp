import os
import sys
import re
import argparse
import glob
import datetime
import json
from tqdm import tqdm
import numpy as np
import pandas as pd
import cv2
from PIL import Image, ImageDraw, ImageFont
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import traceback


def parse(label):
    p_str_jp = re.compile("[^0-9\-·]+")
    p_number = re.compile("[0-9\-·]+")
    branch, purpose = p_str_jp.findall(label)
    cls_numbers, numbers = p_number.findall(label)
    lpinfo = {
        "branch": branch,
        "cls_numbers": cls_numbers,
        "purpose": purpose,
        "numbers": numbers
    }
    return lpinfo


label = "なにわ300あ33-40"
lpinfo = parse(label)

fm.findSystemFonts()
font_path = "/usr/share/fonts/truetype/migmix/migmix-1p-regular.ttf"
font_prop = fm.FontProperties(fname=font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name()

img = 255*np.ones([165, 330, 3]).astype(np.uint8)
# plt.text(60, 50, lpinfo["branch"], fontsize=40)
# plt.text(190, 50, lpinfo["cls_numbers"], fontsize=40)
# plt.text(20, 120, lpinfo["purpose"], fontsize=30)
# plt.text(80, 140, lpinfo["numbers"], fontsize=80)
# plt.axis("off")

# plt.imshow(img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(img_rgb)
pil_draw = ImageDraw.Draw(pil_img)
font = ImageFont.truetype(font_path, 40)
pil_draw.text([165, 40], lpinfo["branch"]+" "+lpinfo["cls_numbers"], font=font, fill=(0,0,0), anchor="mm")
font = ImageFont.truetype(font_path, 30)
pil_draw.text([40, 110], lpinfo["purpose"], font=font, fill=(0,0,0), anchor="mm")
font = ImageFont.truetype(font_path, 80)
pil_draw.text([190, 110], lpinfo["numbers"], font=font, fill=(0,0,0), anchor="mm")


img_lp = np.array(pil_img)

plt.imshow(img_lp)
plt.axis("off")

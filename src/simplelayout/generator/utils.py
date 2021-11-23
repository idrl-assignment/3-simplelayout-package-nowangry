"""
辅助函数
"""

import os
# from pathlib import Path
# import matplotlib.pyplot as plt
import scipy.io as sio
from PIL import Image
import numpy as np


def save_matrix(matrix, file_name):
    # TODO: 存储 matrix 到 file_name.mat, mdict 的 key 为 "matrix"
    sio.savemat(file_name + ".mat", {"matrix": matrix})


def save_fig(matrix, file_name):
    # TODO: 将 matrix 画图保存到 file_name.jpg
    image = Image.fromarray(np.uint8(matrix * 255)).convert('1')
    image.save(file_name + ".jpg")


def make_dir(outdir):
    folder = os.path.exists(outdir)
    if not folder:
        os.makedirs(outdir)
        print("---  new folder: {}  ---".format(outdir))
    else:
        print("---  Folder existed: {} ---".format(outdir))

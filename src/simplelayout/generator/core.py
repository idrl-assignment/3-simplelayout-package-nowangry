"""
数据生成的主要逻辑
"""

import numpy as np
# from numpy.matrixlib.defmatrix import matrix


def generate_matrix(
        board_grid: int, unit_grid: int, unit_n: int, positions: list
) -> np.ndarray:
    """生成指定布局矩阵
    Args:
        board_grid (int): 布局板分辨率，代表矩形区域的边长像素数
        unit_grid (int): 矩形组件分辨率
        unit_n (int): 组件数
        positions (list): 每个元素代表每个组件的位置
    Returns:
        np.ndarray: 布局矩阵
    """
    # TODO: 实现布局矩阵的生成
    length = board_grid // unit_grid
    Matrix = np.zeros((board_grid, board_grid))
    for i in range(unit_n):
        x = ((positions[i] - 1) // length) * unit_grid
        y = ((positions[i] - 1) % length) * unit_grid

        Matrix[x:x+length, y:y+length] = 1
        # for j in range(length):
        #     for k in range(length):
        #         Matrix[x + j][y + k] = 1

    return Matrix

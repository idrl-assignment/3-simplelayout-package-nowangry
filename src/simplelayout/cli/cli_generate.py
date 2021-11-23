import sys
import argparse
import os
from simplelayout.generator.utils import make_dir


def get_options():
    parser = argparse.ArgumentParser()
    # TODO: 按 1-simplelayout-CLI 要求添加相应参数
    parser.add_argument("--board_grid", type=int,
                        help="布局板分辨率，代表矩形区域的边长像素数")
    parser.add_argument("--unit_grid", type=int,
                        help="矩形组件分辨率；要求 board_grid 能整除 unit_grid，若不满足退出程序")
    parser.add_argument("--unit_n", type=int, help="组件数")
    parser.add_argument("--positions", type=int, nargs="+",
                        help="数量与 unit_n 一致；代表每个组件的位置编号，位置为从1开始的整数，\
                            上限为 (board_grid/unit_grid)^2 ，若不满足要求退出程序")
    parser.add_argument("-o", "--outdir", type=str,
                        help="输出结果的目录，默认为当前目录下的 example_dir \
                            目录；若目录不存在程序会自行创建，支持跨平台路径")
    parser.add_argument("--file_name", type=str,
                        help="输出文件名（不包括文件类型后缀），默认为 example")
    args = parser.parse_args()

    if not args.board_grid % args.unit_grid == 0:
        print("not args.board_grid % args.unit_grid == 0:")
        sys.exit(1)
    if not args.unit_n == len(args.positions):
        print("not args.unit_n == len(args.positions):")
        sys.exit(1)
    for i in range(args.unit_n):
        if not (args.positions[i] >= 1 and args.positions[i] <=
                (args.board_grid / args.unit_grid) ** 2):
            print("not (args.positions[i] >= 1 and args.positions[i] <= \
                (args.board_grid / args.unit_grid)**2):")
            sys.exit(1)

    make_dir(args.outdir)
    file1 = open(os.path.join(args.outdir, args.file_name + ".jpg"), 'w')
    file1.close()
    file2 = open(os.path.join(args.outdir, args.file_name + ".mat"), 'w')
    file2.close()
    return args

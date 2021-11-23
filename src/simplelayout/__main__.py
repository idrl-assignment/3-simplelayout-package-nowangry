# TODO 正确导入函数 generate_matrix, save_matrix, save_fig
import os
from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入
from simplelayout.generator.core import generate_matrix
from simplelayout.generator.utils import save_matrix, save_fig


def main():
    print("hello world")
    options = get_options()
    print(options)

    matrix = generate_matrix(board_grid=options.board_grid,
                             unit_grid=options.unit_grid,
                             unit_n=options.unit_n,
                             positions=options.positions)
    save_matrix(matrix, os.path.join(options.outdir,
                                     options.file_name))
    save_fig(matrix, os.path.join(options.outdir,
                                  options.file_name))


if __name__ == "__main__":
    main()

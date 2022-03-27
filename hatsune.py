import argparse
import sys
import pathlib

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def parse_arguments():
    parser = argparse.ArgumentParser('\'hatsune\' image color component (scatter plot) visualizer')
    parser.add_argument('--input', '-i', type=str, required=True, help='Input image path')
    exclusive_group = parser.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument('--show', '-s', action='store_true', help='Display a figure')
    exclusive_group.add_argument('--output', '-o', type=str, help='Output figure path')
    return parser.parse_args()


def main(args):
    input = pathlib.Path(args.input).resolve()
    if not input.exists():
        raise Exception(f'{input} is not found')

    # read original image with alpha channel
    hatsune = cv2.imread(str(input), cv2.IMREAD_UNCHANGED)
    # f**k bgr
    hatsune = cv2.cvtColor(hatsune, cv2.COLOR_BGRA2RGBA)

    # flatten
    hatsune_one_dim = hatsune.reshape(-1, 4)
    # remove transparency
    hatsune_one_dim = hatsune_one_dim[hatsune_one_dim[:, 3] != 0]
    # truncate alpha channel
    hatsune_one_dim = hatsune_one_dim[:, 0:3]

    hatsune_pd = pd.DataFrame(hatsune_one_dim, columns=['Red', 'Green', 'Blue'])
    # count duplicate rows(pixels) and sort in descending order
    hatsune_pd = hatsune_pd.pivot_table(columns=['Red', 'Green', 'Blue'], aggfunc=np.size).reset_index(name='Size').sort_values('Size', ascending=False)

    # DataFrame to ndarray
    rgbs = hatsune_pd[['Red', 'Green', 'Blue']].to_numpy(dtype=np.uint8)
    ss = hatsune_pd['Size'].to_numpy(dtype=np.uint32)
    rs = rgbs[:, 0]
    gs = rgbs[:, 1]
    bs = rgbs[:, 2]
    # rgb list to html hex str, [2:] is removing '0x'
    cs = ['#' + hex((rgb[0] << 16) + (rgb[1] << 8) + rgb[2])[2:].zfill(6) for rgb in rgbs]

    fig = plt.figure(figsize=[19.2, 10.8], dpi=96.0)
    plt.rcParams['axes.facecolor'] = 'none'

    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    ax.scatter(rs, gs, bs, c=cs, s=ss, marker='.', depthshade=False)

    output = pathlib.Path(args.output).resolve() if args.output is not None else None
    if output is None or output.exists() or args.show:
        plt.show()
    else:
        plt.savefig(str(output))


if __name__ == '__main__':
    try:
        main(parse_arguments())
    except Exception as e:
        print(f'something is wrong: {e}', file=sys.stderr)

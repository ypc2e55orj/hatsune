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
    parser.add_argument('--output', '-o', type=str, required=False, help='Output figure path')
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

    hatsune_df = pd.DataFrame(hatsune_one_dim, columns=['Red', 'Green', 'Blue'])
    # count duplicate rows(pixels) and sort in descending order
    hatsune_df = hatsune_df.pivot_table(columns=['Red', 'Green', 'Blue'], aggfunc=np.size).reset_index(name='Size').sort_values('Size', ascending=False)

    # DataFrame to ndarray
    rgbs = hatsune_df[['Red', 'Green', 'Blue']].to_numpy(dtype=np.uint8)
    ss = hatsune_df['Size'].to_numpy(dtype=np.uint32)
    rs = rgbs[:, 0]
    gs = rgbs[:, 1]
    bs = rgbs[:, 2]
    # rgb list to html hex str list
    cs = [f'#{(r << 16) | (g << 8) | b:06x}' for r, g, b in rgbs]

    fig = plt.figure(figsize=[19.2, 10.8], dpi=96.0)

    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.scatter(rs, gs, bs, c=cs, s=ss, marker='.', depthshade=False)

    output = pathlib.Path(args.output).resolve() if args.output is not None else None
    if output is None or output.exists():
        plt.show()
    else:
        plt.savefig(str(output))


if __name__ == '__main__':
    try:
        main(parse_arguments())
    except Exception as e:
        print(f'something is wrong: {e}', file=sys.stderr)

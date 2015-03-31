#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
import argparse
import logging
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

FRESSIN_DIR = os.path.join(os.environ['WASP'], 'ComparisonWithFressin')
sys.path.insert(0, FRESSIN_DIR)
import fressin


logging.basicConfig(
    level='DEBUG', format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
logger = logging.getLogger(__name__)


def main(args):
    logger.debug(args)

    sns.set(style='white', context='talk')

    colours = sns.color_palette(n_colors=5)

    f = fressin.Fressin(os.path.join(FRESSIN_DIR, 'koi_minus_fp.fits'))

    fig, axis = plt.subplots()
    
    x = np.append(f.x, 50)
    bx = np.array(list(zip(x[:-1], x[1:]))).flatten()
    by = by = np.array(list(zip(f.y, f.y))).flatten()

    lw = 2
    axis.errorbar(f.b, f.y, f.e, ls='None', lw=lw, capsize=0.,
            color=colours[0], marker='.')
    axis.plot(bx, by, color=colours[0], lw=lw)

    axis.set_xscale('log')
    axis.xaxis.set_major_locator(plt.LogLocator(subs=[1, 2, 5]))
    axis.xaxis.set_major_formatter(plt.LogFormatter(labelOnlyBase=False))
    axis.set_xlim(0.6, 12)
    axis.set_ylim(0., 0.004)
    axis.set_xlabel(r'Orbital period / days')
    axis.set_ylabel(r'Number of planets per star')
    axis.grid(True)

    fig.tight_layout()
    fig.savefig(os.path.join(
        os.path.dirname(__file__), '..', 'images', 'plots',
        'fressin-comparison.pdf'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np
from waspselectioneffects.wasp import WASP
import os
import seaborn as sns

logging.basicConfig(
    level='DEBUG', format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
logger = logging.getLogger(__name__)


sns.set(style='white', context='talk')

def main(args):
    w = WASP(filename=os.path.join(
        os.environ['WASP'], 'DistributionAnalyser', 'fields.h5'),
        multiple=2, scale=False)

    fig, axis = plt.subplots()

    colours = sns.color_palette(n_colors=5)
    axis.errorbar(w.b, w.y, w.e, ls='None', marker='.', capsize=0.,
            color=colours[0])
    axis.plot(w.x, w.y, drawstyle='steps-post',
            color=colours[0])

    axis.set_xscale('log')
    axis.set_xlim(0.6, 12)

    axis.xaxis.set_major_locator(plt.LogLocator(subs=[1, 2, 5]))
    axis.xaxis.set_major_formatter(
            plt.LogFormatter(labelOnlyBase=False))

    axis.set_xlabel(r'Orbital period / days')
    axis.set_ylabel(r'Occurrence rate / planets per star')

    axis.grid(True)

    fig.tight_layout()
    fig.savefig(os.path.join(
        os.path.dirname(__file__), '..', 'images', 'plots',
        'occurrence-rate.pdf'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())

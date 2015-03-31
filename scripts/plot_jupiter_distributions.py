#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
import argparse
import logging
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

import seaborn as sns

sns.set(style='white', context='talk', rc={
'font.family': ['sans-serif',],
'font.sans-serif': ['Source Sans Pro', 'Arial'],
'font.monospace': [],
})

logging.basicConfig(
    level='DEBUG', format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
logger = logging.getLogger(__name__)


def main(args):
    logger.debug(args)
    df = pd.read_csv('scripts/data/exoplanets.csv', low_memory=False).drop(0)

    period_ind = (df['PER'] > 0) & (df['PER'] <= 10)
    giant_ind = ((df['R'] >= 0.8) & (df['R'] <= 2.5) |
            (df['MSINI'] >= 0.1) & (df['MSINI'] < 13))

    df = df[giant_ind]

    wasp_ind = df['NAME'].str.contains('WASP')
    wasp = df[wasp_ind]
    rv_ind = df['PLANETDISCMETH'] == 'RV'
    rv = df[rv_ind]
    kepler_ind = df['NAME'].str.contains('Kepler')
    kepler = df[kepler_ind]

    colours = sns.color_palette(n_colors=3)

    fig, axis = plt.subplots()

    lims = (0.6, 10)
    axis.hist([wasp.PER.values, rv.PER.values, kepler.PER.values],
            bins=np.logspace(np.log10(0.68399037867067902),
                np.log10(50), 13),
            histtype='stepfilled', alpha=0.2, label=['WASP', 'RV', 'Kepler'],
            lw=2., edgecolor='k', color=colours)
    axis.hist([wasp.PER.values, rv.PER.values, kepler.PER.values],
            bins=np.logspace(np.log10(0.68399037867067902),
                np.log10(50), 13),
            histtype='step',
            lw=2., color=colours)
    axis.set_xscale('log')
    axis.legend(loc='best')
    axis.xaxis.set_major_locator(plt.LogLocator(subs=[1, 2, 5]))
    axis.xaxis.set_major_formatter(plt.LogFormatter(labelOnlyBase=False))
    axis.set_xlim(0.6, 20)
    axis.set_xlabel(r'Orbital period / days')

    fig.tight_layout()
    fig.savefig(os.path.join(
        os.path.dirname(__file__), '..', 'images', 'plots',
        'giant_planets.pdf'))
    plt.close(fig)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())

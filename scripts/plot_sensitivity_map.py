#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid1 import AxesGrid
import numpy as np
import os
from planetdatabase.waspdatabase import SouthernPublishedDatabase
import astropy.constants as const
import tables

import seaborn as sns

sns.set(style='white', context='talk')

secondsInDay = 86400.
GravConst = const.G.value

def roche_radius(period, mp):
    '''
    Given the period and planetary mass, calculate the radius value
    '''
    period = period * secondsInDay
    mp = mp * const.M_jup.value

    C = 0.46224
    result = C * (((GravConst * mp * period ** 2) / (4. * np.pi ** 2))
            ** (1. / 3.))
    return result / const.R_jup.value

def set_axis_limits(ax):
    ticks = [0.1, 0.2, 0.5, 1, 2, 5, 10]

    period_limits = (0.35, 10)
    radius_limits = (0.3, 6)
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xticks(ticks)
    ax.set_xticklabels(ticks)

    ax.set_yticks(ticks)
    ax.set_yticklabels(ticks)

    ax.set_xlim(*period_limits)
    ax.set_ylim(*radius_limits)


def label_axis(ax):
    ax.set_xlabel(r'Orbital period / days')
    ax.set_ylabel(r'Planetary radius / $\mathrm{R_J}$')


def plot_roche_limits(ax):
    roche_periods = np.linspace(0.35, 10, 10)
    for rp in [roche_radius(roche_periods, mp) for mp in [0.5, 2, 10]]:
        ax.plot(roche_periods, rp, 'w--')

def render_planets(axis):
    wd = SouthernPublishedDatabase()
    population = wd.data()
    (_, _, period, period_up, period_low, radius, radius_up, radius_low) = map(
        np.array, zip(*population))

    axis.errorbar(period, radius, yerr=[radius_low, radius_up],
            xerr=[period_low, period_up], ls='None', capsize=0., lw=2.,
            marker='o', ms=5., color='w', mec='k')


def main():
    outfilename = os.path.join(
            os.path.dirname(__file__),
            '..', 'images', 'plots', 'sensitivitymap{}.pdf')
    data_filename = os.path.expanduser(
            os.path.join(
                '~', 'work', 'WASP', 'DistributionAnalyser', 'fields.h5'))


    with tables.open_file(data_filename) as infile:
        node = infile.root.debug.oriondetectionmap
        period = np.log10(node.period[:])
        radius = np.log10(node.radius[:])
        orion_detection_map = node.map[:]

        node = infile.root.sensitivity.map
        prob = node.prob[:]
        noprob = node.noprob[:]

    period_centres = 10 ** (period + np.diff(period)[0] / 2.)
    radius_centres = 10 ** (radius + np.diff(radius)[0] / 2.)

    cmap = plt.cm.afmhot

    panel_width = 4
    panel_height = 3

    plot_lims = [
            (0, 1),
            (0, 0.8),
            (0, 0.4),
            ]

    for i, (data, lims) in enumerate(zip([orion_detection_map, noprob, prob],
                                    plot_lims)):
        fig, axis = plt.subplots()
        mappable = axis.pcolormesh(period_centres, radius_centres, data,
                vmin=lims[0], vmax=lims[1], cmap=cmap)
        fig.colorbar(mappable, ax=axis)
        set_axis_limits(axis)
        label_axis(axis)
        plot_roche_limits(axis)
        render_planets(axis)
        fig.tight_layout()
        fig.savefig(outfilename.format(i))


if __name__ == '__main__':
    main()

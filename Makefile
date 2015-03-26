all: plots

plots: images/plots/giant_planets.pdf images/plots/occurrence-rate.pdf images/plots/sensitivitymap0.pdf images/plots/sensitivitymap1.pdf images/plots/sensitivitymap2.pdf

images/plots/giant_planets.pdf: scripts/plot_jupiter_distributions.py
	python $<

images/plots/occurrence-rate.pdf: scripts/plot_underlying_distribution.py
	python $<

images/plots/sensitivitymap0.pdf: scripts/plot_sensitivity_map.py
	python $<

images/plots/sensitivitymap1.pdf: scripts/plot_sensitivity_map.py
	python $<

images/plots/sensitivitymap2.pdf: scripts/plot_sensitivity_map.py
	python $<

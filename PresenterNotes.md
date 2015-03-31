# Slides

* Simon Walker
    * Occurrence rate of hot Jupiters
    
* Hot Jupiter sample
    * Pile up noted in hot Jupiter population
        * is this a selection bias? 
    * WASP detected more hot Jupiters than any other project
        * Ideally placed to determine this
    * We insert transits, run the wasp pipeline and study the recovery fraction
        
* Define a sample around which we can make a quantatitive estimate of the underlying period distribution
    * Number of stars increases rapidly towards faint stars
        * only found planets around the bright end
        * restrict our search space to bright stars
    * Planets found mostly around bluer stars
    * Planets found only around dwarfs
        * contours show dwarf probability
        
* Resulting distributions:
    * Mid F to early K stars
        * peaking at early G

* Transit synthesis:
    * unaltered phase folded WASP-12 lightcurve
    * model the transit with Mandel & Agol and remove transit signal
    * insert synthetic transit of WASP-6 b which has much longer period
    
* Insertion model statistics
    * Upper left: number density of inserted transit signals
    * Upper right: track non-transiting models to account for transit probability
    * Lower left: include grazing transits
    * Numbers at the top
    
* Transit detection with BLS algorithm
    * We want to ensure we recover what we put in
    * Input period vs recovered period
    * dots everywhere - spurious detections
    * horizontal lines - aliases of one day signals
    * diagonal lines - matches
    * we allow multiple of two aliases: 1/2 and 2
    
* BLS detection efficiency
    * orbital period vs planet radius
    * colour map is the detection probability
        * vertical drops as hard coded rejection points around one and a half days
        * black region upper left - planets reached roche limit and disintegrated
            * diagonal lines are this for 0.5, 2, 10 MJ
        * white dots - planets
        * drop in sensitivity towards long periods and low radii

* Apply false positive rejection cuts
    * Reduces the absolute sensitivity slightly
    * mostly sharply reduces sensitivity to large planets
        * looking into expanding this cut and searching for extremely inflated planets
        
* Incorporate probability of transit
    * Overall sensitivity drops as $$$P^{-2/3}$$$
    
* Occurrence rate
    * Pile up moves further out
    
* and is real

* RV sample from Butler showed pile up in 2006
    * non-uniform sample
    * small sample
    
* Uniform RV sample from Mayor
    * very small numbers
   
* Howard 
    * Modest evidence for pile up
    * low numbers
    * KOIs so false positive questions
    
* Fressin
    * no sign of pile up
    
* Model as power law with Gaussian excess
    * characteristic period at 3.9 days
    * use Howard occurrence rate to constrain longer period
    * modelled free incompleteness factor normalising the two data sets

* Interpretation
    * characteristic circularisation inner edge at twice the roche limit
   
* Disc migration
    * planet migrates inward in disc until its outer lindblad resonant point falls within truncated inner edge of disk
    * this is located at twice the orbital period of the planet
        * and matches stellar rotation period
    * 4 day period would lead to spin period of young stars corresponding to 8 days
    
* Summary
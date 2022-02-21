# special_extras

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VChristiaens/special_extras/master?filepath=binder%2Fwelcome.ipynb)


> additional material for [special](https://github.com/VChristiaens/special)


## [Tutorials](./tutorials)

A walkthrough tutorial in the form of a Jupyter notebook can be found in the `tutorials/` folder. They can be visualized directly here on GitHub (by just clicking on them), or using the nbviewer service.

> [GitHub](./tutorials/walkthrough.ipynb) / [nbviewer](http://nbviewer.jupyter.org/github/VChristiaens/special_extras/blob/master/tutorials/walkthrough.ipynb) / [binder](https://mybinder.org/v2/gh/VChristiaens/special_extras/master?filepath=tutorials%2Fwalkthrough.ipynb)

This tutorial covers:

- loading the test dataset;
- calculating a spectral correlation matrix (e.g. for use in spectral fits involving IFS measurements);
- using the MCMC (emcee) sampler to infer posterior distributions on spectral model parameters;
- using the nested (nestle) sampler to infer posterior distributions on spectral model parameters;
- finding the best-fit spectral template in a given library, with 2 free parameters (scaling and extinction).


## [Datasets](./datasets)

The data used in the tutorial are located in the `datasets/` folder, and correspond to the J1900-3645 b/B (aka. CrA-9 b/B) spectrum acquired from VLT/SPHERE-IFS, VLT/SPHERE-IRDIS and VLT/NACO high-contrast imaging data presented in [Christiaens et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.6117C/abstract).


## [Models and templates](./static)

For the purpose of the tutorial, we only use a fraction of the BT-SETTL model grid [(Allard et al. 2012)](https://ui.adsabs.harvard.edu/abs/2012RSPTA.370.2765A/abstract) spanning effective temperatures of 2000 K to 4000 K. 
We also downloaded the full Montreal Spectral Library of low-mass dwarf template spectra.
Both the model grid and the template library are placed in the `static/` folder.



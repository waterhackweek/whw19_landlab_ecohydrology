# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:41:01 2019

@author: keckj
"""

import matplotlib.pyplot as plt
import numpy as np
import os as os
import pandas as pd

from landlab import RasterModelGrid
from landlab.components import FlowDirectorSteepest, TransportLengthHillslopeDiffuser, LinearDiffuser, FlowDirectorD8
from landlab.components import StreamPowerEroder, FlowRouter, PrecipitationDistribution, FlowAccumulator
from landlab import imshow_grid
from landlab.io.esri_ascii import write_esri_ascii
from landlab.io import read_esri_ascii
from landlab.io.netcdf import read_netcdf
 
from mpl_toolkits.mplot3d import Axes3D


os.chdir('D:/UW_PhD/dhsvm/projects/b694/gis/python/')

#load existing landscape
(mg, z) = read_esri_ascii('D:/UW_PhD/dhsvm/projects/b694/gis/python/b694_clip.asc', name='topographic__elevation')

#view existing landscape
plt.figure('topo')
imshow_grid(mg,z,grid_units=('m','m'),var_name='Elevation(m)',plot_name = 'test')
#plt.ylim([0,3000])
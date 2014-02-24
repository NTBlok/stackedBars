"""
@author: NTBlok
 
This function uses python libraries, numpy and matplotlib. It also imports a list of rgb color values using rgb_uniqColors.py that should be saved to the same directory. 
A new png file will be saved with default filename, newChart.png to the same directory.
 
#Example syntax:
import stackedBars as ch1
help(ch1)
ch1.stackedBars(ch1.x_vector,ch1.y_labels,ch1.rgb_alpha,ch1.y_matrix,ch1.title,ch1.xlabel,ch1.ylabel,yAxis_max=None,filename=None,rgb_colorList = None)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  #This needs to be called before pyplot is imported if running on server (w/o X server) to prevent RuntimeError: Invalid DISPLAY variable
 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

import rgb_uniqColors as rgb 
 
values = [x for x in range(4)]
jet = cm = plt.get_cmap('jet')
cNorm  = colors.Normalize(vmin=0, vmax=values)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
blackColor = (0.,0.,0.,1.)
 

rgb_colorList = rgb.rgb_uniq
rgb_alpha = 0.8

import random

def randomColors(n):
 rand_index = []
 while len(rand_index)<n:
  r = random.randint(0,len(rgb_colorList)-1)
  if r not in rand_index: rand_index.append(r)
 rand_rgb = [rgb_colorList[i] for i in rand_index]
 return rand_rgb

def transformColorList(colorList,alpha):
 colors = []
 for rgb in colorList:
  rd = int(rgb.split()[0])
  gn = int(rgb.split()[1])
  bl = int(rgb.split()[2])
  rgb_tuple = (rd/255.,gn/255.,bl/255.,alpha)
  colors.append(rgb_tuple)
 return colors

 
####Example data BEGIN
x_vector = np.array([0,31,61,91,123])  #t0 at M2 and following thru M6
 
y_labels = ['US', 'CAN',  'EUR', 'JAP', 'Asia', 'India', 'CAR',  'S Pac', 'S Amer']
 
y_M2     = [350,    0,      0,  0   ,   0 ,  0  ,     0,     0,    0]
y_M3     = [318,   15 ,     20 ,  5  ,   3 ,   10  ,     2,     1,   2]
y_M4     = [ 302,   9,     10 ,  7  ,   4 ,   0  ,     0,     0,   1]
y_M5     = [ 225,   9,     3 ,  9  ,    5,   0  ,      0,   0 ,    0]
y_M6     = [ 213,  11,     3 ,  10 ,   4 ,    1 ,     1 ,   1 ,    0]
y_matrix = np.array([y_M2,y_M3, y_M4, y_M5, y_M6])
 
title = "Software XYZ Downloads\n by Region over Time"
xlabel = 'Days'
ylabel = 'Number of Downloads'
#####Example data END


def stackedBars(x_vector,y_labels,rgb_alpha,y_matrix,title,xlabel,ylabel,yAxis_max=None,filename=None,rgb_colorList=None):
 if rgb_colorList is None:
   n = len(y_labels); colorList = randomColors(n)
   colors = transformColorList(colorList,rgb_alpha)
 else:  colors = transformColorList(rgb_colorList,rgb_alpha)
 if filename is None: filename="newChart.png"
 wideArray = y_matrix
 array_T = wideArray.transpose()
 (rows,cols) = array_T.shape
 for n in range(rows):
   exec("vector_t%i = array_T[%i]" %(n,n))
 fig = plt.figure()
 ax = fig.add_subplot(111)
 bar_width = 10.0
 bar_t0 = plt.bar(x_vector-5, vector_t0, bar_width, color = colors[0])
 rhs = "vector_t0"
 for i in range(1,rows):
  if i >= 2: rhs = rhs + " + vector_t%i" %(i-1)
  exec("bar_t%i = plt.bar(x_vector-5, vector_t%i, bar_width, color = colors[%i], bottom = %s)" %(i,i,i,rhs))
 ax.set_xticks(x_vector)
 ax.set_xticklabels(x_vector)
 barsTxt = "bar_t0[0]"
 for i in range(1,rows):
  barsTxt = barsTxt + " , bar_t%i[0]" %(i)
 yLabelsTxt = "y_labels[0]"
 for i in range(1,rows):
  yLabelsTxt = yLabelsTxt + " , y_labels[%i]" %(i)
 exec("plt.legend((%s),(%s))" %(barsTxt,yLabelsTxt))
 if yAxis_max is None:
  sums = y_matrix.sum(axis=1)
  yAxis_max = int(round(max(sums/50.))*50.)
 plt.ylim(0,yAxis_max)
 plt.xlim(-10,x_vector[4]+60)
 plt.title(title) #"New Auto Policy Households as of October 2011\n Tracking Policy Category over Time")
 plt.xlabel(xlabel) #'Days')
 plt.ylabel(ylabel) #'Number of Households')
 exec("fig.savefig('%s')" %(filename))
 return fig
 

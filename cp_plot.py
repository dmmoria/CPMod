# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:57:11 2020

@author: dmmoria
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})


def millions(x, pos):
    return '${}M'.format(int(x*1e-6))

def thousands(x,pos):
    return '${}k'.format(int(x*1e-3))

def make_labels(max_value, cp_quantiles):
    if max_value < 10**6:
        cp_quantiles_thousands = cp_quantiles/(10**3)
        cp_quantiles_formatted = cp_quantiles_thousands.apply(lambda x:"${:,.1f}k".format(x))
        formatter = FuncFormatter(thousands)
    else:
        cp_quantiles_millions = cp_quantiles/(10**6)
        cp_quantiles_formatted = cp_quantiles_millions.apply(lambda x:"${:,.2f}M".format(x))
        formatter = FuncFormatter(millions)
    return formatter, cp_quantiles_formatted
        
def create_text_percentile(index,cp_quantiles):
    text_percentile_func = lambda percent: "{}{}".format(percent,"tsnrhtdd"[(np.floor(index/10)%10!=1)*(percent%10<4)*percent%10::4])
    text_percentile_formatted = text_percentile_func(int(100*index))
    text_percentile = " {} percentile: {}".format(text_percentile_formatted, cp_quantiles.loc[index])
    return text_percentile    

def consequence_potential_plot(consequence_potential,quantiles):
    cp_min = consequence_potential.min()
    cp_max = consequence_potential.max()
    cp_quantiles = consequence_potential.quantile(quantiles).astype(int)

    formatter, cp_quantiles_formatted = make_labels(cp_max, cp_quantiles)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for index, value in cp_quantiles.items():
        text_percentile = create_text_percentile(index,cp_quantiles_formatted)
        ax.plot([cp_min,value],[index,index],'k--') 
        ax.text(cp_min,
                index+0.01,
                text_percentile, 
                va='bottom',
                fontsize=8)
    kwargs = {'cumulative': True}
    sns.distplot(consequence_potential, hist_kws={'cumulative':False}, kde_kws=kwargs)
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlabel('Consequence Probability')
    ax.set_ylabel('Probability')
    plt.xlim(cp_min,cp_max)
    plt.savefig('Consequence_Potential.png', dpi=300)
    
    
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
# For use with Seaborn 0.11.0 - not yet part of standard Anaconda distribution     
# def consequence_potential_ridgeplot(cp_data, s):
#     pal = sns.cubehelix_palette(10, rot=-0.25, light=0.7)
#     g = sns.FacetGrid(cp_data, row="category", hue="category", aspect=15, height=0.5, palette=pal)
    
#     g.map(sns.kdeplot, "data", bw_adjust=.5, clip_on=False, fill=True, alpha=1, linewidth=1.5)
#     g.map(sns.kdeplot, "data", clip_on=False, color="w", lw=2, bw_adjust=.5)
#     g.map(plt.axhline, y=0, lw=2, clip_on=False)
    
#     g.map(label, "data")

#     # Set the subplots to overlap
#     g.fig.subplots_adjust(hspace=-.25)

#     # Remove axes details that don't play well with overlap
#     g.set_titles("")
#     g.set(yticks=[])
#     g.despine(bottom=True, left=True)
#     plt.xlabel("Consequence Potential")
#     plt.savefig('Ridge_plot.png', dpi=300)

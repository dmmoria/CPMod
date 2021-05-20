# -*- coding: utf-8 -*-
"""
__version__ = '0.1'

__copyright__ = Copyright 2019 National Technology & Engineering 
Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 
with NTESS, the U.S. Government retains certain rights in this software.

__license__ = "Revised BSD License"
"""

import numpy as np
import scipy.stats as stats
import pandas as pd
import cp_calcs as calc
import cp_tools as tls
import cp_plot as plt_tls

np.random.seed(12345)


def calc_consequence_potential():
    global s, inputs, scenarios_ind, scenarios_dep, scenarios_all, data, cp_totl, data_with_categories, data_summed_by_category, data_category_stacked
    inputs = tls.import_cp_inputs
    scenario_num = 1000
    inputs = tls.import_cp_inputs()
    scenarios_ind = calc.calc_cp_independent(inputs, scenario_num).transpose()
    scenarios_dep = calc.calc_cp_dependent(inputs, scenario_num).transpose()
    scenarios_all = scenarios_ind.append(scenarios_dep)
    data = pd.concat([inputs,scenarios_all],axis=1)
    
    cp_totl = scenarios_all.sum()
   
    data_with_categories = data.drop(['dependence','dist_type','value','mean_value','std_dev','min','max'],axis=1)
    data_summed_by_category = data_with_categories.groupby(['category']).sum()
    
    s = data_summed_by_category.sum(axis=1).sort_values().index.tolist()
    
    data_summed_by_category = data_summed_by_category.reindex(s)
    
    data_category_stacked = data_summed_by_category.stack()
    data_category_stacked = data_category_stacked.to_frame()
    data_category_stacked = data_category_stacked.rename(columns={0:"data"})
    data_category_stacked = data_category_stacked.reset_index()
    
    plt_tls.consequence_potential_plot(cp_totl, [0.10, 0.50, 0.90])
    plt_tls.consequence_potential_ridgeplot(data_category_stacked, s)

def main():
    #import_inputs()
    consequence_potential = calc_consequence_potential() # dollars
    
    quantiles = [0.25]
    #cm_plot.consequence_potential_plot(consequence_potential, quantiles)
    return consequence_potential

if __name__ == "__main__":
    consequence_potential = main()
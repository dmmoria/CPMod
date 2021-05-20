#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:52:28 2020

@author: dmmoria
"""
import numpy as np
import pandas as pd
import scipy.stats as stats

import cp_params as params




### CALCULATIONS FOR DEPENDENT CONSEQUENCE POTENTIALS ###
def get_unique_groups(inputs):
    unique_groups = inputs.dependence.unique()
    return unique_groups

def separate_dependent_cp(cp_inputs):
    cp_dependent = cp_inputs[cp_inputs['dependence'].notna()]
    return cp_dependent

def make_percentile_for_ppf(num_scenario):
    percentile = np.random.uniform(size=num_scenario)
    return percentile

def ppf_value(value,scenario_num):
    dist = pd.Series(value, index=np.arange(scenario_num))
    return dist

def ppf_uniform(q, value_min, value_max):
    loc = value_min
    scale = value_max - value_min
    dist = stats.uniform.ppf(q, loc, scale)
    return dist

def ppf_normal(q, mean, std_dev):
    loc = mean
    scale = std_dev
    dist = stats.norm.ppf(q, loc, scale)
    return dist

def calc_cp_dependent(inputs, scenario_num):
    cp_dependent = separate_dependent_cp(inputs) 
    unique_groups = get_unique_groups(cp_dependent)
    VARS_EXCL = params.get_excel_vars()
    scenarios_dep = pd.DataFrame()
    for group in unique_groups:
        q = make_percentile_for_ppf(scenario_num)  
        # Select consequence potentials in the same group
        cp_dependent_group = cp_dependent.loc[cp_dependent[VARS_EXCL['NAME_COLUMN_DEPENDENCE']] == group]
        for index, row in cp_dependent_group.iterrows():
            if row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_VALUE']:
                # get parameter (value) from group
                value = cp_dependent_group.loc[
                                               index.
                                               VAR_EXCL['NAME_DIST_VALUE']
                                               ]
                # calculate scenarios
                scenarios_dep[index] = ppf_value(value, scenario_num)
            elif row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_UNIFORM']:
                # get parameters from group
                value_min = cp_dependent_group.loc[
                                                   index, 
                                                   VARS_EXCL['NAME_DIST_UNIFORM_MIN']
                                                   ]
                value_max = cp_dependent_group.loc[
                                                   index, 
                                                   VARS_EXCL['NAME_DIST_UNIFORM_MAX']
                                                   ]
                scenarios_dep[index] = ppf_uniform(q, 
                                                   value_min, 
                                                   value_max
                                                   )
            elif row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_NORMAL']:
                value_mean = cp_dependent_group.loc[
                                                    index, 
                                                    VARS_EXCL['NAME_DIST_NORMAL_MEAN']
                                                    ]
                value_std = cp_dependent_group.loc[
                                                   index, 
                                                   VARS_EXCL['NAME_DIST_NORMAL_STD']
                                                   ]
                scenarios_dep[index] = ppf_normal(q,
                                                  value_mean,
                                                  value_std)
            else:
                print('something went wrong... (dependent scenario)')   
    return scenarios_dep
    



### CALCULATIONS FOR INPENDENT CONSEQUENCE POTENTIALS ###
def create_distribution_value(value, num_trials):
    dist = pd.Series(value, index=np.arange(num_trials))
    return dist

def create_distribution_uniform(value_min, value_max, num_trials):
    dist_numpy = np.random.uniform(value_min, 
                                   value_max, 
                                   num_trials
                                   )
    dist = pd.Series(data=dist_numpy)
    return dist
    
def create_distribution_normal(value_mean, value_std, num_trials):
    dist_numpy = np.random.normal(loc=value_mean, 
                                  scale=value_std, 
                                  size=num_trials
                                  )
    dist = pd.Series(data=dist_numpy)
    return dist 

def separate_independent_cp(cp_inputs):
    cp_independent = cp_inputs[cp_inputs['dependence'].isna()]
    return cp_independent
            
def calc_cp_independent(inputs, scenario_num):
    cp_independent = separate_independent_cp(inputs)   
    VARS_EXCL = params.get_excel_vars()
    scenarios_ind = pd.DataFrame()
    for index, row in cp_independent.iterrows():
        if row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_VALUE']:
            value = cp_independent.loc[
                                       index, 
                                       VARS_EXCL['NAME_DIST_VALUE']
                                       ]
            scenarios_ind[index] = create_distribution_value(
                                                             value, 
                                                             scenario_num
                                                             )
        elif row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_UNIFORM']:
            value_min = cp_independent.loc[
                                           index, 
                                           VARS_EXCL['NAME_DIST_UNIFORM_MIN']
                                           ]
            value_max = cp_independent.loc[
                                           index, 
                                           VARS_EXCL['NAME_DIST_UNIFORM_MAX']
                                           ]
            scenarios_ind[index] = create_distribution_uniform(
                                                               value_min, 
                                                               value_max, 
                                                               scenario_num
                                                               )
        elif row[VARS_EXCL['NAME_COLUMN_TYPE']] == VARS_EXCL['NAME_DIST_NORMAL']:
            value_mean = cp_independent.loc[
                                            index, 
                                            VARS_EXCL['NAME_DIST_NORMAL_MEAN']
                                            ]
            value_std = cp_independent.loc[
                                           index, 
                                           VARS_EXCL['NAME_DIST_NORMAL_STD']
                                           ]
            scenarios_ind[index] = create_distribution_normal(
                                                              value_mean, 
                                                              value_std, 
                                                              scenario_num
                                                              )
        else:
            print('something went wrong... (independent scenario)')   
    return scenarios_ind
    
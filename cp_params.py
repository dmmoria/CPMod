# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:13:03 2020

@author: dmmoria
"""

### VARIABLE NAMES ###
def get_workbook_name():
    NAME_WORKBOOK = 'Consequence_of_Failure_Inputs_Test.xlsx'
    return NAME_WORKBOOK

def get_excel_vars():
    VARS_EXCL = {
                 # Excel Column Names
                 'NAME_COLUMN_TYPE':'dist_type',
                 'NAME_COLUMN_DEPENDENCE':'dependence',
                 
                 # Constant Value Names
                 'NAME_DIST_VALUE':'value',
                 
                 # Uniform Distribution Names
                 'NAME_DIST_UNIFORM':'uniform',
                 'NAME_DIST_UNIFORM_MIN':'min',
                 'NAME_DIST_UNIFORM_MAX':'max',
                 
                 # Normal Distribution Names
                 'NAME_DIST_NORMAL':'normal',
                 'NAME_DIST_NORMAL_MEAN':'mean_value',
                 'NAME_DIST_NORMAL_STD':'std_dev'
                 }
    return VARS_EXCL
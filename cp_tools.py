# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:04:04 2020

@author: dmmoria
"""
import pandas as pd
import cp_params as params

### IMPORT DATA FROM EXCEL ###
def import_cp_inputs():
    NAME_WORKBOOK = params.get_workbook_name()
    inputs = pd.read_excel(NAME_WORKBOOK,
                           header=1,
                           index_col=0
                           )
    return inputs
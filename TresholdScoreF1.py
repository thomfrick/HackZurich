#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:34:48 2019

@author: tbr
"""

import numpy as np
from sklearn.metrics import confusion_matrix, f1_score

def TresholdScore(value, prediction, treshold, plot_flag):
    """
    arg: value(numpy.array): measured values
         prediction(numpy.array): predicted values 
         treshold(float): class treshold
         plot_flag(boolean): score print or not
         
    return: f1(float): f1-score
    """
    
    treshold_array = np.ones(points)*treshold
    
    value_full = np.greater(value, treshold_array )
    prediction_full = np.greater(prediction, treshold_array )

    cm = confusion_matrix(value_full, prediction_full)
    tn, fp, fn, tp = cm.ravel()
    f1 = f1_score(value_full, prediction_full)
    
    if plot_flag == True:
        print("true positive: ", tp, "\t false positive: ", fp, "\t true negative: ", tn, "\t false negative: ", fn)
        print("f1-score: %1.3f" % f1)
    
    return f1






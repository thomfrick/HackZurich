#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:34:48 2019

@author: tbr
"""

import numpy as np
import matplotlib.pylab as plt

#%% generate data
    
day_points = int(60/5*24)
week_days = 7
week_points = day_points * week_days
weeks = 10
points = day_points * week_days * weeks

n = np.linspace(0, points, points+1)
x = np.linspace(0, week_days*weeks*np.pi, points+1)
mu, sigma = 0, 0.1 # mean and standard deviation

week_factor = np.concatenate((np.ones((week_days-1)*day_points)*0.8, np.ones(1*day_points)))
weeks_factor = week_factor
for i in range(0,weeks-1):
    weeks_factor = np.concatenate((weeks_factor, week_factor))
weeks_factor = np.concatenate((weeks_factor, np.ones(1)))

value = np.sin(x)
value = np.square(value)
value = value * weeks_factor

prediction = value * 0.8
prediction = np.roll(prediction, -50)

noise =  np.random.normal(mu, sigma, points+1)
value = value + noise
#noise =  np.random.normal(mu, sigma*1.5, points+1)
#prediction = prediction + noise

plt.plot(n, value, n, prediction)
plt.xlabel('Day')
plt.ylabel('Value')
plt.axis('tight')
plt.show()


#%%

def CI_interval(value, prediction):  
    day_points = int(60/5*24)
    week_days = 7
    week_points = day_points * week_days
    weeks = len(value)/(day_points*week_days) #
    points = day_points * week_days * weeks
    
    window_weeks = 6 #for mean, std analyzis
    
    na = np.zeros(window_weeks*week_points)
    mean = np.empty(0)
    std = np.empty(0)
    
    position = window_weeks * week_points
    
    while position < len(value)-1:
        error = np.empty(0)
        for m in range(0,window_weeks):
            error_position = position - week_points * (m+1)
            error = np.append(error, prediction[error_position] - value[error_position])
        mean = np.append(mean, error.mean())
        std = np.append(std, error.std())
        position = position +1
    
    mean = np.concatenate((na, mean))  
    std = np.concatenate((na, std))  
    mean = np.append(mean,mean[-1])
    std = np.append(std,std[-1])
    
    N = 12 #winow size for CI smoothing
    mean_smooth = np.convolve(mean, np.ones((N,))/N, mode='same')
    std_smooth = np.convolve(std, np.ones((N,))/N, mode='same')
    
    CI_upper = -mean_smooth+std_smooth+prediction
    CI_lower = -mean_smooth-std_smooth+prediction
    
    return CI_upper, CI_lower

#%%

CI_upper, CI_lower = CI_interval(value, prediction)    

plt.plot(n, value, n, prediction, alpha=1)
plt.plot(n, CI_upper, n, CI_lower, alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Value')
plt.xlim(19000, 20000)
plt.legend(('value', 'prediction', 'CI_upper', 'CI_lower'))
plt.show()



    






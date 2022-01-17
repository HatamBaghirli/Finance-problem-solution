#!/usr/bin/env python
# coding: utf-8
    The local newspaper, Stavanger Aftenblad, ran an article on September 4th about one of
the long-time top managers in Equinor, Margareth Øvrum, who is about to retire at age 62. When she
was 32, Øvrum became the first female platform manager in Statoil. Since then she has held a number
of top management jobs in the company and since 2004 she has been a member of the company’s
executive management team reporting directly to the managing director. Her current job is as
managing director of Equinor Brazil.

    According to the newspaper, the present value at the end of 2019 of Øvrum’s lifetime retirement
pension was NOK 69 million. According to NAV1, life expectancy for a woman born in 1958 is about 88
years.
    The Norwegian State’s Pension Fund use an annual discount rate of 4%2 to calculate the value of the
pension fund (assume annual compounding).

a) Given the information above, what will be the size of Øvrum’s monthly pension when she
begins her retirement in January 2020?
b) Use Python to do a sensitivity analysis to evaluate what her monthly pension will be for
discount rates between 0 and 5%. Graph your results.
# In[1]:


import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from scipy import stats
from scipy import optimize
from scipy.optimize import differential_evolution
from scipy import interpolate
import warnings


# In[2]:


Years = np.arange(10)
NetCashFlows = np.zeros(10)
NetCashFlows[0] = 500
NetCashFlows[1] = 300
NetCashFlows[2] = 100
NetCashFlows[3] =-2400
NetCashFlows[4] = 200
NetCashFlows[5] = 200
NetCashFlows[6] = 200
NetCashFlows[7] = 350
NetCashFlows[8] =350
NetCashFlows[9] =350
fig_NCF = px.bar(x=Years, y=NetCashFlows, labels={'x':'Time (year)','y':'Net Cash Flows (k USD)'})
fig_NCF.show()


# In[3]:


def PW(i,n,p_0,p_1,p_2):
    return p_0+p_1*(((1+i)**n-1)/(i*(1+i)**n))+p_2/(1+i)**n
def fun_NPV(NetCashFlows, Years, DiscountRate):
    DiscountFactors = 1/(1+DiscountRate)**Years
    DiscountedNetCashFlows = NetCashFlows*DiscountFactors
    NPV = np.sum(DiscountedNetCashFlows)
    return NPV


# In[4]:


rate_array = np.linspace(start=0,stop=1,num=1001)
PW_array = []
for DiscountRate in rate_array:
    PW = fun_NPV(NetCashFlows, Years, DiscountRate)
    PW_array.append(PW)


# In[5]:


fig_PW = px.line(x=rate_array, y=PW_array, labels={'x':'Discount Rate','y':'Present Worth (k USD)'})
fig_PW.show()


# In[6]:


WARR = 0.08
NPV = fun_NPV(NetCashFlows, Years, WARR)
print(NPV)


# In[7]:


def fun_MIRR(years_p, NCF_p, rate_reinv, years_n, NCF_n, rate_fin):
    n_years = max(np.array([max(years_p),max(years_n)]))
    PV_n = fun_NPV(NCF_n, years_n, rate_fin)
    PV_p = fun_NPV(NCF_p, years_p, rate_reinv)
    FV_p = PV_p*(1+rate_reinv)**n_years
    MIRR = (FV_p/(-PV_n))**(1/n_years)-1
    return MIRR


# In[9]:


years_p = np.array([1,2,3,4,5,6,7,8,9,10])
NCF_p = np.array([500,300,100,-2400,200,200,200,350,350,350])
rate_reinv = 0.08
years_n = np.array([1,10])
NCF_n = np.array([500,300,100,-2400,200,200,200,350,350,350])


# In[ ]:





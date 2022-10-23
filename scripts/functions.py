#!/usr/bin/env python
# coding: utf-8

# # Lab | Customer Analysis Functions
# 

# In[131]:


import pandas as pd
import numpy as np


# In[133]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# #### Deal with NaN values

# In[134]:


def deal_nan(entry_dataframe):
    for col in entry_dataframe.columns:
        if entry_dataframe[col].dtype == 'object':
            entry_dataframe[col].fillna('No answer', inplace = True)
        else:
            entry_dataframe[col].fillna(value=entry_dataframe[col].mean(), inplace = True)
    return entry_dataframe            


# #### Standarize columns names

# In[135]:


def stand_col_labels(entry_dataframe):
    entry_dataframe.columns = entry_dataframe.columns.str.lower()
    entry_dataframe.columns = entry_dataframe.columns.str.replace (" ", "_")
    return entry_dataframe


# #### Plot hist and boxplot

# In[136]:


def uni_analysis(entry_dataframe, var):
    plt.figure(figsize = (10,3))
    plt.suptitle(var, fontsize=12)

    plt.subplot2grid((1,2), (0,0))
    plt.hist(entry_dataframe[var],
             bins='sturges',
             ec='orangered',
             color='navajowhite')
    plt.title('Histogram', fontsize = 8)
    plt.xlabel(var, fontsize = 10)
    
    plt.subplot2grid((1,2), (0,1))
    plt.boxplot(entry_dataframe[var],
                patch_artist=True,
                showmeans=True,widths=0.6,
                boxprops=dict(facecolor='navajowhite'),
                medianprops=dict(color='orangered',linewidth=2),
                flierprops=dict(marker='o',markerfacecolor='red'),
                meanline=True,
                labels=[var])
    plt.title('Boxplot', fontsize = 8)
    #plt.show()


# #### Distributions

# In[137]:


def uni_distrib(entry_num_dataframe):
    fig, axs = plt.subplots(4, 2, figsize = (10, 10))
    for i in range(4):
        for j in range(2):
            curr_column = entry_dataframe.columns[(i*2) + j]
            sns.distplot(entry_dataframe[curr_column],
            hist=True, 
            kde=True,
            ax=axs[i,j], 
            bins=20, 
            #color = 'darkblue', 
            #hist_kws={'edgecolor':'black'},
            kde_kws={'linewidth': 1})
            #axs[i,j].set_title(curr_column)


# #### Correlations

# In[138]:


def corr_func(entry_dataframe, var='Person'):
    if (var=='Pearson'):
        return entry_dataframe.corr()
    elif (var=='Spearman'):
        return entry_dataframe.corr('Spearman')
    else:
        return entry_dataframe.corr('kendall')


# #### Visualizations

# In[1]:


def plot_data(
    X,
    y,
    alpha=1.0,
    xlim=None,
    ylim=None,
    legend=True,
    cmap=None,
    aspect="equal",
    ax=None,
):
    if ax is None:
        fig, ax = plt.subplots()

    ax.set_aspect(aspect)

    # Plot the features matrix X (with labels):
    scatter = ax.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        s=50,
        ec="black",
        alpha=alpha,
        cmap=cmap,
    )

    if legend:
        # Add a legend with the unique classes:
        handles, labels = scatter.legend_elements(markeredgecolor="black")
        ax.legend(handles, labels, title="Classes")

    # Add labels:
    ax.set_xlabel("$x_{1}$")
    ax.set_ylabel("$x_{2}$")
    ax.set_title("X: Original data")

    # Set limits:
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim);


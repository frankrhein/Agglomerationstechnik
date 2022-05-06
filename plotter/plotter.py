# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:05:56 2021

@author: Frank Rhein
"""
import matplotlib.pyplot as plt
    
# ----------------------------------
# Define Plot defaults
# ----------------------------------
# scl_a4 define scaling of given figuresize 
    # 2: half page figure. Generate additional margin for legend.
    # 1: full page figure. Generate additional margin for legend.
# page_lnewdth_cm: Linewidth of document in cm
# scl: Additional font scaling
# fnt: Font type used in plot
# figsze: Figure size in inches
# frac_lnewdth: Additional scaling option to width = frac_lnewith*document_linewidth
# mrksze: Markersize
# lnewdth: Linewidth (of lines used in plot)
# use_locale: If True use local number format
def plot_init(scl_a4=1,page_lnewdth_cm=16.5,scl=1,fnt='Latin Modern Roman',figsze=[6.4,4.8],frac_lnewdth=0.6,mrksze=6,lnewdth=1.5,use_locale=False):
    
    # --- Initialize defaults ---
    plt.rcdefaults()
    
    # --- Scale figure ---
    # 2: Half page figure
    if scl_a4==2:     
        fac=page_lnewdth_cm/(2.54*figsze[0]*2) #2.54: cm --> inch
        figsze=[figsze[0]*fac,figsze[1]*fac]
    
    # 2: Full page figure
    elif scl_a4==1:
        fac=page_lnewdth_cm/(2.54*figsze[0]) #2.54: cm --> inch
        figsze=[figsze[0]*fac,figsze[1]*fac]
    
    # 3: Scaling for presentations (OLD)
    elif scl_a4==3:
        fac=page_lnewdth_cm/(2.54*figsze[0]) #2.54: cm --> inch
        figsze=[figsze[0]*fac,figsze[1]*fac]
        scl=1.6
        
    # 4: Scaling for variable fraction of linewidth frac_lnewdth
    elif scl_a4==4:
        fac=frac_lnewdth*page_lnewdth_cm/(2.54*figsze[0])
        figsze=[figsze[0]*fac,figsze[1]*fac]
    
    # --- Adjust legend ---
    plt.rc('legend',fontsize=10*scl,fancybox=True, shadow=False,edgecolor='k',
           handletextpad=0.2,handlelength=1,borderpad=0.2,
           labelspacing=0.2,columnspacing=0.2)
    
    # --- General plot setup ---
    plt.rc('mathtext', fontset='cm')
    plt.rc('font', family=fnt)
    plt.rc('xtick', labelsize=8*scl)
    plt.rc('ytick', labelsize=8*scl)
    plt.rc('axes', labelsize=10*scl, linewidth=0.5*scl)
    plt.rc('legend', fontsize=10*scl)
    plt.rc('axes', axisbelow=True) # Grid lines in Background
    plt.rcParams['lines.markersize']=mrksze
    plt.rcParams['hatch.linewidth']=lnewdth/2
    plt.rcParams['lines.linewidth']=lnewdth     
    plt.rcParams['figure.figsize']=figsze
    
    if use_locale: plt.rc('axes.formatter',use_locale=True)

# ----------------------------------
# Actual plot function
# ----------------------------------    
# x: x-Data
# y: y-Data
# err: (optional) Error data
# fig: (optional) Plot in given fig. Create new if None
# ax: (optional) Plot in given ax. Create new in None
# plt_type: Type of Plot
    # Default: Points with lines
    # 'scatter': Scatter without lines
    # 'bar': Bar plot
    # 'line': Line plot   
# lbl: (optional) Label of given Dataset (legend entry)
# xlbl: (optional) Label of x-axis
# ylbl: (optional) Label of y-axis
# mrk: (optional) Marker type, defaul 'o'
# lnstyle: (optional) Linestyle, default '-'
# clr: (optional) Color of plot, default 'k'
# tit: (optional) Title of plot
# grd: (optional) Set grid, default 'major. For no grid use None
# grd_ax: (optional) Define axis for grid, defaul 'both'
# leg: (optional) Bool. Define if legend is plotted, default True
# leg_points_only: (optional) Bool. If True only marker are plottet in legend 
# barwidth: (optional) Width of bar plot
# hatch: (optional) Hatch of bar plot
# alpha: (optional) Alpha of plot
# err_clr: (optional) Color of error bars, If None (default) use plot color
# zorder: (optional) Z-Order of plot. Higher values plotted above lower values
# mrkedgecolor: (optional) Edgecolor of marker
# mrkedgewidth: (optional) Width of marker edge
def plot_data(x,y,err=None,fig=None,ax=None,plt_type=None,lbl=None,xlbl=None,ylbl=None,
              mrk='o',lnstyle='-',clr='k',tit=None,grd='major',grd_ax='both',leg=True,
              leg_points_only=False,barwidth=0.5,hatch=None,alpha=1,err_clr=None,zorder=None,
              mrkedgecolor=None,mrkedgewidth=0.5):
    
    # --- If fig is not given by user: create new figure --- 
    if fig == None:
        fig=plt.figure()
    
    # --- If ax is not given create new axis on figure (only reasonable if fig==None also) ---
    if fig == None or ax == None:    
        ax=fig.add_subplot(1,1,1)
    
    # --- Plot data according to plt_type ---
    # --- Scatter ---
    if plt_type == 'scatter':  
        if mrkedgecolor == None:
            ax.scatter(x,y,label=lbl,marker=mrk,color=clr,zorder=zorder)
        else:
            ax.scatter(x,y,label=lbl,marker=mrk,color=clr,zorder=zorder,edgecolor=mrkedgecolor,linewidths=mrkedgewidth)
    
    # --- Bar ---
    elif plt_type == 'bar':    
        ax.bar(x,y,width=barwidth,label=lbl,color=clr,edgecolor='k',alpha=alpha,hatch=hatch,zorder=zorder,linewidth=plt.rcParams['hatch.linewidth'])
    
    # --- Line ---
    elif plt_type == 'line':
        # NOTE: If only line is plotted increase default linewidth by 50%
        ax.plot(x,y,label=lbl,linestyle=lnstyle,color=clr,linewidth=1.5*plt.rcParams['lines.linewidth'],zorder=zorder)
    
    # --- Default: Marker and Lines ---
    else:
        # --- Plot scatter first to show up in legend ---
        if leg_points_only: 
            if mrkedgecolor == None:
                ax.scatter(x,y,label=lbl,marker=mrk,color=clr,zorder=zorder)
                ax.plot(x,y,marker=mrk,linestyle=lnstyle,color=clr,zorder=zorder)
            else:
                ax.scatter(x,y,label=lbl,marker=mrk,color=clr,zorder=zorder,edgecolor=mrkedgecolor,linewidths=mrkedgewidth)
                ax.plot(x,y,marker=mrk,linestyle=lnstyle,color=clr,zorder=zorder,mec=mrkedgecolor,mew=mrkedgewidth)
        else:
            if mrkedgecolor == None:
                ax.plot(x,y,label=lbl,marker=mrk,linestyle=lnstyle,color=clr,zorder=zorder)
            else:
                ax.plot(x,y,label=lbl,marker=mrk,linestyle=lnstyle,color=clr,zorder=zorder,mec=mrkedgecolor,mew=mrkedgewidth)
    
    # --- Plot errorbars if error is given, if no err_color is given use plot color ---
    if err_clr == None: err_clr=clr
    if err is not None:
        ax.errorbar(x,y,yerr=err,fmt='none',color=err_clr,capsize=plt.rcParams['lines.markersize']-2,alpha=0.5,zorder=0)
        
    # --- Set labels, title and grid if given ---
    if xlbl != None: ax.set_xlabel(xlbl)
    if ylbl != None: ax.set_ylabel(ylbl)
    if tit != None: ax.set_title(tit)
    if grd!=None: ax.grid(True,which=grd,axis=grd_ax,alpha=0.5)
    if leg: ax.legend()
    
    # --- return ax and fig ---
    return ax, fig

# ----------------------------------
# Export current plot
# ----------------------------------    
# filename: Path for export. File extension determines format! (.pdf / .png)
# squeeze: Bool. Define if tight layout is used or not, default True
# dpi: DPI value for export. Only relevant for picture formats like .png / .jpg        
def plot_export(filename,squeeze=True,dpi=1000,pad_inch=False):
    
    if squeeze: 
        bb='tight' 
    else: 
        bb=None
    
    if pad_inch: 
        plt.savefig(filename,dpi=dpi,bbox_inches=bb,pad_inches = 0)
    else:
        plt.savefig(filename,dpi=dpi,bbox_inches=bb)

          
        
        
        
        
        
        

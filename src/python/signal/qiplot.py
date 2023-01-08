def plot_ts(ax,t,y,title='',color='#666666',markers_on=[]):
    ax.minorticks_on()
    ax.plot(t,y,'--o',markevery=markers_on,color=color)
    ax.grid(which='both')
    ax.grid(zorder=0)
    ax.grid(which='major', color='white', linestyle='-',alpha=.5)
    ax.grid(which='minor', color='white', linestyle='-',alpha=0.25)
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.set_title(title)

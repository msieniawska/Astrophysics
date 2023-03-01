import numpy as np
import matplotlib.pyplot as plt 
#import astropy.coordinates as coord
#import astropy.units as u
import sys 
import struct


# based on http://balbuceosastropy.blogspot.com/2013/09/the-mollweide-projection.html

def plot_mwd(org):

    tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    tick_labels = np.remainder(tick_labels + 360 + org, 360)
    fig = plt.figure(figsize = (10, 5))
    ax = fig.add_subplot(111, projection = 'mollweide') # possible projections: 'mollweide', 'aitoff', 'hammer', 'lambert'
    sun = np.genfromtxt('Sun_planets_data_position.txt', dtype=[('frame', 'int'), ('gps', 'float'), ('d1','U3'), ('d2','U2'), ('d3','U4'), ('pos1','float'), ('pos2','float'), ('merc_pos1','float'), ('merc_pos2','float'), ('ven_pos1','float'), ('ven_pos2','float'), ('moon_pos1','float'), ('moon_pos2','float'), ('mars_pos1','float'), ('mars_pos2','float'), ('jup_pos1','float'), ('jup_pos2','float'), ('sat_pos1','float'), ('sat_pos2','float'), ('uran_pos1','float'), ('uran_pos2','float'), ('nep_pos1','float'), ('nep_pos2','float')])

    line=int(sys.argv[2]) - 1
#    print line
    data1=sun[line]['d1']
    data2=sun[line]['d2']
    data3=sun[line]['d3']
#    print data1, data2, data3
    sunpos1=sun[line]['pos1']
    sunpos2=sun[line]['pos2']
    mercpos1=sun[line]['merc_pos1']
    mercpos2=sun[line]['merc_pos2']
    venpos1=sun[line]['ven_pos1']
    venpos2=sun[line]['ven_pos2']
    moonpos1=sun[line]['moon_pos1']
    moonpos2=sun[line]['moon_pos2']
    marspos1=sun[line]['mars_pos1']
    marspos2=sun[line]['mars_pos2']
    juppos1=sun[line]['jup_pos1']
    juppos2=sun[line]['jup_pos2']
    satpos1=sun[line]['sat_pos1']
    satpos2=sun[line]['sat_pos2']
    uranpos1=sun[line]['uran_pos1']
    uranpos2=sun[line]['uran_pos2']
    neppos1=sun[line]['nep_pos1']
    neppos2=sun[line]['nep_pos2']
#    print sun[line,2], sun[line,3], sun[line,4]
    tt = data1 + " " + data2 + " " + data3
    ax.set_xticklabels(tick_labels)
    ax.set_title(tt)
    ax.title.set_fontsize(15)
    ax.set_xlabel("RA")
    ax.xaxis.label.set_fontsize(12)
    ax.set_ylabel("Dec")
    ax.yaxis.label.set_fontsize(12)
    ax.grid(True)

# Add ecliptic plane
    eclp = np.genfromtxt('Sun_alpha_delta.txt')

    x = np.remainder(eclp[:,0] + 360 - org, 360) # shift RA values
    ind = x > 180
    x[ind] -= 360    # scale conversion to [-180, 180]
    x = -x    # reverse the scale: East to the left
    ax.scatter(np.radians(x), np.radians(eclp[:,1]), color = 'cornflowerblue')

    if sunpos1 >= 180:
    	sunpos1 = 360 - sunpos1
    else:
	sunpos1 =- sunpos1
    ax.scatter(np.radians(sunpos1 - org), np.radians(sunpos2), color = 'gold', marker = 'o', s = 700, edgecolor = 'black', label = 'Sun')
    if mercpos1 >= 180:
    	mercpos1 = 360 - mercpos1
    else:
	mercpos1 =- mercpos1
    ax.scatter(np.radians(mercpos1 - org), np.radians(mercpos2), color = 'darkgoldenrod', marker = 'o', s = 100, edgecolor = 'black', label = 'Mercury')
    if venpos1 >= 180:
    	venpos1 = 360 - venpos1
    else:
	venpos1 =- venpos1
    ax.scatter(np.radians(venpos1 - org), np.radians(venpos2), color = 'orchid', marker = 'o', s = 200, edgecolor = 'black', label = 'Venus')
    if moonpos1 >= 180:
    	moonpos1 = 360 - moonpos1
    else:
	moonpos1 =- moonpos1
    ax.scatter(np.radians(moonpos1 - org), np.radians(moonpos2), color = 'silver', marker = 'o', s = 500, edgecolor = 'black', label = 'Moon')
    if marspos1 >= 180:
    	marspos1 = 360 - marspos1
    else:
	marspos1 =- marspos1
    ax.scatter(np.radians(marspos1 - org), np.radians(marspos2), color = 'crimson', marker = 'o', s = 200, edgecolor = 'black', label = 'Mars')
    if juppos1 >= 180:
    	juppos1 = 360 - juppos1
    else:
	juppos1 =- juppos1
    ax.scatter(np.radians(juppos1 - org), np.radians(juppos2), color = 'rosybrown', marker = 'o', s = 300, edgecolor = 'black', label = 'Jupiter')
    if satpos1 >= 180:
    	satpos1 = 360 - satpos1
    else:
	satpos1 =- satpos1
    ax.scatter(np.radians(satpos1 - org), np.radians(satpos2), color = 'maroon', marker = 'o', s = 250, edgecolor = 'black', label = 'Saturn')
    if uranpos1 >= 180:
    	uranpos1 = 360 - uranpos1
    else:
	uranpos1 =- uranpos1
    ax.scatter(np.radians(uranpos1 - org), np.radians(uranpos2), color = 'cyan', marker = 'o', s = 250, edgecolor='black', label = 'Uranus')
    if neppos1>=180:
    	neppos1=360-neppos1
    else:
	neppos1=-neppos1
    ax.scatter(np.radians(neppos1-org), np.radians(neppos2), color = 'blue', marker = 'o', s = 250, edgecolor = 'black', label = 'Neptune')
    plt.legend(loc='lower right')



plot_mwd(org = 0)

o=sys.argv[1]
plt.savefig(o+".png", bbox_inches="tight")
#plt.show()

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#mycolors = ["#004249","#0097a7"]
myexplode = [0.2,0]
mylabel = ["SI","NO"]


#y = np.array([84.5,15.5])
#z = np.array([61,39])
#x = np.array([59,41])
w = np.array([58,42])

patches, texts, pcts  = plt.pie(w,explode = myexplode, labels = mylabel,autopct='%.1f%%',wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'})
plt.setp(pcts, color='white', fontweight='bold')
plt.show()
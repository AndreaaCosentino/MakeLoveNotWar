import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("war-deaths.csv")

fig, ax = plt.subplots(3,1)
fig.set_size_inches(11,8)

plt.suptitle("Morti e Feriti nelle Guerre dell'ultimo Secolo (in milioni)", fontsize = 20)

militari = []
for i in df['Militari morti']:

    militari.append(i / 1000000)

civili = []
for i in df['Civili morti']:
    civili.append(i / 1000000)

feriti = []
for i in df['Feriti']:
    feriti.append(i / 1000000)

labels = ["Prima Guerra Mondiale", "Seconda Guerra Mondiale", "Guerra del Vietnam", "Prima Guerra Cecena", "Seconda Guerra Cecena", "Guerra in Afghanistan", "Guerra in Ucraina"]
x = np.arange(len(labels))
width = 0.2

ax[0].bar(x - 0.2, militari, width, label = "Militari morti", color = '#007E0A')
ax[0].bar(x, civili, width, label = "Civili morti", color = '#FFDDD9')
ax[0].bar(x + 0.2, feriti, width, label = "Feriti", color = '#DD331F')
ax[0].legend(loc = 'upper right')
ax[0].set_xticks(x, labels, rotation = 6)

militari = []
counter = 0
for i in df['Militari morti']:
    counter += 1
    if counter > 2:
        militari.append(i / 1000000)

civili = []
counter = 0
for i in df['Civili morti']:
    counter += 1
    if counter > 2:
     civili.append(i / 1000000)

feriti = []
counter = 0
for i in df['Feriti']:
    counter += 1
    if counter > 2:
        feriti.append(i / 1000000)

labels = ["Guerra del Vietnam", "Prima Guerra Cecena", "Seconda Guerra Cecena", "Guerra in Afghanistan", "Guerra in Ucraina"]
x = np.arange(len(labels))
width = 0.2

ax[1].bar(x - 0.2, militari, width, label = "Militari morti", color = '#007E0A')
ax[1].bar(x, civili, width, label = "Civili morti", color = '#FFDDD9')
ax[1].bar(x + 0.2, feriti, width, label = "Feriti", color = '#DD331F')
ax[1].set_xticks(x, labels, rotation = 0)

militari = []
counter = 0
for i in df['Militari morti']:
    counter += 1
    if counter > 3:
        militari.append(i / 1000000)

civili = []
counter = 0
for i in df['Civili morti']:
    counter += 1
    if counter > 3:
     civili.append(i / 1000000)

feriti = []
counter = 0
for i in df['Feriti']:
    counter += 1
    if counter > 3:
        feriti.append(i / 1000000)

labels = ["Prima Guerra Cecena", "Seconda Guerra Cecena", "Guerra in Afghanistan", "Guerra in Ucraina"]
x = np.arange(len(labels))
width = 0.2

ax[2].bar(x - 0.2, militari, width, label = "Militari morti", color = '#007E0A')
ax[2].bar(x, civili, width, label = "Civili morti", color = '#FFDDD9')
ax[2].bar(x + 0.2, feriti, width, label = "Feriti", color = '#DD331F')
ax[2].set_xticks(x, labels, rotation = 0)


plt.show()

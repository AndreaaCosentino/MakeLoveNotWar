import matplotlib.pyplot as plt
import numpy as np
from data import exp_values

COLORS = ["#fef08a", "#fde047", "#eab308", "#a16207", "#713f12", "#4e3524"]

x = np.arange(1980, 2021) # (N,) array-like

fig, ax = plt.subplots(figsize=(10, 7))
ax.stackplot(x, exp_values, labels=["Tutti gli altri", "Germania", "Francia", "Italia", "Regno Unito", "Stati Uniti"], colors=COLORS)
ax.axvline(x=1990, color="red", linestyle="--", label="Fine Germania Ovest")

plt.legend(loc="upper left")
plt.title("Spesa militare paesi NATO (1980-2020)")
plt.show()
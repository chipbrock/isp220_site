import numpy as np
import math
import matplotlib.pyplot as plt
from myst_nb import glue

from matplotlib.widgets import Button, Slider

def gamma(x):
    return np.sqrt(1/(1-(x**2)))

x = np.arange(0,1.0,0.0001)

init_frequency = 1

fig, ax = plt.subplots()
line, = ax.plot(x, gamma(x), lw=2)
ax.set_xlabel('Beta')

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axbeta = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axbeta,
    label='Beta',
    valmin=0,
    valmax=1,
    valinit=init_frequency,
)

def update(val):
    line.set_ydata(gamma(b, freq_slider.val))
    fig.canvas.draw_idle()

freq_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
button.on_clicked(reset)

plt.show()
glue("Gamma",fig, display="False")

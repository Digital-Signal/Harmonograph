import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import RadioButtons, Slider
from matplotlib.collections import LineCollection


def x(a1, f1, p1, d1, a2, f2, p2, d2, tt):
    return a1 * np.sin(tt * f1 + p1) * np.exp(-1 * d1 * tt) + a2 * np.sin(tt * f2 + p2) * np.exp(-1 * d2 * tt)


def y(a3, f3, p3, d3, a4, f4, p4, d4, tt):
    return a3 * np.sin(tt * f3 + p3) * np.exp(-1 * d3 * tt) + a4 * np.sin(tt * f4 + p4) * np.exp(-1 * d4 * tt)


t = np.linspace(0, 100, 10000)

init_A1 = 100
init_A2 = 100
init_A3 = 100
init_A4 = 100

init_f1 = 10
init_f2 = 10
init_f3 = 10
init_f4 = 10

init_p1 = 0
init_p2 = 0
init_p3 = 0
init_p4 = 0

init_d1 = 0.1
init_d2 = 0.1
init_d3 = 0.1
init_d4 = 0.1

lc = None

fig, ax = plt.subplots(figsize=(10, 5))
plt.title("Harmonograph")
line, = ax.plot(x(init_A1, init_f1, init_p1, init_d1, init_A2, init_f2, init_p2, init_d2, t),
                y(init_A3, init_f3, init_p3, init_d3, init_A4, init_f4, init_p4, init_d4, t), color='black')
fig.subplots_adjust(left=0.05, right=0.45)
plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)

A1_slider = Slider(
    ax=fig.add_axes([0.55, 0.9, 0.3, 0.01]),
    label='A1',
    valmin=0,
    valmax=100,
    valinit=init_A1,
)

A2_slider = Slider(
    ax=fig.add_axes([0.55, 0.87, 0.3, 0.01]),
    label='A2',
    valmin=0,
    valmax=100,
    valinit=init_A2,
)

A3_slider = Slider(
    ax=fig.add_axes([0.55, 0.84, 0.3, 0.01]),
    label='A3',
    valmin=0,
    valmax=100,
    valinit=init_A3,
)

A4_slider = Slider(
    ax=fig.add_axes([0.55, 0.81, 0.3, 0.01]),
    label='A4',
    valmin=0,
    valmax=100,
    valinit=init_A4,
)

f1_slider = Slider(
    ax=fig.add_axes([0.55, 0.78, 0.3, 0.01]),
    label='f1',
    valmin=0,
    valmax=50,
    valinit=init_f1,
)

f2_slider = Slider(
    ax=fig.add_axes([0.55, 0.75, 0.3, 0.01]),
    label='f2',
    valmin=0,
    valmax=50,
    valinit=init_f2,
)

f3_slider = Slider(
    ax=fig.add_axes([0.55, 0.72, 0.3, 0.01]),
    label='f3',
    valmin=0,
    valmax=50,
    valinit=init_f3,
)

f4_slider = Slider(
    ax=fig.add_axes([0.55, 0.69, 0.3, 0.01]),
    label='f4',
    valmin=0,
    valmax=50,
    valinit=init_f4,
)

p1_slider = Slider(
    ax=fig.add_axes([0.55, 0.66, 0.3, 0.01]),
    label='p1',
    valmin=0,
    valmax=6.28,
    valinit=init_p1,
)

p2_slider = Slider(
    ax=fig.add_axes([0.55, 0.63, 0.3, 0.01]),
    label='p2',
    valmin=0,
    valmax=6.28,
    valinit=init_p2,
)

p3_slider = Slider(
    ax=fig.add_axes([0.55, 0.60, 0.3, 0.01]),
    label='p3',
    valmin=0,
    valmax=6.28,
    valinit=init_p3,
)

p4_slider = Slider(
    ax=fig.add_axes([0.55, 0.57, 0.3, 0.01]),
    label='p4',
    valmin=0,
    valmax=6.28,
    valinit=init_p4,
)

d1_slider = Slider(
    ax=fig.add_axes([0.55, 0.54, 0.3, 0.01]),
    label='d1',
    valmin=0,
    valmax=1,
    valinit=init_d1,
)

d2_slider = Slider(
    ax=fig.add_axes([0.55, 0.51, 0.3, 0.01]),
    label='d2',
    valmin=0,
    valmax=1,
    valinit=init_d2,
)

d3_slider = Slider(
    ax=fig.add_axes([0.55, 0.48, 0.3, 0.01]),
    label='d3',
    valmin=0,
    valmax=1,
    valinit=init_d3,
)

d4_slider = Slider(
    ax=fig.add_axes([0.55, 0.45, 0.3, 0.01]),
    label='d4',
    valmin=0,
    valmax=1,
    valinit=init_d4,
)

length_slider = Slider(
    ax=fig.add_axes([0.55, 0.42, 0.3, 0.01]),
    label='length',
    valmin=0,
    valmax=25,
    valinit=25,
)

line_width_slider = Slider(
    ax=fig.add_axes([0.55, 0.39, 0.3, 0.01]),
    label='line width',
    valmin=0,
    valmax=2,
    valinit=1,
)

R_line_slider = Slider(
    ax=fig.add_axes([0.55, 0.36, 0.3, 0.01]),
    label='R line',
    valmin=0,
    valmax=1,
    valinit=0,
)

G_line_slider = Slider(
    ax=fig.add_axes([0.55, 0.33, 0.3, 0.01]),
    label='G line',
    valmin=0,
    valmax=1,
    valinit=0,
)

B_line_slider = Slider(
    ax=fig.add_axes([0.55, 0.30, 0.3, 0.01]),
    label='B line',
    valmin=0,
    valmax=1,
    valinit=0,
)

Alpha_line_slider = Slider(
    ax=fig.add_axes([0.55, 0.27, 0.3, 0.01]),
    label='Alpha line',
    valmin=0,
    valmax=1,
    valinit=1,
)

R_background_slider = Slider(
    ax=fig.add_axes([0.55, 0.24, 0.3, 0.01]),
    label='R bg',
    valmin=0,
    valmax=1,
    valinit=1,
)

G_background_slider = Slider(
    ax=fig.add_axes([0.55, 0.21, 0.3, 0.01]),
    label='G bg',
    valmin=0,
    valmax=1,
    valinit=1,
)

B_background_slider = Slider(
    ax=fig.add_axes([0.55, 0.18, 0.3, 0.01]),
    label='B bg',
    valmin=0,
    valmax=1,
    valinit=1,
)

Alpha_background_slider = Slider(
    ax=fig.add_axes([0.55, 0.15, 0.3, 0.01]),
    label='Alpha bg',
    valmin=0,
    valmax=1,
    valinit=1,
)


def update(val):

    global lc
    if lc:
        lc.remove()
        lc = None

    new_t = np.linspace(0, length_slider.val, 10000)
    line.set_linewidth(line_width_slider.val)
    ax.set_facecolor((R_background_slider.val, G_background_slider.val, B_background_slider.val,
                      Alpha_background_slider.val))
    line.set_color((R_line_slider.val, G_line_slider.val, B_line_slider.val, Alpha_line_slider.val))

    x_values = x(A1_slider.val, f1_slider.val, p1_slider.val, d1_slider.val, A2_slider.val, f2_slider.val,
                 p2_slider.val, d2_slider.val, new_t)
    y_values = y(A3_slider.val, f3_slider.val, p3_slider.val, d3_slider.val, A4_slider.val, f4_slider.val,
                 p4_slider.val, d4_slider.val, new_t)
    line.set_xdata(x_values)
    line.set_ydata(y_values)

    fig.canvas.draw_idle()


A1_slider.on_changed(update)
A2_slider.on_changed(update)
A3_slider.on_changed(update)
A4_slider.on_changed(update)
f1_slider.on_changed(update)
f2_slider.on_changed(update)
f3_slider.on_changed(update)
f4_slider.on_changed(update)
p1_slider.on_changed(update)
p2_slider.on_changed(update)
p3_slider.on_changed(update)
p4_slider.on_changed(update)
d1_slider.on_changed(update)
d2_slider.on_changed(update)
d3_slider.on_changed(update)
d4_slider.on_changed(update)
length_slider.on_changed(update)
line_width_slider.on_changed(update)
R_line_slider.on_changed(update)
G_line_slider.on_changed(update)
B_line_slider.on_changed(update)
Alpha_line_slider.on_changed(update)
R_background_slider.on_changed(update)
G_background_slider.on_changed(update)
B_background_slider.on_changed(update)
Alpha_background_slider.on_changed(update)

rax = plt.axes([0.9, 0.3, 0.08, 0.5])
radio = RadioButtons(rax, ('viridis', 'inferno', 'cividis', 'Greys', 'Blues', 'YlGnBu', 'bone', 'winter',
                           'cool', 'RdBu', 'Spectral', 'ocean'))


def color_function(label):

    global lc
    if lc:
        lc.remove()
        lc = None

    new_t = np.linspace(0, length_slider.val, 10000)
    ax.set_facecolor((R_background_slider.val, G_background_slider.val, B_background_slider.val,
                      Alpha_background_slider.val))

    x_values = x(A1_slider.val, f1_slider.val, p1_slider.val, d1_slider.val, A2_slider.val, f2_slider.val,
                 p2_slider.val, d2_slider.val, new_t)
    y_values = y(A3_slider.val, f3_slider.val, p3_slider.val, d3_slider.val, A4_slider.val, f4_slider.val,
                 p4_slider.val, d4_slider.val, new_t)

    dydx = np.gradient(y_values, x_values)
    points = np.array([x_values, y_values]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = plt.Normalize(-1, 1)
    lc = LineCollection(segments, cmap=label, norm=norm)
    ax.add_collection(lc)
    lc.set_segments(segments)
    lc.set_array(dydx)
    lc.set_linewidth(line_width_slider.val)
    fig.canvas.draw_idle()


radio.on_clicked(color_function)

plt.show()
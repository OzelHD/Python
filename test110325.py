import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import IFrame

# Fixing random state for reproducibility
np.random.seed(19680801)


# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Create rain data
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

# Initialize the raindrops in random positions and with
# random growth rates. Here we visualize the first frame
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
rain_drops['size'] = np.full(n_drops, 5)
rain_drops['color'] = np.array([
    (np.random.uniform(0, 0.3), np.random.uniform(0, 0.3), np.random.uniform(0.5, 1), 1)
    for _ in range(n_drops)
])


# TODO: Construct the scatter which we will update during animation
# as the raindrops develop. 
# Note: You need to set the facecolors to be 'none' and line width to be 0.5
sc = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1], s=rain_drops['size'], edgecolors=rain_drops['color'], facecolors='none', linewidth=0.5)

def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (
    np.random.uniform(0, 0.3), np.random.uniform(0, 0.3), np.random.uniform(0.5, 1), 1
    )

    rain_drops['color'][:, 3] = 1
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)
   

    # TODO: Update the scatter collection, with the new colors, sizes and positions.
    # Please directly use the value stored in "rain_drops"
    # Hint: Use the function set_edgecolors(), set_sizes() and set_offsets()
    sc.set_edgecolors(rain_drops['color'])
    sc.set_sizes(rain_drops['size'])
    sc.set_offsets(rain_drops['position'])


# Construct the animation, using the update function as the animation director.
ani = animation.FuncAnimation(fig, update, interval=80, save_count=1000)

# Save the animation as an html file and display here
plt.close()
with open("rain.html","w") as f:
    print(ani.to_jshtml(),file = f)
IFrame(src = "rain.html",width = 1920, height = 1080)


#aus jupyter notebook 
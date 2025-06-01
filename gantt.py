import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd


# Load the data (see section above)
df = pd.read_csv("example.csv", dtype=str)

# Create the labelling for the task blocks (I want to see task dependencies)
df['Labelling'] = np.where(
    df['Dependencies'].isnull(),
    df['Task'],
    df['Task'] + ", Dependencies: " + df["Dependencies"]
)

# Order as I want plotted (will be sorted by 'resource' in plot though)
df = df.sort_values("Start", ascending=False)

# Plot
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Resource",
    text="Labelling",
    hover_name="Resource",
    hover_data={"Resource": False, "Start": True, "Finish": True, "Labelling": False},
    title="Gantt Chart"
)

fig.show()

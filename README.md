# ganttinize

Gantt chart generation using Plotly, following [this Plotly guide](https://plotly.com/python/gantt/)

And then adding some bits.

## Setup
```bash
python -m venv env
source env/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run

This is very barebones, code reads `example.csv`, which defines the tasks to plot
with task names, start dates, finish datee, a list of dependencies (just a text field for now)
and "Resource" (that's humans, to the rest of us).

```bash
python gantt.py
```

## To be added if I remember

- I want to instead define a start date, dependencies and weeks taken for tasks and have the software figure out the task start dates for me.
- If I've gone this far, might as well add a way of editing tasks through a web interface/Dash.

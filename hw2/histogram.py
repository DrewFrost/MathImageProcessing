"""
hw 2 histogram equalization
"""

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import cv2
import numpy as np

"""
missed plotly key and identification
"""


img = cv2.imread("../geneva.tif", 0)
h = img.shape[0]
w = img.shape[1]


def histo():
    histogram = [0 for n in range(256)]
    return histogram


histogram_data = histo()
for i in range(h):
    for j in range(w):
        val = img[i][j]
        histogram_data[val] = histogram_data[val] + 1


cummulative = histo()
density = histo()
size = img.size
for i in range(256):
    density[i] = (histogram_data[i])/(size)
    for j in range(i):
        cummulative[i] = cummulative[i] + density[j]
    cummulative[i] = int(cummulative[i]*255)


histogram_equalized = histo()
for i in range(256):
        histogram_equalized[cummulative[i]] = histogram_equalized[cummulative[i]] + histogram_data[i]

new_img = np.zeros((h,w), np.uint8)

for i in range(h):
    for j in range(w):
        new_img[i][j]=cummulative[img[i][j]]

cv2.imshow('original', img)
cv2.imshow('equalized', new_img)

x0 = histogram_data
x1 = histogram_equalized
trace1 = go.Histogram(
    x=x0,
    opacity=0.8,
    name='Original',    
)
trace2 = go.Histogram(
    x=x1,
    opacity=0.75,
    name='Equalized',
)

data = [trace1, trace2]
# layout = go.Layout()
layout = go.Layout(
    xaxis=dict(
        autorange=True,
    ),
    yaxis=dict(
        autorange=True,
    ),barmode='overlay'
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='overlaid histogram')
cv2.waitKey(0)

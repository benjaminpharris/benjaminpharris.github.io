import sys

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(width=800, height=600, xmin=-2.0, xmax=1.0, ymin=-1.0, ymax=1.0, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    div_time = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        Z = Z**2 + C
        diverged = np.abs(Z) > 2
        div_now = diverged & (div_time == 0)
        div_time[div_now] = i
        Z[diverged] = 2

    return div_time

st.title("🔮 Mandelbrot Explorer")
st.caption("Made with ❤️ and magma")

# Sidebar controls
st.sidebar.header("Parameters")
xmin = st.sidebar.slider("X min", -2.5, 0.0, -2.0, step=0.01)
xmax = st.sidebar.slider("X max", 0.0, 2.0, 1.0, step=0.01)
ymin = st.sidebar.slider("Y min", -2.0, 0.0, -1.0, step=0.01)
ymax = st.sidebar.slider("Y max", 0.0, 2.0, 1.0, step=0.01)
max_iter = st.sidebar.slider("Max Iterations", 10, 500, 100, step=10)
width = st.sidebar.slider("Image Width", 100, 1000, 500, step=50)
height = st.sidebar.slider("Image Height", 100, 1000, 500, step=50)

#ST loading Spinner to wrap fractal - mandlebrot parameters set by ST sliders
with st.spinner("Rendering fractal..."):
    fractal = mandelbrot(
    width=int(width),
    height=int(height),
    xmin=xmin,
    xmax=xmax,
    ymin=ymin,
    ymax=ymax,
    max_iter=int(max_iter)
    )
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(fractal, cmap="magma", extent=[xmin, xmax, ymin, ymax])
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    st.pyplot(fig)


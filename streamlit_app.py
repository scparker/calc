import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title('Calculator')

numerator = st.text_area("numerator", value = "x")
denominator = st.text_area("denominator", value = "1")

xmin = st.slider("xmin", min_value=-100.0, max_value=100.0, value = -30.0)
xmax = st.slider("xmax", min_value=-100.0, max_value=100.0, value = 30.0)

ymin = st.slider("ymin", min_value=-100.0, max_value=100.0, value = -10.0)
ymax = st.slider("ymax", min_value=-100.0, max_value=100.0, value = 10.0)

x = np.arange(xmin, xmax, .01)

try:
    f_numerator = eval(numerator)
    num_valid = True
except:
    num_valid = False

try:
    f_denominator = eval(denominator)
    den_valid = True
except:
    den_valid = False

if num_valid and den_valid:
    fig, ax = plt.subplots()
    ax.plot(x, f_numerator / f_denominator)
    ax.set_xlim((xmin,xmax))
    ax.set_ylim((ymin,ymax))
    ax.grid()
    fig
else:
    if not num_valid:
        "Numerator Not Valid"

    if not den_valid:
        "Demonimator Not Valid"

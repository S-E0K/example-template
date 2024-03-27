import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)


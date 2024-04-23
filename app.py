import base64
import streamlit as st
from PIL import ImageOps, Image
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras

# set title
st.title('Zebrafish malformations classification')

# set header
st.header('Please upload a Zebrafish larvae image')


    # Display the DataFrame as a table with invisible borders
    st.write(df)

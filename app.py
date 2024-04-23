import base64
import streamlit as st
from PIL import ImageOps, Image
import numpy as np
import pandas as pd

import tensorflow as tf

# set title
st.title('Zebrafish malformations classification')

# set header
st.header('Please upload a Zebrafish larvae image')

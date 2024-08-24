import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.write("""
    
    # Exploratory Data Analysis
    
    """)

# Dataset Information and How to Use
st.write("""

## Dataset Information


""")

# Load the Boston housing dataset from the original source
data_url = ".data/benin-melanville.csv"
data = pd.read_csv(data_url)

# Display first 5 elements of the dataset
st.write("## First 5 Elements of the Dataset")
st.write(data.head())

# Calculate correlation between features and targets
correlation = data.corr()

# Plot histogram for correlation
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write("### Correlation between Features and Target")
plt.figure(figsize=(18, 14))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
st.pyplot()


# Explanation of each column
st.write("""
#### Explanation of Each Column

**MFoC**: 'Material-Form-on-Casting',

**MT**: 'Material-Type ', 

**OQ**: 'Order-Quantity',

**ND**: 'Non-Defective', 

**D**: 'Defective', 

**C**: 'C', 

**Si**: 'Si', 

**Mn**: 'Mn', 

**Cr**: 'Cr', 

**P**: 'P', 

**S**: 'S', 

**Cu**: 'Cu',

**Sn**: 'Sn', 

**GS**: 'Grain-Size', 

**BC**: 'Binder-Content', 

**GP**: 'Gas-Permeability',

**CaT**: 'Casting-Time', 

**CoR**: 'Cooling-Rate', 

**CTe**: 'Casting-Temperature', 

**PR**: 'Pouring-Rate',

**PT**: 'Pouring-Temperature', 

**SoT**: 'Solidification -Time ',

**SGSD**: 'Sand-Grain-Size-Distribution', 

**sT**: 'Sand-Temperature', 

**SRR**: 'Sand-Reuse-Rate',

**SF**: 'Sand-Flowability', 

**CQ**: 'Core-Quality', 

**PQ**: 'Pattern-Quality', 

**MQ**: 'Mold-Quality',

**SMC**: 'Sand-Moisture-Content', 

**AMP**: 'Alloy-Melting-Point', 

**ShT**: 'Shakeout-Time',

**MS**: 'Mold-Strength', 

**Cmpt**: 'Compactability', 

**SiS**: 'Silica-Sand', 

**SoD**: 'Severeity-of-Defect'

**DT**: 'Defect-Type'

""")


st.write("""

## Thank you!

**Contributor:** Tadesse Abateneh

""")
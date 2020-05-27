import numpy as np
import matplotlib.pyplot as plt

"""
MSI Mask Shanghai
"""
# Load the data and extract the bands
DEM = np.load("Shanghai/DEM-Region2.npy")
DEM = DEM[-1]
# DEM[DEM > 0.0] = 1
# DEM[DEM < 0.0] = 0

SAR = np.load("Shanghai/SAR-Region2.npy")
SAR = SAR[-1][:, :, 0]
# SAR[SAR > 0.1] = 1
# SAR[SAR < 0.1] = 0

MSI = np.load("Shanghai/MSI-Region2.npy")
blue = MSI[-1][:, :, 1]
green = MSI[-1][:, :, 2]
red = MSI[-1][:, :, 3]
NIR = MSI[-1][:, :, 7]
SWIR1 = MSI[-1][:, :, 10]
SWIR2 = MSI[-1][:, :, 11]

# Decide on an index
PI = ((blue - SWIR2) / (blue + SWIR2))

# Interpolate the index
PI[PI < 0] = 0
PI[PI > 0] = 1

# A = (PI - SAR) / (PI + SAR)

plt.imshow(PI)
plt.show()

plt.imsave("shangai.png", PI)
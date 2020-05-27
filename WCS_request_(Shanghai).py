from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox, DataSource, SHConfig, DataSource
import matplotlib.pyplot as plt
from datetime import timedelta, date
import numpy as np

INSTANCE_ID = '77763d50-1c52-42a9-8850-2a84823362ce'
if INSTANCE_ID:
    config = SHConfig()
    config.instance_id = INSTANCE_ID
else:
    config = None

# Change vector
change_vector_5000pix = [0.5194570000000027, 0.4494460000000018]
change_vector_2000pix = [0.2538370000000043, 0.21265400000000056]


# 2020-04-30
shanghai_coords_1 = [121.382593,
                     31.163285,
                     121.382593 + change_vector_2000pix[0],
                     31.163285 + change_vector_2000pix[1]]


# 2020-04-30
shanghai_coords_2 = [121.550542,
                     30.798554,
                     121.550542 + change_vector_2000pix[0],
                     30.798554 + change_vector_2000pix[1]]

# 2020-04-28
shanghai_coords_3 = [120.696260,
                     30.873884,
                     120.696260 + change_vector_2000pix[0],
                     30.873884 + change_vector_2000pix[1]]

# Test Region
test = [121.550542, 30.798554, 121.58056, 30.85]

# Assign CRS
shanghai_coords_WGS84 = BBox(bbox=shanghai_coords_1, crs=CRS.WGS84)

# Request data from sentinel hub API
wcs_SAR_color_request = WcsRequest(
    data_source=DataSource.SENTINEL1_IW,
    layer='BANDS-S1-IW',
    bbox=shanghai_coords_WGS84,
    time='latest',
    resx="10m",
    resy="10m",
    config=config,
    image_format=MimeType.TIFF_d32f
)
output = wcs_SAR_color_request.get_data()

# Output the file
np.array(output)
np.save("Shanghai/SAR-Region1", output)

# Reload the data and check data dimensions
data = np.load("Shanghai/SAR-Region1.npy")
print(data.shape)

# Quick view
plt.imshow(output[-1][:, :, 1])
plt.show()

print(output)

print(output.shape)


# Aprox 5000 x 5000
# shanghai_coords_2 = [121.550542, 30.798554, 122.069999, 31.248]
import os
import numpy as np
import pandas as pd
from osgeo import gdal
from matplotlib import pyplot as plt
%matplotlib inline

os.chdir(r"\SummerSem\test\test_data")
imgs = [i for i in os.listdir() if i.endswith(".tif")]
print(imgs)

ndv = [arcpy.Describe(arcpy.sa.Raster(each)).noDataValue for each in imgs]
rasterArrays = {}
for img in imgs:
    rast = arcpy.sa.Raster(img)
    try:
        arr0 = arcpy.RasterToNumPyArray(img, nodata_to_value = np.nan)
    except:
        arr0 = arcpy.RasterToNumPyArray(img, nodata_to_value = -1)
    rasterArrays[img] = arr0
    #plt.imshow(arr0, cmap = "hot")
    #plt.title(img)
    #plt.show()

lu001 = arcpy.RasterToNumPyArray(arcpy.sa.Raster('lc2001_small.tif'))
mask = np.where(lu001 == 0, 1, 0 )
plt.imshow(mask, cmap = "hot"); plt.show()
np.sum(mask)

# Masks all the rasters and plots them
# May be not required to do this
masked = {}
for img in imgs:
    rast = arcpy.sa.Raster(img)
    try:
        temp = arcpy.RasterToNumPyArray(img, nodata_to_value = np.nan)
        tempm = np.ma.array(temp, fill_value = np.nan)
        tempm[np.isnan(temp)] = np.ma.masked
    except:
        temp = arcpy.RasterToNumPyArray(img, nodata_to_value = -1)
        tempm = np.ma.array(temp, fill_value = -1)
        tempm[temp == -1] = np.ma.masked
        
    tempm[mask.astype(bool)] = np.ma.masked
    masked[img] = tempm
    
    #plt.imshow(tempm, cmap = "hot")
    #plt.title(img)
    #plt.show()

# Saves masked lu 2001 array to raster
#mlu001 = masked['lc2001_small.tif']
#mluSave = arcpy.NumPyArrayToRaster(mlu001.data, lower_left_corner = ll, y_cell_size = 30, x_cell_size = 30)
#mluSave.save("mlu2001.tif")
#myRaster = arcpy.sa.Raster('lc2001_small.tif')
#ll = arcpy.Point(myRaster.extent.XMin, myRaster.extent.YMin)
#arcpy.env.cellSize = 30
#arcpy.management.GetRasterProperties(myRaster, "CELLSIZEY")

# Creates a mask which will be used to extract wanted values
# Here the mask is for useful position i.e where data to analyze actually is
lu001 = arcpy.RasterToNumPyArray(arcpy.sa.Raster('lc2001_small.tif'), nodata_to_value = 0 )
dlu001 = lu001.ravel()
mask = np.where(dlu001!=0)
plt.imshow(dlu001.reshape(lu001.shape), cmap = "gray"); plt.show()

# converts rasters to one-d arrays and then extracts data from only mask positions
masked = {}
for key, val in rasterArrays.items():
    unraveled = val.ravel()
    
    masked[key] = unraveled[mask]

for each in masked:
    print(masked[each].shape)

df = pd.DataFrame.from_dict(masked)
df.columns = [i.replace(".tif", "") for i in df.columns]
df.head()

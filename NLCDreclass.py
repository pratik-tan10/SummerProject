import arcpy
import os

infolder = r"NLCD\NLCD_s3ia0UdTvcDGRSGRmzuV"
outfolder = r"ReclassifiedNLCD"
arcpy.env.workspace = infolder

rasts = [ii for ii in arcpy.ListRasters("*") if len(ii)==59]
reclassTable = "0 0;11 8;12 10;21 6;22 2;23 2;24 1;31 9;41 5;42 5;43 5;51 10;52 7;71 6;72 10;73 10;74 10;81 6;82 3;90 7;95 7"
inOut=[]
for each in rasts:
    outfile0 = each[:9]+"_reclassified.tif"
    outfile = os.path.join(outfolder, outfile0)
    infile = os.path.join(infolder, each)
    print(f"Reclassifying {each}")
    arcpy.ddd.Reclassify(infile, "Value", reclassTable, outfile, "NODATA")
    
    print(f"{each} reclassified to {outfile0}")

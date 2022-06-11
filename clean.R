library(dplyr)
library(readr)
setwd("/Data/enviroAtlas")

r3pH <- read_csv("R3_Fertilizer_P_kg_ha.csv" , skip = 9, col_names  = NULL, n_max = 1)
r3p <- read_csv("R3_Fertilizer_P_kg_ha.csv" , skip = 10, col_names  = c("HUC_12", "Fertilizer_P_kg_ha"))
r3p <- read_csv("R3_Fertilizer_P_kg_ha.csv" , skip = 10, col_names  = c("HUC_12", "Fertilizer_P_kg_ha"))
r3p <- read_csv("R3_Fertilizer_P_kg_ha.csv" , skip = 10, col_names  = c("HUC_12", "Fertilizer_P_kg_ha"))
head(r3p)

r3nH <- read_csv("R5_SNFA_MEAN.csv" , skip = 9, col_names  = NULL, n_max = 1)
r3n <- read_csv("R5_SNFA_MEAN.csv" , skip = 10, col_names  = c("HUC_12", "SNFA_MEAN"))
head(r3n)


library(httr)
library(sf)
library(terra)

setwd("/Data/LCMS")
boundary <- "/Data/shpfiles/HUC8Boundaries.shp"
bpoly <- st_read(boundary)

yearX <- 1986:1987
#function to download LMCS for conterminous US

lmcsDownload <- function(x){
  murl <- "https://data.fs.usda.gov/geodata/LCMS/LCMS_CONUS_v2021-7_Land_Use_Annual_2021.zip"
  mname <- "LCMS_CONUS_v2021-7_Land_Use_Annual_2021.zip"
  url <- gsub("2021.zip", paste0(x,".zip"), murl)
  name <- gsub("2021.zip", paste0(x,".zip"), mname)
  download.file(url,name)
  name
}

cropR<-function(x){
  raster<-rast(gsub("1985",x, "LCMS_CONUS_v2021-7_Land_Use_Annual_1985/LCMS_CONUS_v2021-7_Land_Use_1985.tif"))
  print("Raster Reading success\n")
  cropped<- crop(raster, ext(bpoly))
  print("Cropping success\n")
  plot(cropped)
  writeRaster(cropped, gsub(".tif","_cropped.tif", gsub("1985",x, "LCMS_CONUS_v2021-7_Land_Use_1985.tif")))
  print("Saved on disk")
}

dnunzip <- function(x){
  zfile<- lmcsDownload(x)
  print("Download Success\n")
  unzip(zipfile <- zfile , exdir = sub(".zip","",zfile))
  print("Unzip successful\n")
  cropR(x)
}

for ( i in 1989:2000){
  dnunzip(i)
}

        

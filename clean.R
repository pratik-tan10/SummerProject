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

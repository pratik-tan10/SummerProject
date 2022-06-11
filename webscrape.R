library(httr)
library(rvest)
wlink <- "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Nepal"

hdoc <- read_html(wlink)
hdoc%>%html_nodes("tbody:nth-child(1)")%>%html_text()->wtext
wtext[2]->w2

cleanr <- function(xw){
  gsub("\n\n",",", xw)->w2
  gsub("\n",",", w2)->w2
  w2
  unlist(strsplit(w2, split = ",")) -> uw2
  uw2[9:length(uw2)][nchar(uw2)>10]->ulw2
  ulw2[!is.na(ulw2)][nchar(ulw2)>2]
  ulw2[grep("–", ulw2)]
}

unlist(lapply(wtext[2:length(wtext)], cleanr))

unlist(strsplit(wtext[2], split = "\n\n\n"))->t
gsub("\n\n",",", t) -> t
trimws(t) -> t
gsub("\n",",", t)->t

strsplit(t, split = ",")->splited
max(unlist(lapply(splited, length)))->maxl

sapply( splited, function(x){
  a = rep("",maxl)
  a[1:length(x)]<-unlist(x)
  a
})->nameMat
data.frame(t(nameMat))

##
extractname <- function(xyz){
  unlist(strsplit(xyz, split = "\n\n\n"))->t
  gsub("\n\n",",", t) -> t
  trimws(t) -> t
  gsub("\n",",", t)->t
  
  strsplit(t, split = ",")->splited
  max(unlist(lapply(splited, length)))->maxl
  max(c(maxl,9))
  
  sapply( splited, function(x){
    a = rep("", maxl)
    a[1:length(x)]<-unlist(x)
    a
  })->nameMat
  data.frame(t(nameMat))[-1,1:5]
}

lapply(wtext[2:8], extractname)->multiDF

idf <- multiDF[[1]]

for ( i in 2:length(multiDF)) {
  idf <- rbind(idf, multiDF[[i]])
}
idf[nchar(idf[,1])>10,1:3]

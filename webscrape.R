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

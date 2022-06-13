library(httr)
library(rvest)
wlink <- "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Nepal"

hdoc <- read_html(wlink)
hdoc%>%html_nodes("tbody:nth-child(1)")%>%html_text()->wtext
wtext[2]->w2

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
idf[nchar(idf[,1])>10,1:3] -> df2clean

colnames(df2clean) <- c("Personal", "Start", "End")

personal <- df2clean$Personal

library(stringr)
personal%>%str_split(pattern = "(?:\\(|\\))") ->personList
sapply(personList, length)==3 ->selector
sapply(personList[selector],
       function(x){
         x[[1]][1:2]
       })

data.frame(t(unlist(personList[2])[1:2]))
m <- length(personList)
matrix(rep(NA, 2*m), nrow = m, ncol = 2) -> nameMat

for (i in 1:length(personList)){
  if (length(personList[[i]])==3){
    nameMat[i,] <- unlist(personList[[i]])[1:2]

  }
}
data.frame(nameMat) -> names
df2clean$Start <- df2clean$Start%>%str_replace(pattern = "\\[.*\\]", "")%>%str_replace(pattern = "(?:c.\\s)", "")
df2clean$End <- df2clean$End%>%str_replace(pattern = "\\[.*\\]", "")%>%str_replace(pattern = "(?:c.\\s)", "")
colnames(names) <- c("PM", "Date")
str_match(names[,2], pattern = '(?:–)((?:\\d){4})')[,2] ->death
str_match(names[,2], pattern = 'born ((?:\\d){4})')[,2] -> birth1
str_match(names[,2], pattern = '((?:\\d){4})–')[,2] -> birth2
birth2[is.na(birth2)] <- birth1[is.na(birth2)]
names$birth <- birth2
names$death <- death
names$Start <- df2clean$Start
names$End <- df2clean$End

names[-c(75,81), -2] ->filteredNames
filteredNames

plot(filteredNames$birth, rep(1, 85), pch = "*")
lines(filteredNames$birth, rep(1, 85))
filteredNames



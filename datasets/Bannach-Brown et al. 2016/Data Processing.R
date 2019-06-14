library(tidyverse)

#read raw data set
Dta_Bannach <- read_delim("Depression-Dataset-SLIM-DevelopmentTrainingSet.txt", delim = "\t")

#change column names and keep only relevant columns
Dta_Bannach <- Dta_Bannach %>%
  rename(id = ID,
         authors = Author,
         title = Title,
         abstract = Abstract,
         included = `Incl(1)/Excl(0)`) %>%
  select(id, authors, title, abstract, included)

#14% inclusion rate
Dta_Bannach %>%
  summarise(inclusion = sum(included)/n())

#write to csv
write_csv(Dta_Bannach, "Bannach-Brown Data.csv")

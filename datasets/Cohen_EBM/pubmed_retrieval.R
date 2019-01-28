# pubmed_retreival.R
#
# Author: Qixiang Fang

require('tidyverse')
require('rentrez')

# Read the data file containing the pubmed IDs of the papers and the labeling decisions
# link to the webpage of the SR: https://dmice.ohsu.edu/cohenaa/systematic-drug-class-review-data.html
# link to the raw data: https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv

fp_data = "https://dmice.ohsu.edu/cohenaa/epc-ir-data/epc-ir.clean.tsv"
# fp_data = "epc-ir.clean.tsv"

docs_labels <- read_tsv(
  fp_data, 
  col_names = c(
    "disease", 'endnoteID', 'pubmedID','abstractLabel', 'articleLabel')
)
dim(table(docs_labels$disease))



#Function to create a data set with the records
#ID, titles, key words, abstracts, authors, inclusion decisions

dataset.create <- function(data) {
  foo.data <- tibble(pubmedID = data$pubmedID, title = NA, keywords = NA, authors = NA, 
                     abstracts = NA, label1 = data$abstractLabel, label2 = data$articleLabel)
  return(foo.data)
}


dataset.fill <- function(data) {
  #pb <- txtProgressBar(min = 1, max = nrow(data), style = 3)
  
  for (i in 1:nrow(data)) {
    foo.id <- data[i, 1]
    foo.query <- parse_pubmed_xml(entrez_fetch(db="pubmed", id=foo.id, rettype="xml"))
    
    foo.title <- str_c(foo.query$title, collapse = '; ')
    if (length(foo.title) > 0) {
      data[i, 2] <- foo.title
    }
    
    foo.keywords <- str_c(foo.query$key_words, collapse = '; ')
    if (length(foo.keywords) > 0) {
      data[i, 3] <- foo.keywords
    }
    
    foo.authors <- str_c(foo.query$authors, collapse = '; ')
    if (length(foo.authors) > 0) {
      data[i, 4] <- foo.authors
    }
    
    foo.abstract <- str_c(foo.query$abstract, collapse = '; ')
    if (length(foo.abstract) > 0) {
      data[i, 5] <- foo.abstract
    }
    
    #setTxtProgressBar(pb, i)
    
    print(paste(i,'/',nrow(data)))
  }
  #close(pb)
  
  return(data)
}



# Export datasets
dir.create("output")


#ACEInhibitors
tibble.ACEInhibitors <- subset(docs_labels, disease == "ACEInhibitors")
create.ACEInhibitors <- dataset.create(tibble.ACEInhibitors)
dataset.ACEInhibitors <- dataset.fill(create.ACEInhibitors)


write_csv(dataset.ACEInhibitors, file.path('output', 'ACEInhibitors.csv'))

table(dataset.ACEInhibitors$label2)


#ADHD
tibble.ADHD <- subset(docs_labels, disease == "ADHD")
create.ADHD <- dataset.create(tibble.ADHD)
dataset.ADHD <- dataset.fill(create.ADHD)

write_csv(dataset.ADHD, file.path('output', 'ADHD.csv'))

#Antihistamines
tibble.Antihistamines <- subset(docs_labels, disease == "Antihistamines")
create.Antihistamines <- dataset.create(tibble.Antihistamines)
dataset.Antihistamines <- dataset.fill(create.Antihistamines)

write_csv(dataset.Antihistamines, file.path('output', 'Antihistamines.csv'))

#AtypicalAntipsychotics
tibble.AtypicalAntipsychotics <- subset(docs_labels, disease == "AtypicalAntipsychotics")
create.AtypicalAntipsychotics <- dataset.create(tibble.AtypicalAntipsychotics)
dataset.AtypicalAntipsychotics <- dataset.fill(create.AtypicalAntipsychotics)

write_csv(dataset.AtypicalAntipsychotics, file.path('output', 'AtypicalAntipsychotics.csv'))

#BetaBlockers
tibble.BetaBlockers <- subset(docs_labels, disease == "BetaBlockers")
create.BetaBlockers <- dataset.create(tibble.BetaBlockers)
dataset.BetaBlockers <- dataset.fill(create.BetaBlockers)

write_csv(dataset.BetaBlockers, file.path('output', 'BetaBlockers.csv'))


#CalciumChannelBlockers
tibble.CalciumChannelBlockers <- subset(docs_labels, disease == "CalciumChannelBlockers")
create.CalciumChannelBlockers <- dataset.create(tibble.CalciumChannelBlockers)
dataset.CalciumChannelBlockers <- dataset.fill(create.CalciumChannelBlockers)

write_csv(dataset.CalciumChannelBlockers, file.path('output', 'CalciumChannelBlockers.csv'))


#Estrogens
tibble.Estrogens <- subset(docs_labels, disease == "Estrogens")
create.Estrogens <- dataset.create(tibble.Estrogens)
dataset.Estrogens <- dataset.fill(create.Estrogens)

write_csv(dataset.Estrogens, file.path('output', 'Estrogens.csv'))

#NSAIDS
tibble.NSAIDS <- subset(docs_labels, disease == "NSAIDS")
create.NSAIDS <- dataset.create(tibble.NSAIDS)
dataset.NSAIDS <- dataset.fill(create.NSAIDS)

write_csv(dataset.NSAIDS, file.path('output', 'NSAIDS.csv'))

##Opiods
tibble.Opiods <- subset(docs_labels, disease == "Opiods")
create.Opiods <- dataset.create(tibble.Opiods)
dataset.Opiods <- dataset.fill(create.Opiods)

write_csv(dataset.Opiods, file.path('output', 'Opiods.csv'))

#OralHypoglycemics
tibble.OralHypoglycemics <- subset(docs_labels, disease == "OralHypoglycemics")
create.OralHypoglycemics <- dataset.create(tibble.OralHypoglycemics)
dataset.OralHypoglycemics <- dataset.fill(create.OralHypoglycemics)

write_csv(dataset.OralHypoglycemics, file.path('output', 'OralHypoglycemics.csv'))

#ProtonPumpInhibitors
tibble.ProtonPumpInhibitors <- subset(docs_labels, disease == "ProtonPumpInhibitors")
create.ProtonPumpInhibitors <- dataset.create(tibble.ProtonPumpInhibitors)
dataset.ProtonPumpInhibitors <- dataset.fill(create.ProtonPumpInhibitors)

write_csv(dataset.ProtonPumpInhibitors, file.path('output', 'ProtonPumpInhibitors.csv'))

#SkeletalMuscleRelaxants
tibble.SkeletalMuscleRelaxants <- subset(docs_labels, disease == "SkeletalMuscleRelaxants")
create.SkeletalMuscleRelaxants <- dataset.create(tibble.SkeletalMuscleRelaxants)
dataset.SkeletalMuscleRelaxants <- dataset.fill(create.SkeletalMuscleRelaxants)

write_csv(dataset.SkeletalMuscleRelaxants, file.path('output', 'SkeletalMuscleRelaxants.csv'))

##Statins
tibble.Statins <- subset(docs_labels, disease == "Statins")
create.Statins <- dataset.create(tibble.Statins)
dataset.Statins <- dataset.fill(create.Statins)

write_csv(dataset.Statins, file.path('output', 'Statins.csv'))

#Triptans
tibble.Triptans <- subset(docs_labels, disease == "Triptans")
create.Triptans <- dataset.create(tibble.Triptans)
dataset.Triptans <- dataset.fill(create.Triptans)

write_csv(dataset.Triptans, file.path('output', 'Triptans.csv'))

#UrinaryIncontinence
tibble.UrinaryIncontinence <- subset(docs_labels, disease == "UrinaryIncontinence")
create.UrinaryIncontinence <- dataset.create(tibble.UrinaryIncontinence)
dataset.UrinaryIncontinence <- dataset.fill(create.UrinaryIncontinence)

write_csv(dataset.UrinaryIncontinence, file.path('output', 'UrinaryIncontinence.csv'))







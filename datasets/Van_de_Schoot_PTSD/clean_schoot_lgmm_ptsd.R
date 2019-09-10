suppressMessages(require(tidyverse))

#original papers
setwd("csv")
all.data <- read_csv("schoot-lgmm-ptsd-initial.csv", col_types=cols())

#included papers
inc.data <- read_csv("schoot-lgmm-ptsd-included-2.csv", col_types=cols())

#After abstract screening
aas.data <- read_csv("schoot-lgmm-ptsd-included-1.csv", col_types=cols())

#Directly included after reading the abstract
dir.data <- read_csv("schoot-lgmm-ptsd-included-3.csv", col_types=cols())

#all titles (clean)
all.title <- gsub("[^A-Za-z0-9]","", all.data$title)
#included titles (clean)
inc.title <- gsub("[^A-Za-z0-9]","", inc.data$title)
#After abstract screening title
aas.title <- gsub("[^A-Za-z0-9]","", aas.data$title)
#Directly included
dir.title <- gsub("[^A-Za-z0-9]","", dir.data$title)

inc_missing = ! tolower(inc.title) %in% tolower(all.title)
aas_missing = ! tolower(aas.title) %in% tolower(all.title)

cat("Papers included, missing from initial data:              ", sum(! tolower(inc.title) %in% tolower(all.title)), "\n")
cat("Papers in abstract screening, missing from initial data: ", sum(! tolower(aas.title) %in% tolower(all.title)), "\n\n")

# Add missing papers to original dataset.
all.data <- dplyr::mutate(all.data, year=as.character(year))
all.data <- bind_rows(all.data, aas.data[aas_missing,])
all.data <- bind_rows(all.data, inc.data[inc_missing,])

# Update "cleaned" titles with new additions.
all.title <- gsub("[^A-Za-z0-9]","", all.data$title)

#train data
label_inc <- as.numeric(tolower(all.title) %in% tolower(inc.title))
label_aas <- as.numeric(tolower(all.title) %in% tolower(aas.title))
label_dir <- as.numeric(tolower(all.title) %in% tolower(dir.title))

CODE_EXCLUDE = 0      # Exclude paper.
CODE_AFT_EXCLUDE = 1  # Exclude after reading full text.
CODE_AFT_INCLUDE = 2  # Include after reading full text.
CODE_AAS_INCLUDE = 3  # Include after reading abstract.

inclusion_code <- (label_aas & !label_inc)*CODE_AFT_EXCLUDE
inclusion_code <- inclusion_code + (label_inc & ! label_dir)*CODE_AFT_INCLUDE
inclusion_code <- inclusion_code + label_dir*CODE_AAS_INCLUDE

# small.train.data <- add_column(all.data[, c("authors", "title", "keywords", "abstract")], included = label_inc, aas_included = label_aas) %>%
#   mutate(authors = gsub("[\\[']", "", authors),
#          authors = gsub("\\]", "", authors))

train.data <- add_column(all.data, included = label_inc, inclusion_code = inclusion_code) %>%
    mutate(authors = gsub("[\\[']", "", authors),
           authors = gsub("\\]", "", authors))


#64 with missing title
cat("Number of papers with missing title:              ", sum(is.na(all.title)), "\n")

#762 with missing abstract
cat("Number of papers with missing abstract:           ", sum(is.na(all.data$abstract)), "\n")

#62 with both missing titles and abstracts
cat("Number of papers with missing title AND abstract: ", sum((is.na(all.title) & is.na(all.data$abstract))), "\n")

#764 with either missing titles or abstracts
cat("Number of papers with missing title OR abstract:  ", sum((is.na(all.title) | is.na(all.data$abstract))), "\n\n")




#there are duplicates, remove them:
#one option is to remove duplicates based on title and authors
#train.data[which(duplicated(train.data[,c('title','authors')], fromLast = T) == F),]

#remove duplicates based on just titles
unique.position <- duplicated(tolower(all.title), incomparables = NA)
unique.train.data <- train.data[!unique.position, ]


n_train = length(unique.train.data$included)
n_inc = sum(unique.train.data$included)
n_exc = n_train-n_inc

n_aas_exc = sum(unique.train.data$inclusion_code == 0)
n_aft_exc = sum(unique.train.data$inclusion_code == CODE_AFT_EXCLUDE)
n_aft_inc = sum(unique.train.data$inclusion_code == CODE_AFT_INCLUDE)
n_aas_inc = sum(unique.train.data$inclusion_code == CODE_AAS_INCLUDE)


cat("Total remaining papers in training set:     ", n_train, "\n")
cat("Total number of INCLUSIONS:                 ", n_inc, " (", round(100*n_inc/n_exc,2), "% )\n")
cat("Total number of EXCLUSIONS:                 ", n_exc, "\n\n")
cat("Total EXCLUSIONS after abstract screening:  ", n_aas_exc, "\n")
cat("Total EXCLUSIONS after full text screening: ", n_aft_exc, "\n")
cat("Total INCLUSIONS after full text screening: ", n_aft_inc, "\n")
cat("Total INCLUSIONS after abstract screening:  ", n_aas_inc, "\n")

write_csv(unique.train.data, 'PTSD_VandeSchoot_18.csv')



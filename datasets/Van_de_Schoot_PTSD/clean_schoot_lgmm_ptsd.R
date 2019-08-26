suppressMessages(require(tidyverse))

#original papers
setwd("csv")
all.data <- read_csv("schoot-lgmm-ptsd-initial.csv", col_types=cols())

#included papers
inc.data <- read_csv("schoot-lgmm-ptsd-included-2.csv", col_types=cols())

#After abstract screening
aas.data <- read_csv("schoot-lgmm-ptsd-included-1.csv", col_types=cols())

#all titles (clean)
all.title <- gsub("[^A-Za-z0-9]","", all.data$title)
#included titles (clean)
inc.title <- gsub("[^A-Za-z0-9]","", inc.data$title)
#After abstract screening title
aas.title <- gsub("[^A-Za-z0-9]","", aas.data$title)

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

# small.train.data <- add_column(all.data[, c("authors", "title", "keywords", "abstract")], included = label_inc, aas_included = label_aas) %>%
#   mutate(authors = gsub("[\\[']", "", authors),
#          authors = gsub("\\]", "", authors))

train.data <- add_column(all.data, included = label_inc, aas_included = label_aas) %>%
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

# Set aas_included to 1 if they are in the final inclusion.
paper_direct = unique.train.data$aas_included == 0 & unique.train.data$included == 1
unique.train.data[paper_direct, "aas_included"] <- 1


n_train = length(unique.train.data$included)
n_inc = sum(unique.train.data$included)
n_aas = sum(unique.train.data$aas_included | unique.train.data$included)

n_direct = sum(paper_direct)
cat("Total remaining papers in training set: ", n_train, "\n")
cat("Papers after abstract screening:        ", n_aas, "\n")
cat("Final papers included:                  ", n_inc, "\n")
cat("Papers directly included:               ", n_direct, "\n")

# print.data.frame(unique.train.data[unique.train.data$included==1,])
write_csv(unique.train.data, 'PTSD_VandeSchoot_18.csv')



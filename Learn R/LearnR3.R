 # DATA CLEANING IN R

 # Diagnose the Data

 head()
 summary()
 colnames()

 # Dealing with Multiple Files
 

# You can combine the base R functions list.files() and lapply() with readr and dplyr to organize this data better, as shown below:
files <- list.files(pattern = "file_.*csv")
df_list <- lapply(files,read_csv)
df <- bind_rows(df_list)

```{r message=FALSE}
# read files
student_files <- list.files(pattern = "exams_.*csv")
df_list <- lapply(student_files,read_csv)
```

```{r}
# concatenate data frames
students <- bind_rows(df_list)

```

```{r}
# number of rows in students
head(students)
nrow_students <- nrow(students)
head(nrow_students)

```

# Reshaping your Data


```{r message=FALSE, warning=FALSE}
# load libraries
library(dplyr)
library(tidyr)
```

```{r}
# load students data frame
load("students.Rda")
```

```{r}
# original column names
original_col_names = colnames(students)

```

```{r}
#We can use tidyr’s gather() function to do this transformation. gather() takes a data frame and the columns to unpack:

# gather columns
students <- students %>% gather("fractions","probability",key = "exam",value = "score")
head(students)

# students is the dataframe you want to unpack
#fractions and probabilities are the columns of the old data frame that you want to turn into variables
# key is what to call the column of the new data frame that stores the variables
# value is what to call the column of the new data frame that stores the values
```

```{r}
# updated column names
gathered_col_names = colnames(students)
print(gathered_col_names)

```

```{r}
# dplyr function count() takes a data frame and a column as arguments and returns a table with counts of the unique values in the named column.

# unique value counts of exam
exam_counts = students %>% count(exam)
head(exam_counts)

```


# Dealing with Duplicates

```{r}
# drop id column
students <- students %>% select(-id)
head(students)


```

```{r}
# find and count duplicated rows

# To check for duplicates, we can use the base R function duplicated(), which will return a logical vector telling us which rows are duplicate rows.

duplicates = students %>% duplicated()%>%table()

# table() is a base R function that takes any R object as an argument and returns a table with the counts of each unique value in the object
head(duplicates)


```

```{r}
# remove duplicated rows

# We can use the dplyr distinct() function to remove all rows of a data frame that are duplicates of another row.
students <- students %>% distinct()

```

```{r}
# find and count duplicated rows in updated data frame

updated_duplicates <- students %>% duplicated()%>%table()
head(updated_duplicates)


# if we wanted to remove every row with a duplicate value in an item column, we could specify a subset:
# Be careful using this as it can remove rows with important data

fruits %>%
  distinct(item,.keep_all=TRUE)
```


# Splitting By Index


```{r}
#We can easily break the data into three separate columns by splitting the strings into substrings using str_sub(), a helpful function from the stringr package:

# Let’s say we have a column “birthday” with data formatted in MMDDYYYY format. In other words, “11011993” represents a birthday of November 1, 1993. We want to split this data into day, month, and year so that we can use these columns as separate features.

# Create the 'month' column
df %>%
  mutate(month = str_sub(birthday,1,2))

# Create the 'day' column
df %>%
  mutate(day = str_sub(birthday,3,4))

# Create the 'year' column
df %>%
  mutate(year = str_sub(birthday,5))



# print columns of students
print(colnames(students))
```

```{r}
# view head of students
head(students)
```

```{r}
# add gender and age columns
students <- students %>% mutate(gender = str_sub(gender_age,1,1) )

head(students)
students <- students %>% mutate(age = str_sub(gender_age,2))

head(students)
```

```{r}
# drop gender_age column
students <- students %>% select(-gender_age)
head(students)

```

 # Splitting By Character


```{r}
# We can thus use the tidyr function separate() to split this column into two, separate columns:

# Create the 'user_type' and 'country' columns
df %>%
  separate(type,c('user_type','country'),'_')

#type is the column to split

#c('user_type','country') is a vector with the names of the two new columns

#'_' is the character to split on

# view the head of students
head(students)
```

```{r}
# separate the full_name column
students <- students %>% separate(full_name,c("first_name","last_name")," ",extra = "merge")

# Provided as an extra argument is the separate() function extra ='merge'. This will ensure that middle names or two-word last names will all end up in the last_name column.

head(students)


```

# Looking at Data Types

# To see the types of each column of a data frame, we can use:

str(df)

print(str(students))

# String Parsing


```{r}
# load students data frame
load("students.Rda")
```

```{r}
#The base R function gsub() will remove the $ from the price column, replacing the symbol with an empty string '':

fruit %>%
  mutate(price=gsub('\\$','',price))

# Then, we can use the base R function as.numeric() to convert character strings containing numerical values to numeric:

fruit %>%
  mutate(price = as.numeric(price))



# view head of students
head(students)
```

```{r}
# remove % from score column
students <- students %>% mutate(score = gsub('\\%',"",score))


```

```{r}
# change score column to numeric
students <- students %>% mutate(score = as.numeric(score))
head(students)

```

```{r}
# update age column
students <- students %>% mutate(age = as.numeric(age))

head(students)


```


# INTRO TO VISUALIZATION WITH R

# Layers and Geoms

# The basic units in the “grammar of graphics” consist of:
#The data or the actual information you wish to visualize.
#The geometries, shortened to “geoms”, describe the shapes that represent our data. e.g line plot,bar plot
#The aesthetics, or the visual attributes of the plot, including the scales on the axes, the color, the fill, and other attributes concerning appearance.
---
title: "Intro To GGPlot2"
output: html_notebook
---

```{r message=FALSE, warning=FALSE}
# load libraries and data
library(readr)
library(dplyr)
library(ggplot2)
movies <- read_csv("imdb.csv")
```

```{r}
# Observe layers being added with the + sign
viz <- ggplot(data=movies, aes(x=imdbRating, y=nrOfWins)) +
       geom_point(aes(color=nrOfGenre), alpha=0.5) + 
       labs(title="Movie Ratings Vs Award Wins", subtitle="From IMDB dataset", y="Number of Award Wins", x="Move Rating", color = "Number of Genre")


# Prints the plot
viz
```

# The ggplot() function

# conceptualize that arguments defined inside ggplot() are inherited by other layers.
ggplot() 


# Associating the Data

```{r}
#Define variable and print it
viz <- ggplot(data = movies)

viz
```

# What are aesthetics?


```{r}
# Inherited aesthetics are aesthetics you define at the canvas level. Every subsequent layers inherit from this aes( ) defined at the canvass level.

viz <- ggplot(data=airquality, aes(x=Ozone, y=Temp)) +
       geom_point() + 
       geom_smooth()


#Create aesthetic mappings at the canvas level

viz <- ggplot(data=movies,aes(x = imdbRating,y = nrOfWins ))
viz
```

# Adding Geoms

# geometries or geoms are the shapes that represent our data.

```{r}
# the scatterplot geom, or geom_point()
# geom_smooth() layer this layer adds the best line fit for the data


# Add a geom point layer
viz <- ggplot(data=movies, aes(x=imdbRating, y=nrOfWins)) + geom_point()


# Prints the plot
viz
```

# Geom Aesthetics


# We can add specific attributes to a geom by paasing it inside the geom and it will be applied only to that geom layer


```{r}
# Add manual alpha aesthetic mapping
viz <- ggplot(data=movies, aes(x=imdbRating, y=nrOfWins)) + geom_point(aes(color=nrOfGenre)) 


# Prints the plot
viz
```

# Manual aesthetics

```{r}
# We can manually add the aesthetics we need by adding it manually as an argument and not inside the aes function.
# To make ur scatterplots darkred simply pass in a color parameter with a manual value darkred or any color value like so:

viz <- ggplot(data=airquality, aes(x=Ozone, y=Temp)) +
       geom_point(color="darkred") 

# Note that we did not wrap the color argument inside aes() because we are manually setting that aesthetic. Here are more aesthetics for the geom_point() layer: x, y, alpha, color, fill, group, shape, size, stroke. The alpha aesthetic describes opacity of the points, and the shape of the dots could be different than a dot. Read more about the values each of these aesthetics take in the geom_point() layer documentation. 

# Add manual alpha aesthetic mapping
viz <- ggplot(data=movies, aes(x=imdbRating, y=nrOfWins)) +
       geom_point(aes(color=nrOfGenre),alpha = 0.5) 


# Prints the plot
viz
```

# Labels

```{r}
# If you wish to customize your labels, you can add a labs() function call to your ggplot object. Inside the function call to labs() you can provide new labels for the x and y axes as well as a title, subtitle, or caption. You can check out the list of available label arguments in the labs() documentation.

viz <- ggplot(df, aes(x=rent, y=size_sqft)) + 
       geom_point() +
       labs(title="Monthly Rent vs Apartment Size in Brooklyn, NY", subtitle="Data by StreetEasy (2017)", x="Monthly Rent ($)", y="Apartment Size (sq ft.)")
viz


# Add labels as specified
viz <- ggplot(data=movies, aes(x=imdbRating, y=nrOfWins)) +
       geom_point(aes(color=nrOfGenre), alpha=0.5) +
       labs(title="Movie Ratings Vs Award Wins", subtitle="From IMDB dataset", x="Movie Rating", y="Number of Award Wins",color = "Number of Genre")


# Prints the plot
viz
```

```{r message=FALSE}
```


# Extending The Grammar


```{r}

bar <- ggplot(books, aes(x=Language)) + geom_bar()
bar
ggsave("bar-example.png")
#ggsave allows us to save the work
# Inspect the mpg builtin dataset
head(mpg)

# mpg is a car data set from ggplot library
```

```{r message=FALSE}
#Create a bar chart
bar <- ggplot(data=mpg,aes(x=class)) + geom_bar(aes(fill=class)) + labs(title="Types of Vehicles", subtitle="From fuel economy data for popular car models (1999-2008)")

bar
```

# Review

#Find the right geom(s) in the ggplot2 documentation
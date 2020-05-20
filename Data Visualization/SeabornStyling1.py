#we’ll look at how we can effectively use color to convey meaning. We’ll cover:

#How to set a palette
#Seaborn default and built-in color palettes
#Color Brewer Palettes
#Selecting palettes for your dataset

#If you want to quickly see what a palette looks like,
#use the function sns.palplot() to plot a palette as an array of colors:

# Save a palette to a variable:
palette = sns.color_palette("bright")

# Use palplot and pass in the variable:
sns.palplot(palette)

#To select and set a palette in Seaborn, use the command sns.set_palette() 
#and pass in the name of the palette that you would like to use:
# Set the palette using the name of a palette:
sns.set_palette("Paired")

# Plot a chart:
sns.stripplot(x="day", y="total_bill", data=tips)

#Seaborn also allows you to style Matplotlib plots
#To do so, call the sns.set() function before your plot:

# Call the sns.set() function 
sns.set()
for col in 'xy':
  plt.hist(data[col], normed=True, alpha=0.5)

#Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.

#To use one of these palettes, pass the name into sns.set_palette():

# Set the palette to the "pastel" default palette:
sns.set_palette("pastel")

# plot using the "pastel" palette
sns.stripplot(x="day", y="total_bill", data=tips)

#To use, pass the name of any Color Brewer palette directly to any of the color functions:

custom_palette = sns.color_palette("Paired", 9)
sns.palplot(custom_palette)

#Here’s an example of a qualitative Color Brewer palette:

qualitative_colors = sns.color_palette("Set3", 10)
sns.palplot(qualitative_colors)

#Here’s an example of a sequential Color Brewer palette:

sequential_colors = sns.color_palette("RdPu", 10)
sns.palplot(sequential_colors)

#Diverging palettes are best suited for datasets where both the low and high
# values might be of equal interest, such as hot and cold temperatures.
diverging_colors = sns.color_palette("RdBu", 10)
sns.palplot(diverging_colors)



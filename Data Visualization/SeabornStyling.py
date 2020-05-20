# in Seaborn - background color, grids, and spines - and these elements can change the look and meaning of your visualizations.
# Seaborn has five built-in themes to style its plots: darkgrid, whitegrid, dark, white, and ticks. Seaborn defaults to using the darkgrid theme for its plots.
sns.set_style("darkgrid")
sns.set_style("ticks")
#Style for the plot below
sns.stripplot(x="day", y="total_bill", data=tips)

#You can also add grids 
sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)

#spine
#By default, an image has four spines. The Square border around a plot
#You may want to remove some or all of the spines for various reasons.
#You can automatically take away the top and right spines using the sns.despine()function.
# Note: this function must be called after you have called your plot.
sns.set_style("white")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine()

#Not including any spines at all may be an aesthetic decision. despine()
sns.set_style("whitegrid")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.despine(left=True, bottom=True)

#You can set the visual format, or context, using sns.set_context()
#Within the usage of sns.set_context(), there are three levels of complexity:

#Pass in one parameter that adjusts the scale of the plot
#Pass in two parameters - one for the scale and the other for the font size
#Pass in three parameters - including the previous two, as well as the rc with the style parameter that you want to override.

#In order of relative size they are: paper, notebook, talk, and poster. The notebook style is the default.
sns.set_style("ticks")

# Smallest context:
sns.set_context("paper")
sns.stripplot(x="day", y="total_bill", data=tips)

sns.set_style("ticks")

# Largest Context:
sns.set_context("poster")
sns.stripplot(x="day", y="total_bill", data=tips)

#Scaling Fonts and Line Widths
#You are also able to change the size of the text using the font_scale parameter for sns.set_context()
# Set font scale and reduce grid line width to match
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.stripplot(x="day", y="total_bill", data=tips)

# Set font scale and increase grid line width to match
sns.set_context("poster", font_scale = 1, rc={"grid.linewidth": 5})
sns.stripplot(x="day", y="total_bill", data=tips)

#As we mentioned above, if you want to override any of these standards, you can use sns.set_context and pass in the parameter rc to target 
#and reset the value of an individual parameter in a dictionary. rc stands for the phrase ‘run command’ - essentially,
# configurations which will execute when you run your code.




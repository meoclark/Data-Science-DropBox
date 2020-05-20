# In order to be sure that you don’t have any stray lines, you can use the command
 #to clear all existing plots before you plot a new one.
  plt.close('all')

  #We can use the command below to create new figures and size them
  plt.figure()
  plt.figure(figsize=(4, 10))


  # Figure 2
plt.figure(figsize=(4, 10)) 
plt.plot(x, parabola)
#We use plt.savefig() to save our graph in any format. png,svg,pdf.
plt.savefig('tall_and_narrow.png')
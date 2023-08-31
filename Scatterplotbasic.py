people = ['Ann','Brandon','Chen','David','Emily','Farook', 'Gagan', 'Hamish', 'Imran', 'Julio', 'Katherine', 'Lily' ]
age = [21,12,32,45,37,18,28,52,5,40,48,15]
weight = [55,35,77,68,70,60,72,69,18,65,82,48]
height = [160,135,170,165,173,168,175,159,105,171,155,158]

#-------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

#scatter chart
plt.scatter(age, height)
plt.show()

#-------------------------------------------------------------------------------------------------

# Set figure size
plt.figure(figsize=(8,6))

#-------------------------------------------------------------------------------------------------

# Add a main title
plt.title("Plot of Age vs. Height (in cms)\n",fontsize=20, fontstyle='italic')


#-------------------------------------------------------------------------------------------------

# X- and Y-label with fontsize
plt.xlabel("Age (years)",fontsize=16)
plt.ylabel("Height (cms)",fontsize=16)


#-------------------------------------------------------------------------------------------------

# Turn on grid
plt.grid (True)

#-------------------------------------------------------------------------------------------------

# Set Y-axis limit
plt.ylim(100,200)


#-------------------------------------------------------------------------------------------------

# X- and Y-axis ticks customization with fontsize and placement
plt.xticks([i*5 for i in range(12)],fontsize=15)
plt.yticks(fontsize=15)

#-------------------------------------------------------------------------------------------------


# Main plotting function with choice of color, marker size, and marker edge color
plt.scatter(x=age,y=height,c='orange',s=150,edgecolors='k')


#-------------------------------------------------------------------------------------------------


# Adding bit of text to the plot
plt.text(x=15,y=105,s="Height increaes up to around \n20 years and then tapers off",fontsize=15,rotation=30, linespacing=2)
plt.text(x=22,y=185,s="Nobody has a height beyond 180 cm",fontsize=15)



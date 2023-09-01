people = ['Ann','Brandon','Chen','David','Emily','Farook', 'Gagan', 'Hamish', 'Imran', 'Julio', 'Katherine', 'Lily' ]
age = [21,12,32,45,37,18,28,52,5,40,48,15]
weight = [55,35,77,68,70,60,72,69,18,65,82,48]
height = [160,135,170,165,173,168,175,159,105,171,155,158]



import seaborn as sns

#Boxplot separated by class/groups of data
#( https://seaborn.pydata.org/generated/seaborn.boxplot.html)
sns.boxplot(x='Class',y='Alcohol',data=df)

#Violin plots (combination of boxplot and histogram/kernel density)
sns.violinplot(x='Class',y='Alcohol',data=df)

#regplot - computes and plots the linear regression fit along with confidence interval
sns.regplot(x='Alcohol',y='Color intensity',data=df)
plt.show()

#lmplot - combination of regplot with grid to visualize across various groups/classes
sns.lmplot(x='Alcohol',y='Color intensity',hue='Class',data=df)
plt.show()

#Correlation matrix and heatmap
import numpy as np
corr_mat=np.corrcoef(df,rowvar=False)
corr_mat.shape
corr_df = pd.DataFrame(corr_mat,columns=df.columns,index=df.columns)
print(np.round(corr_mat,3))
sns.heatmap(corr_df,linewidth=1,cmap='plasma')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter Plot - Total Bill vs Tip")
plt.show()

sns.boxplot(x="total_bill", data=tips)
plt.title("Box Plot - Distribution of Total Bill")
plt.show()


sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot - Total Bill distribution by Day")
plt.show()

sns.pairplot(tips, hue="sex")
plt.suptitle("Pair Plot - Pairwise Relationships with Hue for Sex")
plt.show()

sns.boxplot(x="sex", y="total_bill", data=tips)
plt.title("Box Plot - Distribution of Total Bill by Gender")
plt.show()


sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", cmap="viridis")
plt.suptitle("Hexbin Plot - Total Bill vs Tip with Color Gradients")
plt.show()
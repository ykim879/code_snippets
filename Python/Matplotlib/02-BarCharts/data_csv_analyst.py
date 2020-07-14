from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
#print(plt.style.available)
plt.style.use("dark_background")

fig,ax = plt.subplots()
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
#print(df)
#print(type(df["Responder_id"]))
r_id = df["Responder_id"]
languages = df["LanguagesWorkedWith"]


counter = Counter()

for language in languages:
	counter.update(language.split(";"))

print(type(counter))
y_axis = []
x_axis = []

for c in counter.most_common(20):
	y_axis.append(c[0])
	x_axis.append(c[1])
y_axis.reverse()
x_axis.reverse()

ax.barh(y_axis, x_axis)
ax.set_title("The Frequency of Using Programming Language")
plt.show()
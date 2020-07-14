from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = False)

ax1.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

s_slices = []
for s in slices:
	s_slices.append(str(s))

ax2.barh(labels, s_slices)

ax1.set_title("Frequency of Using Programming Languages")
plt.tight_layout()
plt.show()

fig.savefig("finished_code.png")
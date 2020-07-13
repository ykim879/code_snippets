from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("fivethirtyeight")

#df['py_dev_y']
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

fig, (ax, ax1) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

ax.plot(ages_x, dev_y, color="#444444", label="All Devs")


py_dev_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
ax.plot(ages_x, py_dev_y, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
ax.plot(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")

data = {
	"ages" : ages_x, 
	"Python": py_dev_y,
	"JavaScript": js_dev_y
}
df = pd.DataFrame(data)

ax1.barh(["Python", "JavaScript"], [df["Python"].median(), df["JavaScript"].median()])
ax1.set_ylabel("Average Salary")

ax.legend()

ax.set_title("Median Salary (USD) by Age")
ax.set_xlabel("Ages")
ax.set_ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()

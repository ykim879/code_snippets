
import pandas as pd
from matplotlib import pyplot as plt

#print(plt.style.available)
plt.style.use('fast')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)



ax2.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')


ax1.plot(ages, py_salaries, label='Python')
ax1.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax2.legend()

ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig.savefig('my_fig.png')

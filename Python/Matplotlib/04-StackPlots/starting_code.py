from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels=["Player 1", "Player2", "Player3"]

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1)

ax1.pie([1, 1, 1], labels = labels)
ax1.set_title("Data on Pie Chart")

ax2.stackplot(minutes, player1, player2, player3, labels = labels)
ax2.legend(loc = (0,1))
ax2.set_title("Data on Stack Plot")
ax2.set_ylabel("shots per a game")
ax2.set_xlabel("minutes")

data = {
	"player1" : player1,
	"player2" : player2,
	"player3" : player3
}
df = pd.DataFrame(data)

ax3.barh(labels, [df["player1"].median(), df["player2"].median(), df["player3"].median()])
ax3.set_xlabel("average shot for each player")
plt.tight_layout()
plt.show()
plt.savefig("my_final.png")

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

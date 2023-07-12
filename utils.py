import matplotlib.pyplot as plt

def createHistogram(abscissaData, ordinateData, barColors):
  plt.bar(abscissaData, ordinateData, color=barColors, zorder=2)
  # plt.xlabel("Format Name")
  # plt.title("Formats by Size")
  plt.ylabel("Payload size (B)")
  plt.xticks(rotation=90)
  plt.grid(axis="y", linestyle="dashed", linewidth=0.5, zorder=1)
  plt.xticks(fontsize=9, rotation=10)


  plt.show()
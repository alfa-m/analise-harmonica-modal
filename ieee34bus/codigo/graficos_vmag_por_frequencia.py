import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

vmag_df = pd.read_csv("../analise_sem_loop/ieee34-1_Mon_l18_828_1_1.csv")
tensao_1 = vmag_df.iloc[0:,2]
tensao_2 = vmag_df.iloc[0:,4]
tensao_3 = vmag_df.iloc[0:,6]
harmonico = vmag_df.iloc[0:,1]
fig, ax = plt.subplots()
ax.plot(harmonico, tensao_1, label='V1')
ax.plot(harmonico, tensao_2, label='V2')
ax.plot(harmonico, tensao_3, label='V3')
ax.legend()
ax.grid()
plt.show()

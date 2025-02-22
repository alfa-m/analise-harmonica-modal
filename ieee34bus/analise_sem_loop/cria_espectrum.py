import pandas as pd
import numpy as np

harmonico_pd = pd.DataFrame()
harmonico_pd['harmonico'] = np.arange(1,100.001,(0.5/60)).tolist()
harmonico_pd['harmonico'] = harmonico_pd['harmonico'].apply(lambda h : round(h, 6))
harmonico_pd['amplitude'] = 100
harmonico_pd['angulo'] = 0
harmonico_pd.to_csv("espectro_harmonico_longo.csv", index=False, header=False)

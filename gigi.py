# To read the txt file 
import pandas as pd

GAIN_path = "gain.txt"
GAIN_df = pd.read_csv(GAIN_path, delim_whitespace=True, comment='E', header=None, skiprows=1)
GAIN_df.columns = ['a(cm)', 'B(cm^-2)', 'K_eff', 'Facteur_mult', 'Taux_U(coup/s)', 'Taux(coup/s)', 'Gain']

# Plot (K)
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(GAIN_df['K_eff'], GAIN_df['Gain'], 'o-', color='purple', label='Le Gain')

plt.xlabel("K_eff")
plt.ylabel("Gain")
plt.title("Variation du Gain en fonction du facteur de multiplication effectif ")
plt.legend()
plt.grid(False)

outpath = "GAIN1.png"
plt.savefig(outpath, dpi=200, bbox_inches='tight')
plt.show()

# Plot (a)
plt.figure(figsize=(8, 6))
plt.plot(GAIN_df['a(cm)'], GAIN_df['Gain'], 'o-', color='red', label='Le Gain')

plt.xlabel("a (cm)")
plt.ylabel("Gain")
plt.title("Variation du Gain en fonction de l'arrête ")
plt.legend()
plt.grid(False)

outpath = "GAIN2.png"
plt.savefig(outpath, dpi=200, bbox_inches='tight')
plt.show()

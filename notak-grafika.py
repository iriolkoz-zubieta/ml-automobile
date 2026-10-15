import pandas as pd
import matplotlib.pyplot as plt

# Irakurri CSV fitxategiko datuak.
datuak = pd.read_csv("data/notak.csv")

# Marraztu ikasketa-orduen eta noten arteko sakabanatze-diagrama.
plt.scatter(datuak["orduak"], datuak["nota"])
plt.xlabel("Orduak")
plt.ylabel("Nota")
plt.title("Ikasketa-orduak eta notak")

plt.show()



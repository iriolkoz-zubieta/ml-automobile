import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Irakurri CSV fitxategiko datuak.
datuak = pd.read_csv("data/notak.csv")

# Marraztu ikasketa-orduen eta noten arteko sakabanatze-diagrama.
plt.scatter(datuak["orduak"], datuak["nota"])
plt.xlabel("Orduak")
plt.ylabel("Nota")
plt.title("Ikasketa-orduak eta notak")

#plt.show()

# Prestatu datuak erregresio linealerako eta entrenatu eredua.
X = datuak[["orduak"]]
y = datuak["nota"]
eredua = LinearRegression()
eredua.fit(X, y)

# Kalkulatu ereduaren zuzenaren balioak eta gehitu grafikoan.
orduak_zuzen = pd.DataFrame({"orduak": [X["orduak"].min(), X["orduak"].max()]})
notak_aurreikusita = eredua.predict(orduak_zuzen)
plt.plot(orduak_zuzen["orduak"], notak_aurreikusita, color="red", label="Erregresio lineala")
plt.legend()

plt.grid(True)
plt.show()

# Aurreikusi 3,75 ordu ikasiz gero lortuko den nota.
ordu_kopurua = 3.75
nota_aurreikusita = eredua.predict(pd.DataFrame({"orduak": [ordu_kopurua]}))[0]
print(f"{ordu_kopurua} ordu ikasiz gero, aurreikusitako nota: {nota_aurreikusita:.2f}")


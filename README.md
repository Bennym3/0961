# Progetto Simulazione CALPHAD

Questa repository contiene semplici strumenti per il calcolo di alcune proprietà dei materiali.

## Moduli principali

- **models.py** implementa modelli di regressione per modulo elastico e durezza,
  il calcolo del parametro di Larson–Miller per la rottura a creep e una legge
  parabolica semplificata per la crescita di ossidi.
- **cli.py** offre una semplice interfaccia a riga di comando per utilizzare i
  modelli.
- **gui.py** mette a disposizione una piccola interfaccia grafica basata su
  Tkinter.
- **export.py** permette di esportare i risultati in formato CSV o JSON.

## Utilizzo da riga di comando

Esempio di fit del modulo elastico:

```bash
python cli.py fit-modulus --temperatures 300 400 500 --values 200 180 160 --out coeffs.json
```

Calcolo del parametro di Larson–Miller:

```bash
python cli.py creep-rupture --temperature 1000 --time 1000
```

## Avvio della GUI

```bash
python gui.py
```

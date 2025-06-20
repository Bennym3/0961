# Progetto Simulazione CALPHAD

Questa repository contiene un'implementazione di base di una
applicazione di simulazione termodinamica in stile CALPHAD.

I moduli principali includono:
- `models.py`: classi per rappresentare materiali e fasi.
- `thermodynamics.py`: funzioni semplificate per calcoli termodinamici.
- `solver.py`: procedure iterative per la stima dell'equilibrio.
- `database.py`: dataset interni di esempio.
- `export.py`: funzioni di esportazione dei dati.
- `gui.py`: interfaccia utente minimale.

Per eseguire un esempio rapido di simulazione da riga di comando:
```bash
python gui.py
```

Sono utilizzati solo modelli approssimati e dati interni, senza
accesso a database termodinamici esterni.

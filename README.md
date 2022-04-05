## Détection de coupures de connection

Petit programme non-optimisé qui détecte les coupures/micro-coupures d'internet et les répertorie dans un fichier.txt.

Utilisant:
```python
os.system("ping -n 1 google.com")
```
de la librairie [os](https://docs.python.org/3/library/os.html "librairie os").


Screen des lignes qui apparaissent lorsqu'il y a eu une coupure:

    Début de coupure: 2022-04-04 13:56:20	Fin de coupure: 2022-04-04 13:56:20    Durée de coupure: 0:00:00.220088
    Début de coupure: 2022-04-04 13:56:47	Fin de coupure: 2022-04-04 13:56:59    Durée de coupure: 0:00:12.282248


Screen du bloc qui apparaît lorsqu'on arrête le programme:

    ---------------------------------------------------------------
    Début du test: 2022-04-04 13:56:06.300269
    Fin du test: 2022-04-04 13:57:14.587292
    Durée du test: 0:01:08.287023

    Nombre de coupures: 2
    Durée totale des coupures: 0:00:12.502336
    Durée moyenne des coupures: 0:00:06.251168
    ---------------------------------------------------------------

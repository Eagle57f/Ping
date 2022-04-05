## Détection de coupures de connection

Petit programme non-optimisé qui détecte les coupures/micro-coupures d'internet et les répertorie dans un fichier.txt.

Utilisant:
```python
os.system("ping -n 1 google.com")
```
de la librairie [os](https://docs.python.org/3/library/os.html "librairie os").


Screen des lignes qui apparaissent lorsqu'il y a eu une cooupure:

![Screen ligne coupure fichier .txt](https://github.com/Eagle57f/Ping/blob/main/Capture_fichier_ligne_coupoure.PNG "Screen ligne coupure")

Screen du bloc qui apparaît lorsqu'on arrête le programme:

![Screen du bloc final fichier .txt](https://github.com/Eagle57f/Ping/blob/main/Capture_fichier_texte_bloc_fin.PNG "Screen bloc final")

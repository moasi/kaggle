# Pràctica Kaggle APC UAB 2022-23
### Nom: Mohamed El Harrak
### DATASET: Fruits fresh and rotten for classification

## Resum
El dataset utilitza fotografies on tenim 10000 fotos per el dataset de train i 2500 per el dataset de test, totes elles son categoriques on poden tenir 6 diferents tipus de classes, rottenapples, rottenbananas, rottenoranges, freshapples, freshbananas, freshapples.

### Objectius del dataset
Volem determinar si una foto nova sera alguna de les anteriors classes independentment de si esta girada si te parts en negre e.t.c.

### Experiments
Durant la practica he realitzat diferents proves cambiant els parametres del model que me ha funcionat i veient com cambia el resultat en comparació amb els altres

### Model
| Model | Hiperparametres | Mètrica | Temps|
|-------|-----------------|---------|------|
| CNN   | epochs = 10     |acc = 90%| 88s  |
| knn   | kneighbours = 5 |acc = 0  | 0.37s|
|-------|-----------------|---------|------|

## Conclusions 
EL millor model que he aconseguir ha sigut CNN he intentant aplicar altres metodes que he realitzat en les practiques anteriors pero al no ser un csv no he sapigut tractar les dades amb exit

## Idees per treballar en un futur
Crec que m'hariua agradat molt mes indagar sobre machine learning si ho hagues realitzat amb calma ja que el poc que he fet m'ha semblat molt interessant per seguir aprenent en un futur.

## Llicencia
El projecte s'ha desenvolupat sota Jupyter Notebook en la seva majorietat.
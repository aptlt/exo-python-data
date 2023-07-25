## Commencement
Ecriture deux fonctions :
- Une fonction permettant d'aller taper sur l'URL : https://data.grandlyon.com/fr/datapusher/ws/rdata/lpa_mobilite.parking_lpaco_2_0_0/all.json. Cette fonction doit écrire le résultat de la requête (GET) dans une variable où sera formaté les données en json.
Librairies nécessaires : requests, json
<br>
- Une fonction permettant d'écrire ces données dans un fichier .json. Pour une facilité de lecture, on indentera le fichier json de 4 (voir json.dumps)
Librairies nécessaires : json


## Exo 1
Compter les parkings accessibles au public : Écrire une fonction qui compte combien de parkings ont "publicaccess" défini sur True.

## Exo 2
Afficher 2 listes : 
- Une liste contiendra le nom des parkings qui sont accessibles au public
- Une liste contiendra le nom des parkings qui ne sont pas accessibles au public
*(Possibilité de démarrer en se basant sur l'algorithme développé à l'exo 1)*

Voici les étapes à suivre :
- Créer deux listes vides : public_parkings et private_parkings (voir comment déclarer des listes en python).
- Parcourir les données JSON et, pour chaque parking, vérifier la valeur de publicaccess (voir exo 1).
- Si publicaccess est true, ajouter le name du parking à public_parkings. Si publicaccess est false, ajouter le name du parking à private_parkings. 
    *Pour ajouter un élément à une liste, on utilise la méthode .append sur une liste. Par exemple : public_parkings.append("MON_SUPER_PARKING") va ajouter MON_SUPER_PARKING à la liste public_parkings. Les noms des parkings sont sous `['values']['name']`*
- Une fois tous les parkings traités, imprimer les deux listes.

## Exo 3
Compter le nombre de parkings dans chaque arrondissement, selon le code postal ("schema:postalCode").
Voici les étapes à suivre :

- Parcourir le JSON pour extraire les données de chaque parking.
- Récupérer le code postal de chaque parking.
- Utiliser un dictionnaire pour compter le nombre de parkings pour chaque code postal. La clé de ce dictionnaire sera le code postal et la valeur sera le nombre de parkings correspondants.
- Afficher pour chaque arrondissement le nombre de parkings disponibles.

À la fin de cet exercice, vous devriez être en mesure d'afficher un message comme celui-ci pour chaque arrondissement : "{arrondissement} : X parkings disponibles."

BONUS : Afficher dans l'ordre décroissant les arrondissements (utiliser `sorted(my_var.items(), key=lambda item: item[1], reverse=True)`)

## Exo 4
Recherche du parking le moins cher en tarif mensuel: Écrire une fonction qui parcourt les données et identifie le parking avec le tarif mensuel le moins cher, basé sur le "schema:price" et le "schema:name" devant inclure le string "Abonnement mensuel".<br>
Cet exercice pourrait impliquer la conversion des tarifs de string à float et la recherche du minimum.

## Exo 5
À partir des données du JSON, votre tâche est de calculer la moyenne des prix pour chaque type de tarification ("schema:name") disponible dans les parkings.
Pour cela, vous devez :

- Parcourir l'ensemble des données de chaque parking pour récupérer toutes les offres ("offer").
- Enregistrer les prix ("schema:price") de chaque offre en les classant par type de tarification ("schema:name").
- Une fois tous les prix enregistrés, calculer la moyenne des prix pour chaque type de tarification.
- Afficher la moyenne des prix pour chaque type de tarification, arrondie à deux décimales.

À la fin de cet exercice, vous devriez pouvoir afficher un message pour chaque type de tarification, comme par exemple : "Moyenne des prix pour la tarification 24 heures : 13.00€".

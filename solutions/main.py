import config
import requests
import json

#########################################
#####  FONCTIONS GLOBALES AU SCRIPT #####
#########################################
# Recuperation des donnees depuis l'API
def get_datas(indent=True):
    response = requests.get(config.url_data_grand_lyon)
    data = response.json()
    return data

# Ecriture des donnes dans un fichier passe en parametre
def write_datas(filename, datas):
    formatted_data = json.dumps(datas, indent=4)
    with open(filename, "w") as file:
        file.write(formatted_data)
#########################################


#########################################
#####     UNE FONCTION PAR EXO      #####
#########################################
def exo1(data):
    count = 0
    for parking in data['values']:
        if parking['publicaccess']:
            count += 1
    
    print(f"Nombre de parkings accessibles au public : {count}")
    

def exo2(data):
    public_parkings = []
    private_parkings = []

    for parking in data['values']:
        if parking['publicaccess']:
            public_parkings.append(parking['name'])
        else:
            private_parkings.append(parking['name'])

    print(f"Liste des parkings publics : {public_parkings}")
    print(f"Liste des parkings privés : {private_parkings}")


def exo3(data):
    parkings_per_district = {}

    for parking in data['values']:
        # Récupération du code postal
        postal_code = parking['address']['schema:postalCode']
        
        # Si le code postal est déjà présent dans le dictionnaire, on incrémente le compteur correspondant
        if postal_code in parkings_per_district:
            parkings_per_district[postal_code] += 1
        # Sinon, on ajoute le code postal au dictionnaire avec un compteur initialisé à 1
        else:
            parkings_per_district[postal_code] = 1

    # Affichage du nombre de parkings par arrondissement
    for district, count in sorted(parkings_per_district.items(), key=lambda item: item[1], reverse=True):
        print(f"{district} : {count} parkings disponibles.")


def exo4(data):
    # On définit le prix min à 'infini'
    min_price = float('inf')
    cheapest_parking = None
    
    for parking in data['values']:
        for offer in parking['offer']:
            for price_spec in offer['schema:priceSpecification']:
                if "Abonnement mensuel" in price_spec['schema:name']:
                    price = float(price_spec['schema:price'])
                    if price < min_price:
                        min_price = price
                        cheapest_parking = parking['name']
    
    print(f"Parking mensuel le moins cher : {cheapest_parking}.\nPrix : {min_price}")


def exo5(data):
    # Initialiser le dictionnaire pour stocker les prix pour chaque type de tarification
    prices_by_type = {}

    # Parcourir les parkings
    for parking in data['values']:
        # Parcourir les offres
        for offer in parking['offer']:
            # Extraire le nom de la tarification et le prix
            name = offer['schema:priceSpecification'][0]['schema:name']
            price = float(offer['schema:priceSpecification'][0]['schema:price'])

            # Ajouter le prix à la liste des prix pour ce type de tarification
            if name in prices_by_type:
                prices_by_type[name].append(price)
            else:
                prices_by_type[name] = [price]

    # Calculer et afficher la moyenne des prix pour chaque tarification
    for name, prices in prices_by_type.items():
        average_price = round(sum(prices) / len(prices), 2)
        print(f"Moyenne des prix pour la tarification {name} : {average_price}€")



#########################################
#####   FONCTION PRINCIPALE MAIN    #####
#########################################
def main():
    # Appel des fonctions de recuperation et ecriture des donnees
    mydatas = get_datas(True)
    write_datas(config.lpa_json, mydatas)

    exo2(mydatas)

if __name__ == "__main__":
    main()


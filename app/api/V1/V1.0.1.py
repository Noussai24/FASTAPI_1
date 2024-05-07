import requests
import json


def fetch_and_save_data():
    url = "https://www.ebi.ac.uk/chembl/api/data/assay?target_chembl_id=CHEMBL231&relationship_type=has_target&type=B"
    payload = {}
    headers = {
        'Cookie': 'X-Mapping-hgegjgnp=20E1F173436CFB52A3BE34C376F58D93'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)  # Ajout pour voir le texte de la réponse

    if response.status_code == 200:
        try:
            # Tentative de sauvegarde de la réponse JSON
            data = response.json()
            with open('models_data.json', 'w') as file:
                json.dump(data, file)
            print("Data saved to models_data.json")
        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

# Appel de la fonction
fetch_and_save_data()

# -*- coding: utf-8 -*-

class Maps:
    """Classe dont le but est de récupérer les infos google maps"""
    def __init__(self):
        pass

    def get_adresse(texte, clef):
        """méthode destinée à récuper l'adresse"""
        import requests
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        
        demande = { 
            'key' : clef,
            'input' : texte,
            'inputtype' : 'textquery',
            'fields' : 'formatted_address'
        }
        
        reponse = requests.get(url, demande)
        
        adresse = reponse.json()
        
        return adresse['candidates'][0]['formatted_address']
        
    def get_carte(adresse, clef):
        """méthode destinée à récupérer l'url pour afficher une carte"""
        url_base = "https://www.google.com/maps/embed/v1/place?key=" + clef
        
        # demande = {
            # 'center' : adresse,
            # 'zoom' : '10',
            # 'key' : clef
        # }
        
        url_demande = "&q=" + adresse
        
        url_maps = url_base + url_demande
        
        return url_maps

# import pytest
# pytest.main()
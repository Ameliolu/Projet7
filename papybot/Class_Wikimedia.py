# -*- coding: utf-8 -*-

class Wikimedia:
    """Classe dont le but est de récupérer la synthèse wikipedia"""
    def __init__(self):
        pass

    def synthese(texte):
        import requests

        url = "https://fr.wikipedia.org/w/api.php"

        demande = {
            "action": "opensearch",
            "namespace": "0",
            "search": texte,
            "limit": "1",
            "format": "json"
        }

        reponse = requests.get(url, demande)
        data = reponse.json()

        histoire = str(data[2][0])
        
        return histoire
        
#    def get_info(search):
#        import requests
#        """Grab some info on wikipedia"""
#        endpoint = "https://fr.wikipedia.org/w/api.php"
#        payload = {
#            'action':'opensearch',
#            'search':search,
#            'format':'json'
#        }
#
#        resp = requests.get(endpoint, payload)
#        data = resp.json()
#        return data

# import pytest
# pytest.main()
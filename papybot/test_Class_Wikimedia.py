# -*- coding: utf-8 -*-

import requests
from json import loads

from Class_Wikimedia import *


def test_synthese(monkeypatch):
    def fake_synthese(url, demande):
        class FakeResponse():
#            @staticmethod
            def json():
                results = """
                            [
                                "truc1",
                                [
                                    "truc2"
                                ],
                                [
                                    "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement."
                                ],
                                [
                                    "https://fr.wikipedia.org/wiki/Tour_Eiffel"
                                ]
                            ]
                """
                return loads(results)
        return FakeResponse
        
    fake_results = "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement."
    
    monkeypatch.setattr(requests, 'get', fake_synthese)
    histoire = Wikimedia.synthese('Tour Eiffel')
    assert histoire == fake_results
    
#def test_get_info(monkeypatch):
#    def fake_get(endpoint, payload):
#        class FakeResponse():
#            @staticmethod
#            def json():
#                results = """
#                            [
#                                "openclassrooms",
#                                [
#                                    "OpenClassrooms"
#                                ],
#                                [
#                                    "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM."
#                                ],
#                                [
#                                    "https://fr.wikipedia.org/wiki/OpenClassrooms"
#                                ]
#                            ]
#                """
#                return loads(results)
#        return FakeResponse
#
#    monkeypatch.setattr(requests, 'get', fake_get)
#    expected_info = "OpenClassrooms est une école en ligne"
#    expected_wiki = "https://fr.wikipedia.org/wiki/OpenClassrooms"
#
#    resp = Wikimedia.get_info('Openclassrooms')
#    assert expected_info in resp[2][0]
#    assert resp[3][0] == expected_wiki
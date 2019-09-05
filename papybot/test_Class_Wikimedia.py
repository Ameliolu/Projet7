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
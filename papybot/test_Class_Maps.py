# -*- coding: utf-8 -*-

import requests
from json import loads

from Class_Maps import *

def test_get_adresse(monkeypatch):
    def fake_get_adresse(url, demande):
        class FakeResponse():
            def json():
                results = """
                            {
                                "candidates": [
                                    {
                                        "formatted_address":"140 George St, The Rocks NSW 2000, Australia"
                                    }
                                ]
                            }
                """
                return loads(results)
        return FakeResponse
        
    fake_results = "140 George St, The Rocks NSW 2000, Australia"
    
    monkeypatch.setattr(requests, 'get', fake_get_adresse)
    adresse = Maps.get_adresse('Museum of Contemporary Art Australia')
    assert adresse == fake_results

def test_get_carte():
    fake_url = "https://www.google.com/maps/embed/v1/place?key=AIzaSyCMepGPJ5esQHtSx-5lg-K7q4WKFAidplU&q=Tour Eiffel"
    assert Maps.get_carte('Tour Eiffel') == fake_url
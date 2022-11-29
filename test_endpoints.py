""" test app endpoints with requests """
import requests
import json
import pytest
from app import app

def test_create_disk():
     """test create disk"""
     response = requests.post('http://localhost:5000/disks', json={
         'title': 'The Dark Side of the Moon',
         'artist': 'Pink Floyd',
         'genre': 'Progressive Rock'
     })
     assert response.status_code == 200
     assert response.json()['title'] == 'The Dark Side of the Moon'
     assert response.json()['artist'] == 'Pink Floyd'
     assert response.json()['genre'] == 'Progressive Rock'

def test_get_disk():
     """test get disk"""
     response = requests.get('http://localhost:5000/disks/1')
     assert response.status_code == 200
     assert response.json()['title'] == 'The Dark Side of the Moon'
     assert response.json()['artist'] == 'Pink Floyd'
     assert response.json()['genre'] == 'Progressive Rock'

def test_get_disks():
     """test get disks"""
     response = requests.get('http://localhost:5000/disks')
     assert response.status_code == 200
     assert response.json()[0]['title'] == 'The Dark Side of the Moon'
     assert response.json()[0]['artist'] == 'Pink Floyd'
     assert response.json()[0]['genre'] == 'Progressive Rock'



def test_update_disk():
    """test update disk"""
    response = requests.put('http://localhost:5000/disks/1', json={
        'title': 'The Wall',
        'artist': 'Pink Floyd',
        'genre': 'Progressive Rock'
    })
    assert response.status_code == 200
    assert response.json()['title'] == 'The Wall'
    assert response.json()['artist'] == 'Pink Floyd'
    assert response.json()['genre'] == 'Progressive Rock'

def test_delete_disk():
    """test delete disk"""
    response = requests.delete('http://localhost:5000/disks/1')
    assert response.status_code == 200
    assert response.json()['title'] == 'The Wall'
    assert response.json()['artist'] == 'Pink Floyd'
    assert response.json()['genre'] == 'Progressive Rock'

""" add example data to the database using requests"""
import requests
import json

requests.post('http://localhost:5000/disks', json={
    'title': 'The Dark Side of the Moon',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'The Wall',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Animals',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Wish You Were Here',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'The Final Cut',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'The Division Bell',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Meddle',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Atom Heart Mother',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Ummagumma',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'A Saucerful of Secrets',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'Relics',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

requests.post('http://localhost:5000/disks', json={
    'title': 'The Piper at the Gates of Dawn',
    'artist': 'Pink Floyd',
    'genre': 'Progressive Rock'
})

# VallesFullStack2022
VallesFullStack 30 Novembre 2022 Terrassa

## Configuració amb Github Codespaces

* Crear Repositori o fer Fork
  * https://github.com/eloipuertas/VallesFullStack2022
* <>Code:  Create codespaces
  * Si heu seguit els passos anteriors de configuració de Github Copilot us hauria de sortir el logo del Copilot a sota.
* Crear el fitxer **requirements.txt**
* Afegir un *Dev Container Configuration file* (ctrl-shift-p): Python 3 i vue client. Descomentar postcreateCommand i forward port 5000.
* Activar **Settings Sync** per no haver d’instal·lar les extensions de VS code altre cop (Copilot)
* Tornar a compilar

## BackEnd
* Crear fitxer `app.py`
* Escriure: `Flask application setup`
* Prémer `Return` i acceptar amb el `tabulador` els imports.
* Obrir Panell de suggeriments amb `Control+Enter`.
* Mirar si hi ha algun tros de codi amb que començar l’applicació, si no seguir amb el `return/tab`.
* Continuar amb `#initiate the flask app` i acceptar tota la funció 
* Continuar amb `#create the app`
  
## BackEnd
* Afegir ruta per defecte amb `add main root route`
* Continuar amb `#run app` 
* Actualitzar els `requirements` i  fer un `ctrl-shift-P `Full Rebuild Container 
* Provar el resultat en el terminal amb un flask run 

## Crear Model 
* Escriure: 
  ```python
  """
  Models, 
  Create a Disk model with title, artist, and genre fields
  """
  ```
* Acceptar la classe proposta.
* Escriure: 
  ```python
  """ GET endpoint for a single Disk in the model “””
  “”” POST endpoint for Disk model “””
  “”” PUT endpoint for Disk model “””
  “”” DELETE endpoint for Disk model “””
  
  #Create models in database with context manager
  ```

## Testejar els endpoints
* Crear fitxer `test_endpoints.py`
* Escriure:
  ```python
  """
  test app endpoints with requests
  """
  ```
* Començar a escriure 
  ```python 
  def test_create_disk()
  ```
* afegir `requests` al requirements i tornar a carregar l’entorn.
* Executar pytest des de Testing

## Afegir dades a la base de dades
* Crear fitxer `add_data_db.py`
* Escriure: 
```python
"""
 add example data to the database using requests
"""
```
* `Ctrl+Enter` i acceptar l’exemple més llarg.
* Executar el fitxer amb `python add_data_db.py`
* Comprovar que s’han afegit les dades en el fitxer `db.sqlite`

## Crear FrontEnd
* Crear un projecte vue, des del terminal amb `vue create client`
* Crear un nou component anomenat `Disk.vue`
* Escriure:
    ```html
     <!— template for the disk model with tilte, artist and genre —>
     ```
* Obrir amb Ctrl Enter la llista de suggerències i agafar la que sigui més complerta.
* Crear i omplir els fitxers `App.vue` i `DiskList.vue` amb les suggerències.
* Especificar en la funció `fetch` la URL del backend a producció.
* Fer públics els ports del codespace
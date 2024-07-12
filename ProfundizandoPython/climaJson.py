import json
import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    'https://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    # contenido = mensaje.read()
    jsonRespuesta = json.loads(mensaje.read().decode('utf-8'))
    print(jsonRespuesta)

for valor in jsonRespuesta["clima"]:
    print(f'Descripcion del clima: {valor["descripcion"]}')

print(f'Temperatura Minima: {jsonRespuesta["principal"]["temp_min"]}')
print(f'Temperatura Maxima: {jsonRespuesta["principal"]["temp_max"]}')



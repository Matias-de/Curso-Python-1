#leer json
import json
import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    # contenido = mensaje.read()
    jsonRespuesta = json.loads(mensaje.read().decode('utf-8'))
    print(jsonRespuesta)


for persona in jsonRespuesta['personas']:
    print(f'Persona: {persona["nombre"]}, {persona["edad"]}')

#accedemos a las variables independientes
print(f'Total de personas: {jsonRespuesta["total"]}')

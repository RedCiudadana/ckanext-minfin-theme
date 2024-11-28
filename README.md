[![Tests](https://github.com/RedCiudadanana/ckanext-minfin-theme/workflows/Tests/badge.svg?branch=main)](https://github.com/RedCiudadanana/ckanext-minfin-theme/actions)

# ckanext-minfin-theme

## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.11             | yes    |

Suggested values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

To install ckanext-minfin-theme:

1. Activate your CKAN virtual environment, for example:
    . /usr/lib/ckan/default/bin/activate

2. Clone the source in `src` and install it on the virtualenv:
    git clone https://github.com/RedCiudadanana/ckanext-minfin-theme.git
    cd ckanext-minfin-theme
    python setup.py develop
    pip install -r requirements.txt

3. Add `minfin-theme` to the `ckan.plugins` setting in your CKAN
    config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Nginx on Ubuntu:
    sudo service nginx reload

## Config settings

List of package to be listed in the home

`ckan.featured_packages = package-1 package-2 package-3`

## Developer installation

To install ckanext-minfin-theme for development:

1. Activate your CKAN virtual environment, for example:
    . /usr/lib/ckan/default/bin/activate

2. Clone the source in `src` and install it on the virtualenv:
    git clone https://github.com/RedCiudadanana/ckanext-minfin-theme.git
    cd ckanext-minfin-theme
    python setup.py develop
    pip install -r dev-requirements.txt

## Configure featured packages in home

Add the featured package to the parameter
```
ckan.featured_packages = package_1 package_2
```

## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini

## How to update the plugin

To update ckanext-minfin-theme for development:

1. Activate your CKAN virtual environment, for example:
    . /usr/lib/ckan/default/bin/activate

2. Clone the source in `src` and update it on the virtualenv:
    cd ckanext-minfin-theme
    git pull
    pip install -r requirements.txt

3. Restart uwsgi processes:
    supervisorctl restart all

## Sitemap example

Add in a CKAN page

```
<ul>
    <li><a href="/pages/datos-abiertos">Datos Abiertos</a></li>
    <li><a href="/dataset">Conjunto de datos</a></li>
    <li><a href="/group">Categorías de datos</a></li>
    <li><a href="/pages/historias">Historias de Usuarios</a></li>
    <li><a href="/pages/videos">Video Tutoriales</a></li>
    <li><a href="/pages/eventos">Eventos</a></li>
    <li><a href="/pages/estadisticas">Estadísticas</a></li>
    <li><a href="/pages/infografias">Infografías</a></li>
    <li><a href="/pages/politica-de-publicacion">Política de Publicación</a></li>
    <li><a href="/pages/documentos">Documentación</a></li>
    <li><a href="/pages/preguntas-frecuentes">Preguntas frecuentes</a></li>
    <li><a href="/pages/reporta-un-problema">Reporta un problema</a></li>
    <li><a href="/pages/evalua">Evalúa</a></li>
    <li><a href="/about">Acerca de</a></li>
</ul>
```

You need to create the following pages

- /pages/datos-abiertos
- /pages/historias
- /pages/videos
- /pages/eventos
- /pages/estadisticas
- /pages/infografias
- /pages/politica-de-publicacion
- /pages/documentos
- /pages/preguntas-frecuentes
- /pages/mapa-sitio
- /pages/preguntas
- /pages/reporta-un-problema
- /pages/evalua

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)

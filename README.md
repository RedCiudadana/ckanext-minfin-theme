[![Tests](https://github.com//ckanext-minfin-theme/workflows/Tests/badge.svg?branch=main)](https://github.com//ckanext-minfin-theme/actions)

# ckanext-minfin-theme

**TODO:** Put a description of your extension here:  What does it do? What features does it have? Consider including some screenshots or embedding a video!


## Requirements

**TODO:** For example, you might want to mention here which versions of CKAN this
extension works with.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.11             | not tested    |

Suggested values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-minfin-theme:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com//ckanext-minfin-theme.git
    cd ckanext-minfin-theme
    pip install -e .
	pip install -r requirements.txt

3. Add `minfin-theme` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.minfin_theme.some_setting = some_default_value


## Developer installation

To install ckanext-minfin-theme for development, activate your CKAN virtualenv and
do:

    git clone https://github.com//ckanext-minfin-theme.git
    cd ckanext-minfin-theme
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-minfin-theme

If ckanext-minfin-theme should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## Sitemap example
Add in a CKAN page

```
<a href="/pages/datos-abiertos">Datos Abiertos</a>
<a href="/dataset">Conjunto de datos</a>
<a href="/group">Categorías de datos</a>
<a href="/pages/historias">Historias de Usuarios</a>
<a href="/pages/videos">Video Tutoriales</a>
<a href="/pages/eventos">Eventos</a>
<a href="/pages/estadisticas">Estadísticas</a>
<a href="/pages/infografias">Infografías</a>
<a href="/pages/politica-de-publicacion">Política de Publicación</a>
<a href="/pages/documentos">Política de Publicación</a>
<a href="/pages/preguntas-frecuentes">Política de Publicación</a>
<a href="/about">Acerca de</a>
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

## Configure featured packages in home
Add the featured package to the parameter
```
ckan.featured_packages = package_1 package_2
```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)

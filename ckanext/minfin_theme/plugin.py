from __future__ import annotations

from ckan.common import config
from ckan.types import Schema
from ckanext.pages.interfaces import IPagesSchema
import ckan.logic as logic
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


from .middleware import track_request, add_csp

def get_theme_parameters():
    return {
        'minfin_theme_feedback_embed': toolkit.config.get('ckanext.minfin_theme.feedback_embed')
    }

def get_pages_in_home():
    # Define parameters for the action (if any)
    data_dict = {
        'in_home': True  # Filter by `in_home=True` if supported by the action
    }
    
    # Call the action
    try:
        pages = toolkit.get_action('ckanext_pages_list')({}, data_dict)
    except toolkit.ObjectNotFound:
        pages = []

    return pages

def get_popular_packages(limit):
    result = []
    try:
        packages = toolkit.get_action('package_search')({}, {
            'sort': 'views_recent desc',
            'rows': 3,
        })

        result = packages['results']
    except:
        result = []

    return result

def get_featured_packages():
    count = 3
    featured_packages = config.get('ckan.featured_packages', '')

    if not featured_packages:
        return False
    
    items = [item.strip() for item in featured_packages.split(' ') if item.strip()]

    packages_data = []
    found = []
    for package_name in items:
        try:
            package = toolkit.get_action('package_show')({}, { 'id': package_name })
        except logic.NotFound:
            continue

        if not package:
            continue

        if package['id'] in found:
            continue

        found.append(package['id'])
        packages_data.append(package)

        if len(packages_data) == count:
            break

    return packages_data

def get_extra_value(extras, key):
    """Fetch the value of an extra field by key."""
    for extra in extras:
        if extra.get('key') == key:
            return extra.get('value')
    return None

class MinfinThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IMiddleware, inherit=True)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(IPagesSchema)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "public")
        toolkit.add_resource("assets", "minfin_theme")

    def update_config_schema(self, schema: Schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        unicode_safe = toolkit.get_validator('unicode_safe')

        schema.update({
            # This is a custom configuration option
            u'ckanext.minfin_theme.feedback_embed': [ignore_missing, unicode_safe],
        })

        return schema

    # IMiddleware
    def make_middleware(self, app: CKANApp, config: CKANConfig) -> Any:
        app.before_request(track_request)
        app.after_request(add_csp)
        return app
    
    #IPagesSchema
    def update_pages_schema(self, schema):
        schema.update({
            'in_home': [
                toolkit.get_validator('boolean_validator')]
            })
        return schema


    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    #ITemplateHelpers
    def get_helpers(self):
        return {
            'get_pages_in_home': get_pages_in_home,
            'get_popular_packages': get_popular_packages,
            'get_featured_packages': get_featured_packages,
            'get_extra_value': get_extra_value,
            'get_theme_parameters': get_theme_parameters,
        }

import yaml
from collections import OrderedDict



def links_to_yaml_string(links_data):
    """
    Given a list of links in the following form
    
        {'links':[
            {  'title': 'The Python package index website',
                'url': 'https://pypi.python.org/pypi',
                'notes': 'These are extra lines that would normally go below the link'
                'URL\nvia https://www.python.org/\ncode https://github.com/python/cpython\n'},
            {   'title': 'Django web framework',
                 'url': 'https://www.djangoproject.com/',
                 'notes': 'This is a useful framework for building websites and now'
                 '\nthis continues on the next line'},
            ]
        }
    
    Returns a YAML string representation of the same data:

        links:
        - url: https://pypi.python.org/pypi
          title: The Python package index website
          notes: |
            These are extra lines that would normally go below the link URL
            via https://www.python.org/
            code https://github.com/python/cpython
        - url: https://www.djangoproject.com/
          title: Django web framework
          notes: |-
            This is a useful framework for building websites and now this continues on the next line

    """

    # Convert `links_data` to a list of OrderedDict objects
    ordered_links_data = {'links':[]}
    for link in links_data['links']:
        new_link = OrderedDict()
        new_link['url'] = link.get('url', None)
        if 'title' in link:
            new_link['title'] = link.get('title')
        if 'notes' in link:
            new_link['notes'] = link.get('notes')
        ordered_links_data['links'].append(new_link)


    # custom make OrderedDict items appear in right order + force multiline notes
    def represent_ordereddict(dumper, data):
        value = []
        for item_key, item_value in data.items():
            node_key = dumper.represent_data(item_key)
            if node_key.value == 'notes':
                node_value = dumper.represent_scalar(u'tag:yaml.org,2002:str', item_value, style='|')
            else:
                node_value = dumper.represent_data(item_value)
            value.append((node_key, node_value))
        return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)
    yaml.SafeDumper.add_representer(OrderedDict, represent_ordereddict)


    # return yaml_str
    return yaml.safe_dump(ordered_links_data, None, allow_unicode=True, default_flow_style=False, indent=2)
    
    
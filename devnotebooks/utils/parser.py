
from markdown2 import Markdown
import re
import yaml



# REs
yaml_header_re = re.compile('^---\n(?P<yaml_str>(.*?))---\n', re.DOTALL|re.MULTILINE)
link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]


def parse_page(mixed_source):
    """
    Given the mixed yaml+md source string, this function will:
      - process the links in the YAML section and turn them into a list of dicts:
          {'url':'<str>', 'title':'<str>', 'notes':'<str>'}
      - process the rest of the source using markdown2 and return it as html
    Returns (links, html)
    """
    links = []
    html = None
    
    # process YAML header
    yaml_match = yaml_header_re.match(mixed_source)
    if yaml_match:
        yaml_str = yaml_match.groupdict()['yaml_str']
        links_data = yaml.load(yaml_str)
        links = links_data['links']

    # process rest of .md file
    rests_of_source = yaml_header_re.sub('', mixed_source)
    markdown=Markdown(extras=["link-patterns"], link_patterns=link_patterns)
    html = markdown.convert(rests_of_source)
    
    return links, html


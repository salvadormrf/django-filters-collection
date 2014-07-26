import re
from urlparse import urlparse

from django import template
from django.utils.translation import ugettext


register = template.Library()


@register.filter(is_safe=False)
def smart_yesno(value, arg=None):
    """
    This is identical to Django yesno filter, but we can use the value itself
    {{ value|smart_yesno:"yes,no,maybe" }}
    {{ value|smart_yesno:"_value_,red,cyan" }}
    
    Note: _value_ is replaced
    This filter always return string
    
    ==========  ======================  ==================================
    Value       Argument                Outputs
    ==========  ======================  ==================================
    ``hello``   `"_value_,no,maybe"``   ``hello``
    ``hello``   `"id-_value_-car,no,maybe"``   ``id-hello-car``
    ==========  ======================  ==================================
    """
    if arg is None:
        arg = ugettext('yes,no,maybe')
    bits = arg.split(',')
    if len(bits) < 2:
        return value  # Invalid arg.
    try:
        yes, no, maybe = bits
    except ValueError:
        # Unpack list of wrong size (no "maybe" value provided).
        yes, no, maybe = bits[0], bits[1], bits[1]
    if value is None:
        return maybe
    if value:
        if '_value_' in yes:
            yes = yes.replace('_value_', str(value))
        return yes
    return no


@register.filter
def pretty_url(value):
    """
    Returns a pretty hostname for a given url
    
    ==================================  ==================================
    Value                               Outputs
    ==================================  ==================================
    ``http://mywebsite.com``            ``mywebsite.com``
    ``mywebsite.com``                   ``mywebsite.com``
    ``http://mywebsite.com/page.html``  ``mywebsite.com``
    ``http://www.mywebsite.com``        ``www.mywebsite.com``
    ``admin.mywebsite.com``             ``admin.mywebsite.com``
    ``mailto:someone@example.com``      ``mailto:someone@example.com``
    ==================================  ==================================
    """
    if value in (None, True, False, ''):
        return ''
    
    url = str(value)
    o = urlparse(url)
    
    if o.scheme == 'http':
        return o.hostname
    elif o.scheme == '':
        # missing protocol, add http
        _o = urlparse("http://%s" % url)
        return _o.hostname or url
    else: # other protocol
        return o.hostname or o.netloc or o.path
    

@register.filter
def strip_protocol(value):
    """
        Strips protocol for a given URL
        http://mywebsite.com/page1    mywebsite.com/page1
    """
    if value in (None, True, False, ''):
        return ''

    url = str(value)
    o = urlparse(url)
    
    netloc = o.netloc
    if not netloc and o.scheme == '':
        # missing protocol, add http
        o = urlparse("http://%s" % url)
        netloc = o.netloc
    
    substr = netloc or o.path
    if substr:
        index = url.find(substr)
        if index:
            return url[index:]
    return url


@register.filter
def strip_vowels(value):
    """
        Strips all vowels from a given string
    """
    if value in (None, True, False, ''):
        return ''
    result = re.sub(r'[AEIOU]', '', value, flags=re.IGNORECASE)
    return result
    
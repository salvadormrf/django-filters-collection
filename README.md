django-filters-collection
=========================

A collection of reusable Django template filters and tags


    
    # This is identical to Django yesno filter, but we can use the value itself
    # {{ value|smart_yesno:"_value_,red,cyan" }}
    # {{ "hello"|smart_yesno:"id-_value_-,red,cyan" }}   result: id-hello-car
    smart_yesno 
    
    # Returns a pretty hostname for a given url
    pretty_url
    
    # Strips protocol for a given URL
    strip_protocol
    
    # Strips all vowels from a given string
    strip_vowels


More... doing some refactoring and adding tests before adding to git repo.



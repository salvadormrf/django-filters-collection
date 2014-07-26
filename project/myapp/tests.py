from django.test import TestCase


from .templatetags.filters import (smart_yesno, pretty_url, strip_protocol, strip_vowels)


class DefaultFiltersTests(TestCase):
    
    def test_smart_yesno(self):
        self.assertEqual(smart_yesno(True), 'yes')
        self.assertEqual(smart_yesno(False), 'no')
        self.assertEqual(smart_yesno(None), 'maybe')
        self.assertEqual(smart_yesno(True, 'certainly,get out of town,perhaps'),
                         'certainly')
        self.assertEqual(smart_yesno(False, 'certainly,get out of town,perhaps'),
                         'get out of town')
        self.assertEqual(smart_yesno(None, 'certainly,get out of town,perhaps'),
                         'perhaps')
        self.assertEqual(smart_yesno(None, 'certainly,get out of town'),
                         'get out of town')
        self.assertEqual(smart_yesno('hello', 'yessir,nosir,maybesir'),
                         'yessir')
        self.assertEqual(smart_yesno('hello', '_value_,nosir,maybesir'),
                         'hello')
        self.assertEqual(smart_yesno('hello', 'hey _value_ world,nosir,maybesir'),
                         'hey hello world')
    
    def test_pretty_url(self):
        self.assertEqual(pretty_url(True), '')
        self.assertEqual(pretty_url(False), '')
        self.assertEqual(pretty_url(None), '')
        self.assertEqual(pretty_url('http://mywebsite.com'), 'mywebsite.com')
        self.assertEqual(pretty_url('http://www.mywebsite.com'), 'www.mywebsite.com')
        self.assertEqual(pretty_url('mywebsite.com'), 'mywebsite.com')
        self.assertEqual(pretty_url('admin.mywebsite.com'), 'admin.mywebsite.com')
        self.assertEqual(pretty_url('http://mywebsite.com/index.html'), 'mywebsite.com')
        self.assertEqual(pretty_url('mailto:someone@example.com'), 'someone@example.com')
        self.assertEqual(pretty_url('ftp://public.mywebsite.com/mydirectory/myfile.txt'), 
                         'public.mywebsite.com')
    
    def test_strip_protocol(self):
        self.assertEqual(strip_protocol(True), '')
        self.assertEqual(strip_protocol(False), '')
        self.assertEqual(strip_protocol(None), '')
        self.assertEqual(strip_protocol('http://mywebsite.com'), 'mywebsite.com')
        self.assertEqual(strip_protocol('http://www.mywebsite.com'), 'www.mywebsite.com')
        self.assertEqual(strip_protocol('mywebsite.com'), 'mywebsite.com')
        self.assertEqual(strip_protocol('admin.mywebsite.com'), 'admin.mywebsite.com')
        self.assertEqual(strip_protocol('http://mywebsite.com/index.html'), 'mywebsite.com/index.html')
        self.assertEqual(strip_protocol('mailto:someone@example.com'), 'someone@example.com')
        self.assertEqual(strip_protocol('ftp://public.mywebsite.com/mydirectory/myfile.txt'), 
                         'public.mywebsite.com/mydirectory/myfile.txt')
    
    def test_strip_vowels(self):
        self.assertEqual(strip_vowels(True), '')
        self.assertEqual(strip_vowels(False), '')
        self.assertEqual(strip_vowels(None), '')
        self.assertEqual(strip_vowels('aeiou'), '')
        self.assertEqual(strip_vowels('drive my car'), 'drv my cr')
        self.assertEqual(strip_vowels('my car is blue'), 'my cr s bl')
        self.assertEqual(strip_vowels('lorem ipsum'), 'lrm psm')
        self.assertEqual(strip_vowels('gym'), 'gym')
        








    
            
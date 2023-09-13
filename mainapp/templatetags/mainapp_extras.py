from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe



register = template.Library()

def my_upper(value,arg):

    value = value.upper()

    return value + arg

def alphabets(value):

    value = value.isalpha() 

    return value   
    
register.filter(alphabets)
register.filter(my_upper)


# using decorators

@ register.filter

def lower(value):

    return value.lower()


# for simple tags

@ register.simple_tag
def hello():
    a = "Hello World!"
    return a

# with filter name

@ register.filter(name="check_words")

def check_words(value):

    return len(value.split())


# Template filters that expect strings

@ register.filter
@ stringfilter

def swap_string(value):

    return value.swapcase()


# safeString

@register.filter(is_safe=True)
def add_xx(value):
    return "%sxx" % value




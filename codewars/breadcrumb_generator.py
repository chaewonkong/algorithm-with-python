"""Breadcrumb Generator

from Codewars
URL: https://www.codewars.com/kata/breadcrumb-generator

What might not be so trivial is instead to get a decent breadcrumb 
from your current url. 
Create a function that takes a url, 
strips the first part (labelling it always HOME) and then builds it making each element 
but the last a <a> element linking to the relevant path; 
last has to be a <span> element getting the active class.

All elements need to be turned to uppercase and separated by a separator, 
given as the second parameter of the function; 
the last element can terminate in some common extension like .html, .htm, .php or .asp; 
if the name of the last element is index.something, you treat it as if it wasn't there, 
sending users automatically to the upper level folder.

A few examples can be more helpful than thousands of words of explanation, 
so here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") 
    == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") 
    == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") 
    == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

if one element (other than the root/home) is longer than 30 characters, 
you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); 
url will be always given in the format this-is-an-element-of-the-url 
and you should ignore words in this array while acronymizing: 
["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; 
a url composed of more words separated by - and equal or less than 
30 characters long needs to be just uppercased with hyphens replaced by spaces.

(examples)
generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") 
    == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") 
    == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
"""


def generate_bc(url, separator):
    ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    ret = ""
    if "//" in url:
        url = "".join(url.split("//")[1:])
    uri = url.split("/")[1:]
    if uri and 'index.' in uri[-1]:
        uri = uri[:-1]
    if uri:
        ret += '<a href="/">HOME</a>'
    if not "".join(uri):
        return '<span class="active">HOME</span>'
    file_name = uri.pop()
    file_name = [a for b in file_name.split("#") for a in b.split("?")][0]
    file_name = file_name.split(".")[0]
    if len(file_name) > 30:
        file_name = "".join([item[0] for item in file_name.split("-") if item not in ignore])
    file_name = " ".join(file_name.split("-"))
    # REST PATH
    tmp = "/"
    for el in uri:
        title = el
        if len(el) > 30:
            title = "".join([item[0] for item in el.split("-") if item not in ignore])
        if not el:
            continue
        if "." in el:
            continue
        tmp += el + "/"
        title = " ".join(title.split("-"))
        ret += separator +'<a href="{}">{}</a>'.format(tmp, title.upper())
    
    ret += separator + '<span class="active">{}</span>'.format(file_name.upper())

    return ret


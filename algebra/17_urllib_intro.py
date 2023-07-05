# Naučit ćemo kako pomoću Python poslati GET upite na web servere i onda kako parsirati response

# U browseru pristupamo web stranici tako što upišemo URL u address bar
# URL - Uniform Resource Locator
    # Protokol -> http, https, ftp, ...
    # Host name -> en.wikipedia.org, nekad imamo i : nakon čega je naveden port (http 80, https 443)
    # Path -> wiki/URL
    # nakon ? slijedi query string -> key - value parovi odvojeni s &

# urllib ima 5 modula - request, response, error, parse, robotparse

# import urllib
# print(dir(urllib))

from urllib import request
# print(dir(request))

resp = request.urlopen("https://en.wikipedia.org/wiki/Main_Page")
# print(type(resp))

# print(dir(resp))
# print(resp.code)
# print(resp.length)

# print(resp.peek())

data = resp.read()
print(type(data))
print(dir(data))
# utf - 8
html = data.decode("UTF-8")
print(type(html))


# https://www.youtube.com/watch?v=LosIGgon_KM

from urllib import parse

print(dir(parse))

params = {"v": "LosIGgon_KM"}
querystring = parse.urlencode(params)

print(querystring)

url = 'https://www.youtube.com/watch' + '?' + querystring

resp = request.urlopen(url)

print(resp.isclosed())
print(resp.code)

html = resp.read().decode('utf-8')
print(html)
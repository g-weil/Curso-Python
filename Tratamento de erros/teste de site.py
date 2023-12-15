# Crie um código em Python que teste se o site youtube está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')

except urllib.error.URLError:
    print('O site não está funcionando! ')

else:
    print('Esta funcionando! ')
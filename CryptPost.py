# -----------------------------------------------------------
# Hakee webbisivun ja lukee sieltä halutut rivit. Tämän jälkeen postaa rivit kryptattuna ja printtaa vastauksen sivulta.
# -----------------------------------------------------------

from urllib.request import build_opener, HTTPCookieProcessor
import  urllib.parse
import hashlib
from http.cookiejar import CookieJar

#Tehdään paikka cookielle ja opener jotta saadaan sama cookie käyttöön
cookie_jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(cookie_jar))
    
#Avaa sivun
contents = opener.open("LISÄÄ SIVU")
lines = contents.readlines()
kryptattava = lines[5][66:86] # Muokkaa rivit halutuiksi
kryptattu = hashlib.md5(kryptattava).hexdigest()

#Laitetaan kryptattu salasana postattavaksi oikeaan muotoon
post_data = urllib.parse.urlencode({'hash' : kryptattu}).encode('ascii')

#Postataan samalla openerilla kryptattu salasana ja otetaan vastaus talteen, joka tulostetaan
vastaus = opener.open("LISÄÄ SIVU", post_data)
print(vastaus.read())


from urllib.request import urlopen
link = "https://www.python.org/"


def get_html():
    try:
        http_rsp = urlopen(link)    #Client starten
        #print(http_rsp)
        html = http_rsp.read()       # HTML holen
        #print(html)
        html_decoded = html.decode() # HTML aufbereiten
        print(html_decoded)

    except Exception as ex:
        print('***Failed to get HTML!***\n\n' + str(ex))
    else:
        return html_decoded
import os

class configuration:
    environment = 'test'
    browser = 'CHROME'
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    path_evidencias = basedir + "\\data\\screenshots"
    Json = basedir + "\\pages"

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'\data\data.xlsx'

    if environment == 'test':
        scenario = {}
        scenario['MiVariable'] = "XXXXX"
        scenario['Test001'] = "hola Joe"

        URL = "https://www.spotify.com/py/signup/"

    if environment == 'dev':
        scenario = {}
        scenario['MiVariable'] = "XXXXX"
        scenario['Test001'] = "hola Joe"
        URL = "https://www.amazon.com/"
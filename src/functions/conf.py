import os


class configuration:
    environment = 'test'
    browser = 'CHROME'
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    path_evidencias = basedir + "\\data\\screenshots"
    Json = basedir + "\\pages"

    if environment == 'test':
        URL = "https://www.spotify.com/py/signup/"

    if environment == 'dev':
        URL = "https://www.amazon.com/"
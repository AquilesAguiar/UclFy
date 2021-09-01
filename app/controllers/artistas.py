import requests
class artistas():
    def __init__(self,artista):
        self.data = requests.get('https://theaudiodb.com/api/v1/json/1/search.php?s={0}'.format(artista)).json()
    
    def retornaId(self):
        id = self.data['artists'][0]['idArtist']
        return id

    def retonarArtista(self):
        self.artista = requests.get('https://theaudiodb.com/api/v1/json/1/artist.php?i={0}'.format(self.retornaId())).json()
        self.artista = self.artista['artists'][0]
        site = self.artista['strWebsite']
        face = self.artista['strFacebook']
        twitter = self.artista['strTwitter']

        site = site.strip('www').strip('.com')
        face = face.strip('www.facebook.com/')
        twitter = twitter.strip('www.twitter.com/')
        jsonArtistas = {
            'nome':self.artista['strArtist'],
            'gravadora':self.artista['strLabel'],
            'anoCriacao':self.artista['intFormedYear'],
            'estilo':self.artista['strStyle'],
            'genero':self.artista['strGenre'],
            'site':'https://www.'+site+'.com',
            'facebook':'https://www.facebook.com/'+face,
            'twitter':'https://twitter.com/'+twitter,
            'biografia':self.artista['strBiographyPT'] if self.artista['strBiographyPT'] != None else self.artista['strBiographyEN'],
            'qtd_integrantes':self.artista['intMembers'],
            'pais':self.artista['strCountry'],
            'logo':self.artista['strArtistLogo']
        }
        return jsonArtistas
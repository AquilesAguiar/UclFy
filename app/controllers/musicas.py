import requests
class musicas():
    def __init__(self,id):
        self.album = requests.get('https://theaudiodb.com/api/v1/json/1/album.php?i={0}'.format(id)).json()
    
    def albumInf(self):
        albumInfo = self.album['album']
        self.jsonAlbum = {
            'idAlbum':[],
            'idArtista':0,
            'nomeAlbum':[],
            'nomeArtista':'',
            'anoLacamento':[],
            'estilo':'',
            'genero':'',
            'gravadora':[],
            'descricao':[],
            'logo':[]
        }
        self.jsonAlbum['idArtista'] = albumInfo[0]['idArtist']
        self.jsonAlbum['nomeArtista'] = albumInfo[0]['strArtist']
        self.jsonAlbum['estilo'] = albumInfo[0]['strStyle']
        self.jsonAlbum['genero'] = albumInfo[0]['strGenre']

       
        for albuns in albumInfo:
            self.jsonAlbum['idAlbum'].append(albuns['idAlbum'])
            self.jsonAlbum['nomeAlbum'].append(albuns['strAlbum'])
            self.jsonAlbum['anoLacamento'].append(albuns['intYearReleased'])
            self.jsonAlbum['gravadora'].append(albuns['strLabel'])
            if 'strDescriptionPT' in albuns and 'strDescriptionEN' in albuns:
                self.jsonAlbum['descricao'].append(albuns['strDescriptionPT']  if albuns['strDescriptionPT'] != None else albuns['strDescriptionEN'])
            else:
                self.jsonAlbum['descricao'].append('')
            self.jsonAlbum['logo'].append(albuns['strAlbumThumb'])
        return self.jsonAlbum
from flask import Flask,render_template,request
from controllers.artistas import artistas
from controllers.musicas import musicas


app = Flask('uclFy')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def pesqArtista():
    try:
        # Artista pesquisado
        artistaPesq = request.form['pesq']

        # Instanciando classe artista passando o artista pesquisado
        artista = artistas(artistaPesq)
        # Id do artista
        id = artista.retornaId()
        
        # Retornando json com informações dos artistas
        bandaInfo = artista.retonarArtista()
        #----------------------------------------------------------------------------------
       
        # Instanciando classe de musica passando o id do artista
        musicasInf = musicas(id)
        infoalbum = musicasInf.albumInf()
        musicasAlbum = musicasInf.musicaAlbumInf()
        return render_template('index.html')
        
    except Exception as e:
        print(str(e))
        return render_template('index.html')


app.run(debug=True,use_reloader=True)
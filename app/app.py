from flask import Flask,render_template,request,flash,redirect
from controllers.artistas import artistas
from controllers.musicas import musicas
import os

app = Flask('uclFy')

app.config['SECRET_KEY'] = os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infoBanda',methods=['GET'])
def pesqArtista():
    try:
        # Artista pesquisado
        artistaPesq = request.args.get('pesq')

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
        videos = musicasInf.retornaVideos()
        return render_template('infoBanda.html',bandaInfo = bandaInfo,infoalbum = infoalbum,musicasAlbum = musicasAlbum,videos=videos)

    except Exception as e:
        print(e)
        flash("Nenhuma Informação encontrada dessa Banda/Artista",'warning')
        return render_template('index.html')


app.run(debug=True,use_reloader=True)
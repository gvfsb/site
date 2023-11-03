from projetoflask import app, database

if __name__ == '__main__':  # Tudo só vai rodar se eu estiver dentro do arquivo main.py
    # Consigo modificar o site e ver essa edição, sem precisar ficar parando de rodar toda hora.
    app.run(debug=True)

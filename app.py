from flask import Flask
app = Flask(__name__)

@app.route('/')
def nomes_grupo():
    dici_grupo = {
        'Marina Sparapani da Silva': '2200808',
        'Rafael Vitor Genaro de Oliveira': '2201287',
        'Guilherme da Silva Oliveira': '2201024',
        'Marcelo costa Miklos': '2200141'
    }

    pessoas_grupo = list(dici_grupo.keys())
    info = []
    for i in range(4):
        info.append(f"Nome: {pessoas_grupo[i]} RA:{dici_grupo[pessoas_grupo[i]]}")
    return '<p>' + '<br>'.join(info) + '</p>'

if __name__ == '__main__':
    app.run(debug=True)
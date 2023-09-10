from flask import Flask, render_template

app = Flask(__name__)

class Aluno:
    def __init__(self, id, nome, nota, media, situacao):        
        self.id = id
        self.nome = nome
        self.nota = nota
        self.media = media
        self.situacao = situacao

a1 = Aluno(1, "Robson", 10, 10, "Aprovado")
a2 = Aluno(2, "Renata", 4, 4, "Reprovada")
a3 = Aluno(3, "Guilherme", 2, 2, "Reprovado")

alunos = []
alunos.append(a1)
alunos.append(a2)
alunos.append(a3)

@app.route("/")

def index():
    return render_template("index.html", alunos = alunos)

app.run(debug=True)
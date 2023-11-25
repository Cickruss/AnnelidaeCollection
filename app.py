from flask import Flask, render_template, request
from Domain.Application.UseCases.EnviarDadosGraficos import UseCaseEnviarDadosGrafico
from Domain.Application.UseCases.CadastrarOcorrencia import UseCaseCadastrarOcorrencia
from Domain.Core.Models import Ocorrencia

__UseCaseDadosGraficos = UseCaseEnviarDadosGrafico
__UseCaseOcorrencia = UseCaseCadastrarOcorrencia
__ocorrencia = Ocorrencia

app = Flask(__name__)



@app.route('/dados', methods = ['GET'])
def Dashboard():
    viewsGraficos = __UseCaseDadosGraficos.EnviarDadosGraficos()
    return render_template("Dados.html", viewsGraficos=viewsGraficos)

@app.route('/cadastro', methods = ['GET'])
def GetFormularioOcorrencia():
    return render_template("Cadastro.html")

@app.route('/cadastro', methods = ['POST'])
def EnviarFormularioOcorrencia():
    Data = request.form['Data']
    Reino = request.form['Reino']
    Filo = request.form['Filo']
    Classe = request.form['Classe']
    Ordem = request.form['Ordem']
    Familia = request.form['Familia']
    Genero = request.form['Genero']
    Nome_cientifico = request.form['NomeCientifico']
    Localidade = request.form['Localidade']
    Estado = Localidade.split(',')[0]
    Cidade = Localidade.split(',')[1]
    GBIF = request.form['GBIF']
    ocorrencia = __ocorrencia.Ocorrencia(Data,Reino,Filo,Classe,Ordem,Familia,Genero,Nome_cientifico,Cidade,Estado, GBIF)
    responseOcorrencia = __UseCaseOcorrencia.CadastrarOcorrencia(ocorrencia)
    return render_template('Dados.html', response = responseOcorrencia)

@app.route('/mapaDensidade', methods = ['GET'])
def GetMapaDensidade():
    return render_template("Mapa.html")

if __name__ == '__main__':
    app.run()

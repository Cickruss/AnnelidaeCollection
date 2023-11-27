from flask import Flask, render_template, request
from Domain.Application.UseCases.EnviarDadosGraficos import UseCaseEnviarDadosGrafico
from Domain.Application.UseCases.CadastrarOcorrencia import UseCaseCadastrarOcorrencia
from Domain.Application.UseCases.EnviarDadosFormulario import UseCaseEnvarDadosFormulario
from Domain.Core.Models import Ocorrencia

__UseCaseDadosGraficos = UseCaseEnviarDadosGrafico
__UseCaseOcorrencia = UseCaseCadastrarOcorrencia
__UseCaseEnviarDadosFormulario = UseCaseEnvarDadosFormulario
__ocorrencia = Ocorrencia

app = Flask(__name__)



@app.route('/dados', methods = ['GET'])
def Dashboard():
    Cidades, Especies = __UseCaseDadosGraficos.EnviarDadosGraficos()
    return render_template("Dados.html", Cidades=Cidades, Especies=Especies)

@app.route('/cadastro', methods = ['GET'])
def GetFormularioOcorrencia():
    Reinos, Filos, Classes, Ordens, Familias, Generos, Especies = __UseCaseEnviarDadosFormulario.enviarDadosFormulario()
    return render_template("Cadastro.html", Reinos = Reinos, Filos = Filos, Classes = Classes,
                           Ordens = Ordens, Familias = Familias, Generos = Generos, Especies = Especies)

@app.route('/cadastro', methods = ['POST'])
def EnviarFormularioOcorrencia():
    Data = request.form['Data']
    Reino = request.form['Reino']
    Filo = request.form['Filo']
    Classe = request.form['Classe']
    Ordem = request.form['Ordem']
    Familia = request.form['Familia']
    Genero = request.form['Genero']
    Especie = request.form['Especie']
    Nome_cientifico = request.form['NomeCientifico']
    Localidade = request.form['Localidade']
    Estado = Localidade.split(',')[0]
    Cidade = Localidade.split(',')[1]
    GBIF = request.form['GBIF']
    ocorrencia = __ocorrencia.Ocorrencia(Data,Reino,Filo,Classe,Ordem,Familia,Genero,Especie,Nome_cientifico,Cidade,Estado, GBIF)
    responseOcorrencia = __UseCaseOcorrencia.CadastrarOcorrencia(ocorrencia)
    return render_template('Cadastro.html')

@app.route('/mapaDensidade', methods = ['GET'])
def GetMapaDensidade():
    return render_template("Mapa.html")

if __name__ == '__main__':
    app.run()

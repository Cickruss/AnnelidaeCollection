from flask import Flask, render_template, request
from Domain.Application.UseCases.EnviarDadosGraficos import UseCaseEnviarDadosGrafico
from Domain.Application.UseCases.CadastrarOcorrencia import UseCaseCadastrarOcorrencia
from Domain.Core.Models import Ocorrencia

__UseCaseDadosGraficos = UseCaseEnviarDadosGrafico
__UseCaseOcorrencia = UseCaseCadastrarOcorrencia
__ocorrencia = Ocorrencia

app = Flask(__name__)



@app.route('/', methods = ['GET'])
def Dashboard():

    viewsGraficos = __UseCaseDadosGraficos.EnviarDadosGraficos()
    return render_template("", viewsGraficos=viewsGraficos)

@app.route('/cadastroOcorrencia', methods = ['GET'])
def GetFormularioOcorrencia():
    return render_template()

@app.route('/cadastroOcorrencia', methods = ['POST'])
def EnviarFormularioOcorrencia():
    Data = request.form['Data']
    Reino = request.form['Reino']
    Filo = request.form['Filo']
    Classe = request.form['Classe']
    Ordem = request.form['Ordem']
    Familia = request.form['Familia']
    Genero = request.form['Genero']
    Nome_cientifico = request.form['Nome_cientifico']
    Cidade = request.form['Cidade']
    Estado = request.form['Estado']
    ocorrencia = __ocorrencia.Ocorrencia(Data,Reino,Filo,Classe,Ordem,Familia,Genero,Nome_cientifico,Cidade,Estado)
    responseOcorrencia = __UseCaseOcorrencia.CadastrarOcorrencia(ocorrencia)
    return render_template('', response = responseOcorrencia)



if __name__ == '__main__':
    app.run()

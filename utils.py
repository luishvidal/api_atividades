from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Vidal', idade='18')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Luis').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Vidal').first()
    pessoa.nome = 'Henrique'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Henrique').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()

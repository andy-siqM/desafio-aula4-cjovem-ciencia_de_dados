def faca_pergunta():
    perguntas = [
        "A criança reconhece todas as letras do alfabeto (sim/não): ",
        "A criança lê palavras simples? (sim/não): ",
        "A criança lê textos completos com fluidez? (sim/não): ",
    ]  
    pontuacao = 0 
    for pergunta in perguntas:
        resposta = input(pergunta).strip().lower()
        if resposta == 'sim':
            pontuacao += 1 
    return pontuacao

def levantar_nivel_alfabetizacao(serie, pontuacao):
    if serie == 1:
        if pontuacao == 0:
            return 'Pré-Leitor'
        elif pontuacao == 1:
            return 'Leitor Inicial'
        elif pontuacao == 2:
            return 'Leitor Intermediário'
        elif pontuacao == 3: 
            return 'Leitor Fluente'
    if serie == 2:
        if pontuacao == 0:
            return 'Pré-Leitor'
        elif pontuacao == 1:
            return 'Leitor Inicial'
        elif pontuacao == 2:  
            return 'Leitor Intermediário'
        elif pontuacao == 3: 
            return 'Leitor Fluente'
    if serie == 3: 
        if pontuacao == 0:
            return 'Pré-Leitor'
        elif pontuacao == 1:
            return 'Leitor Inicial'
        elif pontuacao == 2:  
            return 'Leitor Intermediário'
        elif pontuacao == 3: 
            return 'Leitor Fluente'
    if serie == 4:
        if pontuacao == 0:
            return 'Pré-Leitor'
        elif pontuacao == 1:
            return 'Leitor Inicial'
        elif pontuacao == 2:  
            return 'Leitor Intermediário'
        elif pontuacao == 3: 
            return 'Leitor Fluente'
						
						
def main():
    serie = int(input("Digite a série do aluno (1, 2, 3, ou 4): ").strip())
    pontuacao = faca_pergunta()
    nivel_alfabetizacao = levantar_nivel_alfabetizacao(serie, pontuacao)
    print(f'O nível de alfabetização do aluno é: {nivel_alfabetizacao}')
	
main()
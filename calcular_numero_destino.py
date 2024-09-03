def calcular_numero_destino(data):
    # Remove qualquer caractere que não seja um dígito
    numeros = ''.join(filter(str.isdigit, data))

    # Função para reduzir um número a um único dígito
    def reduzir_para_um_digito(numero):
        while len(numero) > 1:
            numero = str(sum(int(digito) for digito in numero))
        return int(numero)

    # Calcula o número do destino
    numero_destino = reduzir_para_um_digito(numeros)

    return numero_destino

def obter_significado_numero_destino(numero):
    significados = {
        1: "Número 1 - O Líder: Independente, inovador, ambicioso e com espírito pioneiro.",
        2: "Número 2 - O Diplomata: Cooperativo, sensível e valorizador de harmonia e parceria.",
        3: "Número 3 - O Comunicador: Criativo, expressivo, otimista e com talento natural para a comunicação.",
        4: "Número 4 - O Construtor: Prático, trabalhador, confiável e valoriza a ordem e a estabilidade.",
        5: "Número 5 - O Aventureiro: Busca liberdade, mudanças, aventura, e tem um espírito adaptável.",
        6: "Número 6 - O Prestativo: Responsável, amoroso, voltado para a família e busca harmonia.",
        7: "Número 7 - O Filósofo: Introspectivo, analítico, espiritual e busca sabedoria interior.",
        8: "Número 8 - O Executivo: Prático, ambicioso, focado em realizações materiais e poder.",
        9: "Número 9 - O Humanitário: Compassivo, generoso, busca fazer o bem para a humanidade.",
    }

    return significados.get(numero, "Significado não encontrado.")

def main():
    print("Bem-vindo ao Arcturus!")
    data_nascimento = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")

    # Calcula o Número de Destino
    numero_destino = calcular_numero_destino(data_nascimento)
    
    # Obtém o significado do Número de Destino
    significado = obter_significado_numero_destino(numero_destino)

    print(f"Seu Número de Destino é: {numero_destino}")
    print(f"Significado: {significado}")

if __name__ == "__main__":
    main()

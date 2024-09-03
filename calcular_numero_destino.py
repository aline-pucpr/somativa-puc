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

def main():
    print("Bem-vindo ao Arcturus!")
    data_nascimento = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")

    # Calcula o Número de Destino
    numero_destino = calcular_numero_destino(data_nascimento)

    print(f"Seu Número de Destino é: {numero_destino}")

if __name__ == "__main__":
    main()

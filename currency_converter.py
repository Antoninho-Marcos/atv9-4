def obter_dados_usuario_para_euro():
    print("Bem-vindo ao Conversor de Moedas: Reais para Euros!")
    
    while True:
        try:
            valor = float(input("Digite o valor em reais (BRL) que deseja converter para euros (EUR): "))
            if valor <= 0:
                print("Por favor, insira um valor maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido.")
    
    # Resumo dos dados inseridos
    print(f"\nResumo:")
    print(f"Valor a ser convertido: R$ {valor:.2f}")
    confirmar = input("Os dados estão corretos? (S/N): ").strip().lower()
    
    if confirmar != 's':
        print("Vamos reiniciar o processo.\n")
        return obter_dados_usuario_para_euro()
    
    return valor

def converter_brl_para_euro(valor_brl, taxa_cambio=5.5):  # Exemplo de taxa fictícia: 1 EUR = 5.5 BRL
    valor_euro = valor_brl / taxa_cambio
    return valor_euro

# Chamada principal
valor_brl = obter_dados_usuario_para_euro()
taxa_cambio_atual = 5.5  # Atualize essa taxa com valores reais de uma API de câmbio
valor_em_euro = converter_brl_para_euro(valor_brl, taxa_cambio_atual)

print(f"\nVocê deseja converter R$ {valor_brl:.2f} para EUR.")
print(f"Com a taxa de câmbio atual (1 EUR = R$ {taxa_cambio_atual:.2f}), você receberá € {valor_em_euro:.2f}.")

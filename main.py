# -*- coding: utf-8 -*-
"""
Projeto Integrador - Fase 2
Sistema de Gerenciamento de Estoque e Vendas - Garage 021
"""

def exibir_menu():
    print("\n" + "="*30)
    print("      GARAGE 021 - ESTOQUE      ")
    print("="*30)
    print("1. Cadastrar Novo Produto")
    print("2. Listar Produtos em Estoque")
    print("3. Registrar Venda")
    print("4. Exibir Relatório de Faturamento")
    print("0. Sair do Sistema")
    print("="*30)

def cadastrar_produto(estoque):
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return
        
    try:
        quantidade = int(input(f"Quantidade inicial de '{nome}': "))
        preco = float(input(f"Preço unitário de '{nome}': R$ "))
        if quantidade < 0 or preco < 0:
            print("Erro: Quantidade e preço devem ser valores positivos.")
            return
    except ValueError:
        print("Erro: Entrada inválida. Digite números válidos.")
        return

    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos(estoque):
    print("\n--- PRODUTOS EM ESTOQUE ---")
    if not estoque:
        print("O estoque está vazio.")
        return
        
    print(f"{'Produto':<20} | {'Qtd':<6} | {'Preço Unitário':<12}")
    print("-" * 45)
    for nome, dados in estoque.items():
        print(f"{nome:<20} | {dados['quantidade']:<6} | R$ {dados['preco']:.2f}")

def registrar_venda(estoque, historico_vendas):
    print("\n--- REGISTRAR VENDA ---")
    if not estoque:
        print("Não há produtos cadastrados para vender.")
        return
        
    nome = input("Digite o nome do produto vendido: ").strip()
    if nome not in estoque:
        print("Produto não encontrado no estoque.")
        return
        
    try:
        qtd_venda = int(input(f"Quantidade a vender (Disponível: {estoque[nome]['quantidade']}): "))
        if qtd_venda <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return
        if qtd_venda > estoque[nome]['quantidade']:
            print("Erro: Quantidade insuficiente em estoque.")
            return
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
        return

    # Processa a venda
    estoque[nome]["quantidade"] -= qtd_venda
    valor_total = qtd_venda * estoque[nome]["preco"]
    historico_vendas.append({"produto": nome, "quantidade": qtd_venda, "total": valor_total})
    
    print(f"Venda realizada! Total: R$ {valor_total:.2f}")

def exibir_faturamento(historico_vendas):
    print("\n--- RELATÓRIO DE FATURAMENTO ---")
    if not historico_vendas:
        print("Nenhuma venda realizada até o momento.")
        return
        
    faturamento_total = sum(venda["total"] for venda in historico_vendas)
    print(f"Total de vendas realizadas: {len(historico_vendas)}")
    print(f"Faturamento Bruto Total: R$ {faturamento_total:.2f}")

def main():
    # Estruturas de dados para o projeto
    estoque = {
        "Pneu Aro 14": {"quantidade": 12, "preco": 350.00},
        "Óleo do Motor 5W30": {"quantidade": 25, "preco": 45.90},
        "Pastilha de Freio": {"quantidade": 8, "preco": 120.00}
    }
    historico_vendas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            registrar_venda(estoque, historico_vendas)
        elif opcao == "4":
            exibir_faturamento(historico_vendas)
        elif opcao == "0":
            print("\nEncerrando o sistema Garage 021. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()s

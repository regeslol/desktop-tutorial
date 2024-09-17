Import models as aux

From database import criar_tabelas



Def main():

    Criar_tabelas()



    While True:

        Print(“1. Usar Calculadora”)

        Print(“2. Listar Cálculos”)

        Print(“3. Editar Cálculo”)

        Print(“4. Deletar Cálculo”)

        Print(“5. Calcular Lucro/Prejuízo”)

        Print(“6. Adicionar Transação Fixa”)

        Print(“7. Listar Transações Fixas”)

        Print(“8. Calcular Produto Estimado”)

        Print(“9. Informar Gastos Extraordinários”)

        Print(“10. Sair”)



        Opcao = int(input(“Escolha uma opção: “))



        If opcao == 1:

            Expressao = input(“Digite a expressão matemática (ex: 2+2*3): “)

            Try:

                Resultado = eval(expressao)

                Print(f”Resultado: {resultado}”)

            Except Exception as e:

                Print(f”Erro na expressão: {e}”)

        Elif opcao == 2:

            Calculos = aux.listar_calculos()

            For calculo in calculos:

                Print(f”ID: {calculo[0]}, Descrição: {calculo[1]}, Valor: {calculo[2]}, Data: {calculo[3]}, Tipo: {calculo[4]}”)

        Elif opcao == 3:

            Calculo_id = int(input(“ID do Cálculo a ser editado: “))

            Nova_descricao = input(“Nova Descrição: “)

            Novo_valor = float(input(“Novo Valor: “))

            Novo_tipo = input(“Novo Tipo (Lucro/Prejuízo): “)

            Aux.editar_calculo(calculo_id, nova_descricao, novo_valor, novo_tipo)

        Elif opcao == 4:

            Calculo_id = int(input(“ID do Cálculo a ser deletado: “))

            Aux.deletar_calculo(calculo_id)

        Elif opcao == 5:

            Resultado = aux.calcular_lucro_prejuizo()

            Print(f”Resultado: {resultado}”)

        Elif opcao == 6:

            Descricao = input(“Descrição da Transação: “)

            Valor = float(input(“Valor da Transação: “))

            Data = input(“Data (YYYY-MM-DD): “)

            Tipo = input(“Tipo (Lucro/Prejuízo): “)

            Aux.adicionar_transacao_fixa(descricao, valor, data, tipo)

        Elif opcao == 7:

            Transacoes = aux.listar_transacoes_fixas()

            For transacao in transacoes:

                Print(f”ID: {transacao[0]}, Descrição: {transacao[1]}, Valor: {transacao[2]}, Data: {transacao[3]}, Tipo: {transacao[4]}”)

        Elif opcao == 8:

            Data = input(“Data para estimativa (YYYY-MM-DD): “)

            Resultado = aux.calcular_produto_estimado(data)

            Print(f”Produto Estimado até {data}: {resultado}”)

        Elif opcao == 9:

            Descricao = input(“Descrição do Gasto Extraordinário: “)

            Valor = float(input(“Valor do Gasto: “))

            Mensagem = aux.informar_gastos_extraordinarios(descricao, valor)

            Print(mensagem)

        Elif opcao == 10:

            Break



If __name__ == “__main__”:

    Main()




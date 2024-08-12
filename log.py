import logging

logger = logging.getLogger(__name__)
def main():
    logging.basicConfig(filename='calc.log', level=logging.INFO)
    logger.info('Calculadora iniciada')
    try:
        operacao = input("""
        Qual operacao deseja fazer?\n
        soma(+)\n
        subtracao(-)\n
        multiplicacao (*)\n
        divisao(/)
        """)

        if operacao not in ['+', '-', '*', '/']:
            logger.warning(f'Operacao selecionada invalida ({operacao})')
            return

        logger.info(f'Operacao selecionada {operacao}')

        num1 = float(input("Digite o primeiro numero"))
        logger.info(f'Primeiro numero coletado {num1}')

        num2 = float(input("Digite o segundo numero"))
        logger.info(f'Segundo numero coletado {num2}')

        if operacao == '+':
            result = num1 + num2
            logger.info(f"Resultado {num1} + {num2}: {result}")
        if operacao == '-':
            result = num1 - num2
            logger.info(f"Resultado {num1} - {num2}: {result}")
        if operacao == '*':
            result = num1 * num2
            logger.info(f"Resultado {num1} * {num2}: {result}")
        if operacao == '/':
            if num2 == 0:
                logger.error(f"Nao e possivel dividir {num1} por zero!!!!!")
                return
            result = num1 / num2
            logger.info(f"Resultado {num1} / {num2}: {result}")

    except Exception as e:
        logger.exception(f"Erro ao executar calculadora: {e}")

if __name__ == '__main__':
    main()


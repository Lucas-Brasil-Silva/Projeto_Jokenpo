import random

PEDRA = 'Pedra'
PAPEL = 'Papel'
TESOURA = 'Tesoura'

def verificar_jogada(player,robo):
    if player == robo:
        return 'Empate'
    
    elif player == PEDRA:
        if robo == PAPEL:
            return 'Perdeu'
        else:
            return 'Venceu'
    
    elif player == PAPEL:
        if robo == TESOURA:
            return 'Perdeu'
        else:
            return 'Venceu'
    
    elif player == TESOURA:
        if robo == PEDRA:
            return 'Perdeu'
        else:
            return 'Venceu'

def resultado(player):
    robo = random.choice([PEDRA,PAPEL,TESOURA])
    resultado = verificar_jogada(player,robo)

    if resultado == 'Empate':
        return f'Empate! Ambos escolheram {player}.', 'white'
    elif resultado == 'Venceu':
        return f'Parabéns! Você ganhou. Você escolheu {player} e o robô escolheu {robo}.', 'green' 
    else:
        return f'Você perdeu. Você escolheu {player} e o robô escolheu {robo}.', 'red'


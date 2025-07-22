#!/usr/bin/env python3

from strands import Agent
from strands.models import BedrockModel
from strands.multiagent.a2a import A2AServer

bedrock_model = BedrockModel(model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

def start_agressive_agent(symbol):
    strategy_prompt = f"""
    Você é um agente de IA jogando jogo da velha como '{symbol}'.
    Seu objetivo é vencer o jogo usando estratégia.
    
    Regras do jogo:
    - O tabuleiro é numerado de 0 a 8:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    
    - Você deve escolher posições vazias (marcadas com ' ')
    - Você vence ao formar uma linha, coluna ou diagonal com seu símbolo
    
    Estratégia:
    1. Tente formar linhas, colunas ou diagonais com seu símbolo
    2. Bloqueie o oponente quando ele estiver prestes a vencer
    3. Prefira o centro (4) e os cantos (0, 2, 6, 8) quando disponíveis
    4. Pense à frente sobre possíveis jogadas futuras
    
    Quando receber uma mensagem com o estado do tabuleiro, analise-o e responda apenas com o número da posição escolhida (0-8).
    """
    agent = Agent(
        name=f"Strategic{symbol}Agent",
        model=bedrock_model,
        system_prompt=strategy_prompt,
        description=strategy_prompt
    )
    
    a2a_server = A2AServer(agent=agent,
                           port=9001)
    a2a_server.serve()

if __name__ == "__main__":
    start_agressive_agent("X")
#!/usr/bin/env python3

from strands import Agent
from strands.models import BedrockModel
from strands.multiagent.a2a import A2AServer

bedrock_model = BedrockModel(model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

def start_strategic_agent(symbol):
    strategy_prompt = f"""
    Você é um agente de IA jogando jogo da velha como '{symbol}'.
    Seu estilo é agressivo e focado em ataque.
    
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
    1. Priorize formar linhas com seu símbolo, mesmo que isso signifique ignorar bloqueios
    2. Tente controlar o centro (4) e os cantos (0, 2, 6, 8)
    3. Seja imprevisível e surpreenda seu oponente
    4. Foque em vencer, não em impedir o oponente
    
    Quando receber uma mensagem com o estado do tabuleiro, analise-o e responda apenas com o número da posição escolhida (0-8).
    """
    
    agent = Agent(
        name=f"Aggressive{symbol}Agent",
        model=bedrock_model,
        system_prompt=strategy_prompt,
        description=strategy_prompt
    )
    
    a2a_server = A2AServer(agent=agent,
                           port=9000)
    a2a_server.serve()

if __name__ == "__main__":
    start_strategic_agent("O")    


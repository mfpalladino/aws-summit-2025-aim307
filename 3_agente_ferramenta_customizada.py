#!/usr/bin/env python3
"""
Agente com Ferramenta Customizada

Este módulo foi desenvolvido como exemplo para a sessão "AIM307" do AWS Summit São Paulo 2025.

Este módulo demonstra como criar e utilizar ferramentas customizadas com o framework
Strands Agents. O exemplo implementa um agente de IA com uma ferramenta simples de
rolagem de dados (roll_dice), ilustrando como estender as capacidades de um agente
com funcionalidades personalizadas.

Este exemplo demonstra o conceito de orquestração dirigida por modelo (Model Driven 
Orchestration), onde o modelo de linguagem determina quando e como utilizar a ferramenta
customizada baseado no contexto e na intenção do usuário.

O agente é construído utilizando o framework de código aberto Strands Agents
(https://strandsagents.com), que facilita a criação de agentes de IA
com capacidades de raciocínio e uso de ferramentas externas.
"""

from strands import Agent, tool
from strands.models import BedrockModel
import random

SYSTEM_PROMPT = """# Assistente de RPG com Rolagem de Dados

Você é um assistente especializado em jogos de RPG que pode ajudar os jogadores com rolagens de dados.

## Suas capacidades:
- Rolar dados de diferentes tipos (d4, d6, d8, d10, d12, d20, d100)
- Explicar regras básicas de RPG
- Ajudar com cálculos de probabilidade em rolagens
- Sugerir rolagens apropriadas para diferentes situações de jogo

## Diretrizes de resposta:
- Quando o usuário pedir para rolar um dado, use a ferramenta roll_dice com o número apropriado de lados
- Explique o resultado da rolagem no contexto do pedido
- Para dados padrão de RPG, use os valores: d4, d6, d8, d10, d12, d20, d100
- Se o usuário pedir múltiplas rolagens, faça cada uma separadamente e explique os resultados
- Se o usuário pedir uma rolagem com modificador (ex: d20+5), role o dado e adicione o modificador manualmente

## Formato de resposta:
- Seja entusiástico e divertido, como um mestre de RPG
- Use linguagem temática de fantasia quando apropriado
- Explique os resultados de forma clara e contextualizada

Responda sempre em português brasileiro, usando terminologia comum de RPG.
"""

@tool
def roll_dice(sides: int=6) -> int:
    """
    Rola um dado com o número especificado de lados.
    
    Args:
        sides (int): Número de lados do dado (padrão: 6)
        
    Returns:
        int: Resultado da rolagem (número entre 1 e o número de lados)
    """
    return random.randint(1, sides)

def main():
    bedrock_model = BedrockModel(
        model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")
    
    agent = Agent(
        model=bedrock_model,
        system_prompt=SYSTEM_PROMPT,
        tools=[roll_dice])
    
    while True:
        user_input = input("\n> ")
        if user_input.lower() == "sair":
            break
        agent(user_input)
    
if __name__ == "__main__":
    main()

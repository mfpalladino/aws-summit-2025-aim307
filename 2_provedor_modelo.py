#!/usr/bin/env python3
"""
Provedor de Modelo Agnóstico com Strands

Este módulo foi desenvolvido como exemplo para a sessão "AIM307" do AWS Summit São Paulo 2025.

Este módulo demonstra como o framework Strands Agents é agnóstico em relação aos
provedores de modelos de linguagem. O exemplo implementa um agente de IA utilizando
um modelo local através do Ollama, ilustrando a flexibilidade do Strands em trabalhar
com diferentes provedores de LLM (não apenas com modelos em nuvem como Amazon Bedrock).

Este exemplo demonstra como o mesmo framework pode ser utilizado com modelos locais
ou em nuvem, permitindo que desenvolvedores escolham o provedor que melhor atende
às suas necessidades de custo, latência, privacidade e capacidades.

O agente implementado é especializado em ciências da computação, capaz de responder
questões sobre algoritmos, linguagens de programação, estruturas de dados e outros
tópicos relacionados.

O agente é construído utilizando o framework de código aberto Strands Agents
(https://strandsagents.com), que facilita a criação de agentes de IA
com capacidades de raciocínio e uso de ferramentas externas.
"""

from strands import Agent
from strands.models.ollama import OllamaModel

SYSTEM_PROMPT = """# Assistente de Ciências da Computação

Você é um assistente especializado em ciências da computação, capaz de fornecer informações 
precisas e úteis sobre diversos tópicos da área.

## Suas áreas de conhecimento:
- Algoritmos e estruturas de dados
- Linguagens de programação e paradigmas
- Sistemas operacionais e arquitetura de computadores
- Redes de computadores e protocolos
- Banco de dados e sistemas de armazenamento
- Inteligência artificial e aprendizado de máquina
- Engenharia de software e metodologias de desenvolvimento
- Segurança da informação e criptografia
- Computação em nuvem e sistemas distribuídos

## Diretrizes de resposta:
- Forneça explicações claras e precisas, adaptadas ao nível de conhecimento aparente do usuário
- Use analogias e exemplos práticos para ilustrar conceitos complexos
- Inclua código de exemplo quando relevante, usando a sintaxe apropriada
- Cite referências históricas importantes e marcos no desenvolvimento de tecnologias
- Quando apropriado, mencione vantagens e desvantagens de diferentes abordagens

## Formato de resposta:
- Seja conciso mas completo
- Use formatação para melhorar a legibilidade (listas, negrito, etc.)
- Organize informações complexas em seções lógicas
- Use linguagem técnica apropriada, mas explique termos especializados

Responda sempre em português brasileiro, usando terminologia técnica correta da área de computação.
"""

def main():
    ollama_model = OllamaModel(
        host="http://localhost:11434",  
        model_id="llama3")    
    
    agent = Agent(
        model=ollama_model,
        system_prompt=SYSTEM_PROMPT)
    
    while True:
        user_input = input("\n> ")
        if user_input.lower() == "sair":
            break
        agent(user_input)
    
if __name__ == "__main__":
    main()

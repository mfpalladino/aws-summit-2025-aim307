#!/usr/bin/env python3
"""
# Fluxo de Trabalho com Agentes: Assistente de Pesquisa

Este exemplo foi desenvolvido para a sessão "AIM307" do AWS Summit São Paulo 2025.

Este exemplo demonstra um fluxo de trabalho com agentes utilizando o framework Strands Agents
com capacidades de pesquisa na web e em base de conhecimento interna.

## Características Principais
- Agentes especializados trabalhando em sequência
- Passagem direta de informações entre estágios do fluxo
- Pesquisa na web usando ferramentas http_request e retrieve
- Consulta a base de conhecimento interna
- Verificação de fatos e síntese de informações

## Como Executar
1. Navegue até o diretório do exemplo
2. Execute: python 6_colaboracao_multi_agente.py
3. Digite consultas ou afirmações no prompt

## Exemplos de Consultas
- "Thomas Edison inventou a lâmpada"
- "Terça-feira vem antes de segunda-feira na semana"

## Processo do Fluxo de Trabalho
1. Agente Pesquisador: Coleta informações da web usando múltiplas ferramentas
2. Agente de Conhecimento: Consulta a base de conhecimento interna
3. Agente Analista: Verifica fatos e sintetiza descobertas de ambas as fontes
4. Agente Redator: Cria o relatório final
"""

from strands import Agent
from strands_tools import http_request, retrieve
from strands.models import BedrockModel

bedrock_model = BedrockModel(model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

RESEARCHER_SYSTEM_PROMPT = (
    "Você é um Agente Pesquisador que coleta informações da web. "
    "1. Determine se a entrada é uma consulta de pesquisa ou uma afirmação factual "
    "2. Use suas ferramentas de pesquisa (http_request) para encontrar informações relevantes "
    "3. Inclua URLs das fontes e mantenha as descobertas com menos de 500 palavras"
)

def execute_research_stage(user_input):
    """
    Etapa 1: Executa o Agente Pesquisador para coletar informações da web.

    Args:
        user_input: Consulta de pesquisa ou afirmação a ser verificada

    Returns:
        str: Resultados da pesquisa
    """
    print("\nEtapa 1: Agente Pesquisador coletando informações da web...")

    researcher_agent = Agent(
        model=bedrock_model,
        system_prompt=RESEARCHER_SYSTEM_PROMPT,
        callback_handler=None,
        tools=[http_request],
    )

    researcher_instruction = (
        f"Pesquisa: '{user_input}'. Use suas ferramentas disponíveis para coletar informações de fontes confiáveis. "
        f"Concentre-se em ser conciso e completo, mas limite as requisições web a 1-2 fontes."
    )

    researcher_response = researcher_agent(researcher_instruction)
    research_findings = str(researcher_response)

    print("Pesquisa web concluída")
    return research_findings

KNOWLEDGE_SYSTEM_PROMPT = (
    "Você é um Agente de Conhecimento que consulta a base de dados interna da empresa. "
    "1. Faça uma consulta à base de conhecimento interna sobre o tópico fornecido "
    "2. Indique claramente que as informações vêm da 'Base de Conhecimento Interna' "
    "3. Mantenha as informações concisas, com menos de 400 palavras"
)

def execute_knowledge_base_stage(user_input):
    """
    Etapa 2: Executa o Agente de Conhecimento para consultar a base de conhecimento interna.

    Args:
        user_input: Consulta de pesquisa ou afirmação a ser verificada

    Returns:
        str: Resultados da consulta à base de conhecimento
    """
    print("\nEtapa 2: Agente de Conhecimento consultando base interna...")

    knowledge_agent = Agent(
        model=bedrock_model,
        system_prompt=KNOWLEDGE_SYSTEM_PROMPT, 
        callback_handler=None, 
        tools=[retrieve]
    )

    knowledge_instruction = (
        f"Consulte nossa base de conhecimento interna sobre: '{user_input}'. "
    )

    knowledge_response = knowledge_agent.tool.retrieve(
        text=knowledge_instruction,
        knowledgeBaseId="XJFMTXZF8L",
        region="us-east-1"
    )

    knowledge_findings = str(knowledge_response)

    print("Consulta à base de conhecimento concluída")
    return knowledge_findings

ANALYST_SYSTEM_PROMPT = (
    "Você é um Agente Analista que verifica e integra informações de múltiplas fontes. "
    "1. Para afirmações factuais: Avalie a precisão de 1-5 e corrija se necessário "
    "2. Para consultas de pesquisa: Identifique 3-5 insights principais "
    "3. Compare e contraste informações da web com dados da base de conhecimento interna "
    "4. Identifique discrepâncias ou confirmações entre as fontes "
    "5. Avalie a confiabilidade das fontes e mantenha a análise com menos de 500 palavras"
)

def execute_analysis_stage(user_input, research_findings, knowledge_findings):
    """
    Etapa 3: Executa o Agente Analista para verificar e analisar as informações de ambas as fontes.

    Args:
        user_input: Consulta de pesquisa ou afirmação original
        research_findings: Resultados da pesquisa web
        knowledge_findings: Resultados da consulta à base de conhecimento

    Returns:
        str: Análise integrada das informações
    """
    print("Etapa 3: Agente Analista analisando descobertas de ambas as fontes...")

    analyst_agent = Agent(
        model=bedrock_model,
        system_prompt=ANALYST_SYSTEM_PROMPT, 
        callback_handler=None)

    analyst_instruction = (
        f"Analise estas descobertas sobre '{user_input}':\n\n"
        f"=== PESQUISA WEB ===\n{research_findings}\n\n"
        f"=== BASE DE CONHECIMENTO INTERNA ===\n{knowledge_findings}"
    )

    analyst_response = analyst_agent(analyst_instruction)
    analysis = str(analyst_response)

    print("Análise concluída")
    return analysis

WRITER_SYSTEM_PROMPT = (
    "Você é um Agente Redator que cria relatórios claros. "
    "1. Para verificações de fatos: Declare se as afirmações são verdadeiras ou falsas "
    "2. Para pesquisas: Apresente os principais insights em uma estrutura lógica "
    "3. Integre informações da web e da base de conhecimento interna de forma coesa "
    "4. Destaque quando o conhecimento interno complementa ou contradiz fontes externas "
    "5. Mantenha os relatórios com menos de 600 palavras com breves menções às fontes"
)

def execute_report_stage(user_input, analysis):
    """
    Etapa 4: Executa o Agente Redator para criar o relatório final.

    Args:
        user_input: Consulta de pesquisa ou afirmação original
        analysis: Análise integrada das informações

    Returns:
        str: Relatório final
    """
    print("Etapa 4: Agente Redator criando relatório final...")

    writer_agent = Agent(
        model=bedrock_model,
        system_prompt=WRITER_SYSTEM_PROMPT)

    writer_instruction = (
        f"Crie um relatório sobre '{user_input}' com base nesta análise:\n\n{analysis}"
    )

    final_report = writer_agent(writer_instruction)

    print("Criação do relatório concluída")
    return final_report

def run_research_workflow(user_input):
    """
    Executa um fluxo de trabalho com quatro agentes para pesquisa e verificação de fatos,
    combinando fontes web e base de conhecimento interna.

    Args:
        user_input: Consulta de pesquisa ou afirmação a ser verificada

    Returns:
        str: O relatório final do Agente Redator
    """
    print(f"\nProcessando: '{user_input}'")

    # Etapa 1: Pesquisa Web
    research_findings = execute_research_stage(user_input)

    # Etapa 2: Consulta à Base de Conhecimento
    knowledge_findings = execute_knowledge_base_stage(user_input)
    print("Passando descobertas de ambas as fontes para o Agente Analista...\n")

    # Etapa 3: Análise Integrada
    analysis = execute_analysis_stage(user_input, research_findings, knowledge_findings)
    print("Passando análise para o Agente Redator...\n")

    # Etapa 4: Relatório
    final_report = execute_report_stage(user_input, analysis)

    # Retorna o relatório final
    return final_report

if __name__ == "__main__":
    # Imprime mensagem de boas-vindas
    print(
        "\nFluxo de Trabalho com Agentes: Assistente de Pesquisa com Base de Conhecimento\n"
    )
    print(
        "Esta demonstração mostra agentes Strands em um fluxo de trabalho com pesquisa na web e base de conhecimento interna."
    )
    print("Experimente perguntas de pesquisa ou verificação de afirmações.")
    print("\nExemplos:")
    print('- "O que são computadores quânticos?"')
    print('- "Limão cura câncer"')
    print('- "Terça-feira vem antes de segunda-feira na semana"')

    # Loop interativo
    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == "sair":
                print("\nAté logo!")
                break

            # Processa a entrada através do fluxo de trabalho de agentes
            final_report = run_research_workflow(user_input)
        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Saindo...")
            break
        except Exception as e:
            print(f"\nOcorreu um erro: {str(e)}")
            print("Por favor, tente uma solicitação diferente.")

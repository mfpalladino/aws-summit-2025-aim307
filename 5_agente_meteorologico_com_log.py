#!/usr/bin/env python3
"""
Agente Meteorológico com Logging

Este módulo foi desenvolvido como exemplo para a sessão "AIM307" do AWS Summit São Paulo 2025.

Este módulo implementa um agente de IA especializado em fornecer informações
meteorológicas utilizando a API do OpenWeatherMap. O agente demonstra o conceito
de orquestração dirigida por modelo (Model Driven Orchestration), onde o modelo
de linguagem determina quais ferramentas utilizar e como orquestrar o fluxo de
execução baseado no contexto e na intenção do usuário.

Este exemplo específico demonstra como habilitar e configurar o sistema de logging
do framework Strands Agents, direcionando os logs para um arquivo em vez de exibi-los
na tela, o que facilita a depuração e análise do comportamento do agente sem
poluir a saída do console.

O agente é construído utilizando o framework de código aberto Strands Agents
(https://strandsagents.com), que facilita a criação de agentes de IA
com capacidades de raciocínio e uso de ferramentas externas.

O agente utiliza ferramentas como requisições HTTP, comandos de shell e acesso
ao tempo atual para enriquecer suas respostas com dados meteorológicos precisos.

Requer uma chave de API do OpenWeatherMap configurada como variável de ambiente.
"""

import os
from strands import Agent
from strands_tools import http_request, shell, current_time
from strands.models import BedrockModel
import logging

SYSTEM_PROMPT = """# Agente Meteorológico do Palla e da Chey para o AWS Summit São Paulo 2025

Você é um assistente especializado em informações meteorológicas que utiliza a API do OpenWeatherMap para fornecer dados precisos sobre o clima.

## Configuração da API:
- Acesse a chave da API do OpenWeatherMap através da variável de ambiente OPENWEATHER_API_KEY (você deve busca-la com a ferramenta apropriada)
- Caso a variável de ambiente não esteja disponível, informe ao usuário que é necessário configurá-la
- Nunca solicite que o usuário forneça a chave da API diretamente na conversa

## Suas capacidades:
- Consultar condições climáticas atuais para qualquer localização
- Fornecer previsões meteorológicas de curto e médio prazo
- Explicar fenômenos meteorológicos de forma clara
- Converter unidades de medida (Celsius/Fahrenheit, km/h para m/s, etc.)
- Interpretar dados meteorológicos técnicos para usuários leigos

## Diretrizes de resposta:
- Sempre inclua a fonte dos dados (OpenWeatherMap) e timestamp da consulta
- Forneça temperaturas em Celsius por padrão, mas ofereça conversão quando solicitado
- Explique condições meteorológicas usando linguagem acessível
- Inclua informações relevantes como sensação térmica, umidade, vento quando apropriado
- Para previsões, sempre mencione o período de validade dos dados
- Se não conseguir obter dados para uma localização, sugira alternativas próximas

## Formato de resposta:
- Seja conciso mas informativo
- Use emojis meteorológicos quando apropriado (☀️🌧️❄️⛅)
- Organize informações em tópicos quando necessário
- Inclua alertas meteorológicos importantes quando disponíveis

## Limitações:
- Reconheça quando os dados podem estar desatualizados
- Não faça previsões além do período coberto pela API
- Sempre mencione que condições podem mudar rapidamente

Responda sempre em português brasileiro, adaptando unidades e terminologia local.
"""

log_file = os.path.join('logs', '5_agente_meteorologico_com_log.log')

logging.getLogger("strands").setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(log_file, mode='w')]
)

def main():
    print(f"Logs detalhados serão salvos em: {os.path.abspath(log_file)}")
    
    bedrock_model = BedrockModel(
        model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")
    
    agent = Agent(
        model=bedrock_model,
        system_prompt=SYSTEM_PROMPT,
        tools=[http_request, shell, current_time])
    
    agent("Qual a temperatura em São Paulo (capital) agora?")

if __name__ == "__main__":
    main()

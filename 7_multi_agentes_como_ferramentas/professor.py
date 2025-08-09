#!/usr/bin/env python3
"""
# 📁 Agente Professor

Um agente Strands especializado que atua como orquestrador para utilizar sub-agentes
e ferramentas à sua disposição para responder a consultas do usuário.

Este exemplo usa um padrão de arquitetura chamado "Agents as Tools".

Este padrão oferece várias vantagens:

Separação de responsabilidades: Cada agente tem uma área focada de responsabilidade, 
tornando o sistema mais fácil de entender e manter. 

Delegação hierárquica: O orquestrador decide qual especialista invocar, 
criando uma clara cadeia de comando. 

Arquitetura modular: Especialistas podem ser adicionados, removidos ou modificados 
independentemente sem afetar todo o sistema. 

Melhor desempenho: Cada agente pode ter prompts do sistema personalizados e 
ferramentas otimizadas para sua tarefa específica.

Exemplos do mundo real que poderiam se beneficiar de uma arquitetura como essa:

Atendimento ao cliente em empresas de telecomunicações:
 - Agente Classificador: Analisa a consulta inicial do cliente e determina a natureza do problema
 - Agente Técnico: Lida com problemas de conectividade, configurações e hardware
 - Agente de Faturamento: Responde a questões sobre cobranças e planos
 - Agente de Retenção: Entra em ação quando detecta intenção de cancelamento
 - Agente Sintetizador: Consolida as informações e fornece uma resposta unificada

Assistente médico para triagem e diagnóstico preliminar:
 - Agente de Coleta de Sintomas: Obtém informações iniciais do paciente
 - Agente de Histórico Médico: Consulta e analisa o histórico do paciente
 - Agente de Conhecimento Médico: Pesquisa literatura médicarelevante
 - Agente de Diagnóstico: Combina as informações para sugerir possíveis diagnósticos
 - Agente de Recomendação: Sugere próximos passos (consulta presencial, exames, etc.)

Sistema de suporte educacional personalizado:
 - Agente Avaliador: Identifica o nível de conhecimento e lacunas do estudante
 - Agente de Conteúdo: Seleciona materiais didáticos apropriados
 - Agente de Exercícios: Gera problemas e questões adaptadas ao nível do aluno
 - Agente de Feedback: Analisa respostas e fornece orientações personalizadas
 - Agente de Progresso: Monitora evolução e ajusta o plano de estudos

Plataforma de pesquisa jurídica:
 - Agente de Classificação: Identifica a área do direito relacionada à consulta
 - Agente de Legislação: Pesquisa leis e códigos relevantes
 - Agente de Jurisprudência: Busca precedentes e decisões judiciais similares
 - Agente de Doutrina: Consulta literatura jurídica e opiniões de especialistas
 - Agente Sintetizador: Compila as informações em um relatório coeso

Sistema de planejamento financeiro:
 - Agente de Perfil: Analisa o perfil financeiro e objetivos do usuário
 - Agente de Mercado: Monitora tendências e oportunidades deinvestimento
 - Agente de Risco: Avalia riscos associados a diferentes estratégias
 - Agente de Simulação: Projeta cenários futuros com base em diferentes decisões
 - Agente de Recomendação: Sugere estratégias financeiras personalizadas
"""

from strands import Agent
from strands.models import BedrockModel
from portugues import portuguese_assistant
from idiomas import language_assistant
from matematica import math_assistant
from ciencias_da_computacao import computer_science_assistant
from generalista import general_assistant


# Define a focused system prompt for file operations
TEACHER_SYSTEM_PROMPT = """
Você é o TeachAssist, um sofisticado orquestrador educacional projetado para coordenar 
suporte educacional em várias disciplinas. Seu papel é:

1. Analisar as consultas dos alunos e determinar o agente especializado mais apropriado para lidar com elas:
   - Agente de Matemática: Para cálculos matemáticos, problemas e conceitos
   - Agente de Português: Para escrita, gramática, literatura e composição
   - Agente de Idiomas: Para tradução e consultas relacionadas a idiomas
   - Agente de Ciências da Computação: Para programação, algoritmos, estruturas de dados e execução de código
   - Assistente Geral: Para todos os outros tópicos fora desses domínios especializados

2. Responsabilidades Principais:
   - Classificar com precisão as consultas dos alunos por área de assunto
   - Encaminhar solicitações para o agente especializado apropriado
   - Manter o contexto e coordenar problemas de múltiplas etapas
   - Garantir respostas coesas quando vários agentes são necessários

3. Protocolo de Decisão:
   - Se a consulta envolve cálculos/números → Agente de Matemática
   - Se a consulta envolve escrita/literatura/gramática → Agente de Português
   - Se a consulta envolve tradução → Agente de Idiomas
   - Se a consulta envolve programação/codificação/algoritmos/ciência da computação → Agente de Ciências da Computação
   - Se a consulta está fora dessas áreas especializadas → Assistente Geral
   - Para consultas complexas, coordene vários agentes conforme necessário

Sempre confirme sua compreensão antes de encaminhar para garantir assistência precisa.
"""

bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

teacher_agent = Agent(
    system_prompt=TEACHER_SYSTEM_PROMPT,
    model=bedrock_model,
    callback_handler=None,
    tools=[math_assistant, 
           language_assistant, 
           portuguese_assistant, 
           computer_science_assistant, 
           general_assistant],
)

if __name__ == "__main__":
    print("\n📁 Assistente de Professor com Agentes Strands 📁\n")
    print("Faça uma pergunta em qualquer área de assunto, e eu a encaminharei para o especialista apropriado.")
    print("Digite 'sair' para sair.")

    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == "sair":
                print("\nAté logo! 👋")
                break

            response = teacher_agent(
                user_input, 
            )
            
            content = str(response)
            print(content)
            
        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Saindo...")
            break
        except Exception as e:
            print(f"\nOcorreu um erro: {str(e)}")
            print("Por favor, tente fazer uma pergunta diferente.")
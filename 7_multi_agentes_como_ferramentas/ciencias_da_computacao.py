from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import python_repl, shell, file_read, file_write, editor

COMPUTER_SCIENCE_ASSISTANT_SYSTEM_PROMPT = """
Você é o EspecialistaEmCiênciasDaComputação, um assistente especializado 
em educação em ciência da computação e programação. Suas capacidades incluem:

1. Suporte à Programação:
   - Explicação e depuração de código
   - Desenvolvimento e otimização de algoritmos
   - Implementação de padrões de design de software
   - Orientação sobre sintaxe de linguagens de programação

2. Educação em Ciência da Computação:
   - Explicação de conceitos teóricos
   - Ensino de estruturas de dados e algoritmos
   - Fundamentos de arquitetura de computadores
   - Princípios de redes e segurança

3. Assistência Técnica:
   - Execução e teste de código em tempo real
   - Orientação e execução de comandos de shell
   - Operações e gerenciamento de sistema de arquivos
   - Sugestões de edição e melhoria de código

4. Metodologia de Ensino:
   - Explicações passo a passo com exemplos
   - Construção progressiva de conceitos
   - Aprendizado interativo através da execução de código
   - Demonstrações de aplicações do mundo real

Concentre-se em fornecer explicações claras e práticas que demonstrem conceitos com exemplos executáveis. Use ferramentas de execução de código para ilustrar conceitos sempre que possível.
"""
@tool
def computer_science_assistant(query: str) -> str:
    """
    Processa e responde a perguntas relacionadas à ciência da computação e programação usando um agente especializado com capacidades de execução de código.
    
    Args:
        query: A pergunta do usuário sobre ciência da computação ou programação
        
    Returns:
        Uma resposta detalhada abordando conceitos de ciência da computação ou resultados de execução de código
    """
    formatted_query = f"Por favor, responda a esta pergunta sobre ciência da computação ou programação. Quando apropriado, forneça exemplos de código executáveis e explique os conceitos detalhadamente: {query}"
    
    try:
        print("Encaminhado para o Assistente de Ciências da Computação")

        bedrock_model = BedrockModel(
            model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

        cs_agent = Agent(
            system_prompt=COMPUTER_SCIENCE_ASSISTANT_SYSTEM_PROMPT,
            model=bedrock_model,
            tools=[python_repl, shell, file_read, file_write, editor],
        )
        agent_response = cs_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "Peço desculpas, mas não consegui processar sua pergunta sobre ciência da computação. Por favor, tente reformular ou fornecer detalhes mais específicos sobre o que você está tentando aprender ou realizar."
    except Exception as e:
        return f"Erro ao processar sua consulta de ciência da computação: {str(e)}"
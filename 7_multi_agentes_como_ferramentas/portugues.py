from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import file_read, file_write, editor

PORTUGUESE_ASSISTANT_SYSTEM_PROMPT = """
Você é o mestre de Português, um assistente avançado de educação em língua portuguesa. Suas capacidades incluem:

1. Suporte à Escrita:
   - Melhoria de gramática e sintaxe
   - Aprimoramento de vocabulário
   - Refinamento de estilo e tom
   - Orientação sobre estrutura e organização

2. Ferramentas de Análise:
   - Resumo de texto
   - Análise literária
   - Avaliação de conteúdo
   - Assistência com citações

3. Métodos de Ensino:
   - Fornecer explicações claras com exemplos
   - Oferecer feedback construtivo
   - Sugerir melhorias
   - Decompor conceitos complexos

Concentre-se em ser claro, encorajador e educativo em todas as interações. Sempre explique o raciocínio por trás de suas sugestões para promover o aprendizado.

"""


@tool
def portuguese_assistant(query: str) -> str:
    """
    Processa e responde a consultas relacionadas à língua portuguesa, literatura e escrita.
    
    Args:
        query: A pergunta do usuário sobre língua portuguesa ou literatura
        
    Returns:
        Uma resposta útil abordando conceitos de língua portuguesa ou literatura
    """
    formatted_query = f"Analise e responda a esta pergunta sobre língua portuguesa ou literatura, fornecendo explicações claras com exemplos quando apropriado: {query}"
    
    try:
        print("Encaminhado para o Assistente de Português")

        bedrock_model = BedrockModel(
            model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

        portuguese_agent = Agent(
            system_prompt=PORTUGUESE_ASSISTANT_SYSTEM_PROMPT,
            model=bedrock_model,
            tools=[editor, file_read, file_write],
        )
        agent_response = portuguese_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "Peço desculpas, mas não consegui analisar adequadamente sua pergunta sobre língua portuguesa. Poderia reformulá-la ou fornecer mais contexto?"
    except Exception as e:
        return f"Erro ao processar sua consulta sobre língua portuguesa: {str(e)}"
from strands import Agent, tool
from strands.models import BedrockModel

GENERAL_ASSISTANT_SYSTEM_PROMPT = """
Você é o AssistenteGeral, um assistente conciso de conhecimento geral 
para tópicos fora de domínios especializados. Suas características principais são:

1. Estilo de Resposta:
   - Sempre comece reconhecendo que você não é um especialista nesta área específica
   - Use frases como "Embora eu não seja um especialista nesta área..." ou "Não tenho conhecimento especializado, mas..."
   - Forneça respostas breves e diretas após este aviso
   - Concentre-se em fatos e clareza
   - Evite elaborações desnecessárias
   - Use linguagem simples e acessível

2. Áreas de Conhecimento:
   - Tópicos de conhecimento geral
   - Solicitações de informações básicas
   - Explicações simples de conceitos
   - Consultas não especializadas

3. Abordagem de Interação:
   - Sempre inclua o aviso de não-especialista em cada resposta
   - Responda com brevidade (2-3 frases quando possível)
   - Use marcadores para vários itens
   - Declare claramente se a informação é limitada
   - Sugira assistência especializada quando apropriado

Sempre mantenha a precisão enquanto prioriza a concisão e clareza em cada resposta, e nunca se esqueça de reconhecer seu status de não-especialista no início de suas respostas.
"""

@tool
def general_assistant(query: str) -> str:
    """
    Lida com consultas de conhecimento geral que estão fora de domínios especializados.
    Fornece respostas concisas e precisas para perguntas não especializadas.
    
    Args:
        query: A pergunta de conhecimento geral do usuário
        
    Returns:
        Uma resposta concisa para a consulta de conhecimento geral
    """

    formatted_query = f"Responda a esta pergunta de conhecimento geral de forma concisa, lembrando-se de começar reconhecendo que você não é um especialista nesta área específica: {query}"
    
    try:
        print("Encaminhado para o Assistente Geral")

        bedrock_model = BedrockModel(
            model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

        general_agent = Agent(
            system_prompt=GENERAL_ASSISTANT_SYSTEM_PROMPT,
            model=bedrock_model,
            tools=[],  
        )
        agent_response = general_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "Desculpe, não consegui fornecer uma resposta para sua pergunta."
    except Exception as e:
        return f"Erro ao processar sua pergunta: {str(e)}"
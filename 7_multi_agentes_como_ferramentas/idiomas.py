from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import http_request

LANGUAGE_ASSISTANT_SYSTEM_PROMPT = """
Você é o AssistenteDeIdiomas, um assistente especializado em 
tradução e aprendizado de idiomas. Seu papel abrange:

1. Serviços de Tradução:
   - Tradução precisa entre idiomas
   - Traduções apropriadas ao contexto
   - Tratamento de expressões idiomáticas
   - Consideração do contexto cultural

2. Suporte ao Aprendizado de Idiomas:
   - Explicar escolhas de tradução
   - Destacar padrões linguísticos
   - Fornecer orientação de pronúncia
   - Explicações de contexto cultural

3. Abordagem de Ensino:
   - Decompor traduções passo a passo
   - Explicar diferenças gramaticais
   - Fornecer exemplos relevantes
   - Oferecer dicas de aprendizado

Mantenha a precisão enquanto garante que as traduções sejam naturais e contextualmente apropriadas.

"""


@tool
def language_assistant(query: str) -> str:
    """
    Processa e responde a consultas de tradução e aprendizado de idiomas estrangeiros.
    
    Args:
        query: Uma solicitação de tradução ou assistência para aprendizado de idiomas
        
    Returns:
        Um texto traduzido ou orientação de aprendizado de idiomas com explicações
    """
    formatted_query = f"Por favor, atenda a esta solicitação de tradução ou aprendizado de idiomas, fornecendo contexto cultural e explicações quando útil: {query}"
    
    try:
        print("Encaminhado para o Assistente de Idiomas")

        bedrock_model = BedrockModel(
            model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

        language_agent = Agent(
            system_prompt=LANGUAGE_ASSISTANT_SYSTEM_PROMPT,
            model=bedrock_model,
            tools=[http_request],
        )
        agent_response = language_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response

        return "Peço desculpas, mas não consegui processar sua solicitação de idioma. Por favor, certifique-se de especificar os idiomas envolvidos e a necessidade específica de tradução ou aprendizado."
    except Exception as e:
        return f"Erro ao processar sua consulta de idioma: {str(e)}"
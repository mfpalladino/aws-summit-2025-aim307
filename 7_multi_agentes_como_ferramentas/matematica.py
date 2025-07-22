from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator

MATH_ASSISTANT_SYSTEM_PROMPT = """
Você é o mago da matemática, um assistente especializado em educação matemática. Suas capacidades incluem:

1. Operações Matemáticas:
   - Cálculos aritméticos
   - Resolução de problemas algébricos
   - Análise geométrica
   - Cálculos estatísticos

2. Ferramentas de Ensino:
   - Resolução de problemas passo a passo
   - Criação de explicações visuais
   - Orientação na aplicação de fórmulas
   - Decomposição de conceitos

3. Abordagem Educacional:
   - Mostrar o trabalho detalhado
   - Explicar o raciocínio matemático
   - Fornecer soluções alternativas
   - Vincular conceitos a aplicações do mundo real

Concentre-se na clareza e na resolução sistemática de problemas, garantindo que os alunos entendam os conceitos subjacentes.
"""

@tool
def math_assistant(query: str) -> str:
    """
    Processa e responde a consultas relacionadas à matemática usando um agente especializado em matemática.
    
    Args:
        query: Uma pergunta ou problema matemático do usuário
        
    Returns:
        Uma resposta matemática detalhada com explicações e etapas
    """

    formatted_query = f"Por favor, resolva o seguinte problema matemático, mostrando todas as etapas e explicando os conceitos claramente: {query}"
    
    try:
        print("Encaminhado para o Assistente de Matemática")

        bedrock_model = BedrockModel(
            model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

        math_agent = Agent(
            system_prompt=MATH_ASSISTANT_SYSTEM_PROMPT,
            model=bedrock_model,
            tools=[calculator],
        )
        agent_response = math_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response

        return "Peço desculpas, mas não consegui resolver este problema matemático. Por favor, verifique se sua consulta está claramente formulada ou tente reformulá-la."
    except Exception as e:
        return f"Erro ao processar sua consulta matemática: {str(e)}"
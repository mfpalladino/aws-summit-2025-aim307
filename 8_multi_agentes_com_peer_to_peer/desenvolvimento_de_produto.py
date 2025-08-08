#!/usr/bin/env python3
"""
Sistema de Desenvolvimento Colaborativo de Produtos com Multi-Agentes

Este módulo implementa um sistema de desenvolvimento de produtos que utiliza múltiplos agentes
especializados trabalhando em colaboração peer-to-peer para criar planos abrangentes de desenvolvimento.

Componentes Principais:
- Agent Coordinator: Coordena uma equipe de especialistas usando a ferramenta swarm
- Equipe de 3 Especialistas:
  * UX/UI Product Designer: Foca em experiência do usuário e design de interfaces
  * Senior Software Developer: Avalia viabilidade técnica e arquitetura
  * Quality Assurance Tester: Identifica riscos e planeja estratégias de teste

Processo Colaborativo:
1. Designer cria pesquisa inicial de usuários e conceitos de design
2. Developer revisa viabilidade e sugere abordagens técnicas
3. Tester identifica problemas potenciais e requisitos de teste
4. Todos colaboram em 2 rodadas de refinamento
5. Plano integrado final é criado

Entregáveis:
- Pesquisa de usuários e personas
- Especificações de funcionalidades
- Visão geral da arquitetura técnica
- Cronograma de desenvolvimento e marcos
- Estratégia de testes e métricas de qualidade
- Avaliação de riscos e planos de mitigação

Casos de Uso do Mundo Real:
- Startups: Validação rápida de MVPs com análise técnica e de mercado
- Empresas: Desenvolvimento de novos produtos digitais com equipes virtuais
- Consultoria: Criação de propostas técnicas detalhadas para clientes
- Educação: Simulação de equipes de desenvolvimento para ensino
- Inovação: Prototipagem de conceitos com avaliação multidisciplinar
- E-commerce: Desenvolvimento de funcionalidades com foco em conversão
- Fintech: Produtos financeiros com ênfase em segurança e compliance
- Healthtech: Aplicações médicas considerando regulamentações e usabilidade
"""

from strands import Agent
from strands_tools import swarm

SYSTEM_PROMPT = """Você é um coordenador de desenvolvimento de produtos que facilita o desenvolvimento colaborativo de produtos usando grupos de agentes especializados (swarms).
    
    Use a ferramenta swarm para criar equipes de agentes especializados que trabalham juntos em tarefas de desenvolvimento de produtos.
    
    Foque em:
    - Princípios de design centrado no usuário
    - Viabilidade técnica e melhores práticas
    - Garantia de qualidade e testes
    - Melhoria iterativa e refinamento
    - Colaboração multifuncional
    """

product_swarm_coordinator = Agent(
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    tools=[swarm],
    system_prompt=SYSTEM_PROMPT
)

def collaborative_product_development(product_idea: str, target_users: str, platform: str = "aplicação web") -> str:
    """Desenvolve um conceito de produto colaborativamente usando uma equipe de especialistas (swarm).
    
    Args:
        product_idea: Descrição do produto a ser desenvolvido
        target_users: Os usuários pretendidos do produto
        platform: A plataforma alvo (web, mobile, desktop, etc.)
    
    Returns:
        Plano abrangente de desenvolvimento de produto
    """
    swarm_request = f"""
    Crie uma equipe de três especialistas em desenvolvimento de produtos para desenvolver colaborativamente: {product_idea}
    Usuários-alvo: {target_users}
    Plataforma: {platform}
    
    A equipe de desenvolvimento deve incluir:
    
    1. Um Designer de Produto UX/UI que:
       - Analisa necessidades e pontos de dor dos usuários
       - Cria personas de usuário e mapas de jornada
       - Projeta interfaces de usuário intuitivas
       - Foca em acessibilidade e usabilidade
       - Considera sistemas de design e consistência
    
    2. Um Desenvolvedor de Software Sênior que:
       - Avalia viabilidade técnica
       - Projeta arquitetura do sistema
       - Identifica tecnologias e frameworks necessários
       - Considera escalabilidade e performance
       - Estima esforço de desenvolvimento e cronograma
    
    3. Um Testador de Garantia de Qualidade que:
       - Identifica potenciais problemas de experiência do usuário
       - Planeja estratégias e cenários de teste
       - Considera casos extremos e tratamento de erros
       - Avalia preocupações de segurança e privacidade
       - Sugere métricas de qualidade e critérios de sucesso
    
    Processo de Colaboração:
    - Designer cria pesquisa inicial de usuários e conceitos de design
    - Desenvolvedor revisa viabilidade e sugere abordagens técnicas
    - Testador identifica problemas potenciais e requisitos de teste
    - Todos os membros da equipe colaboram por 2 rodadas de refinamento
    - Plano integrado final de desenvolvimento de produto é criado
    
    Os entregáveis devem incluir:
    - Pesquisa de usuários e personas
    - Especificações de funcionalidades
    - Visão geral da arquitetura técnica
    - Cronograma de desenvolvimento e marcos
    - Estratégia de testes e métricas de qualidade
    - Avaliação de riscos e planos de mitigação
    """
    
    print(f"🚀 Iniciando desenvolvimento colaborativo de produto para: {product_idea}")
    print(f"👥 Usuários-alvo: {target_users}")
    print(f"💻 Plataforma: {platform}")
    print("⏳ Equipe de desenvolvimento está colaborando...\n")
    
    result = product_swarm_coordinator(swarm_request)
    return result

print("✅ Coordenador de equipe de desenvolvimento de produto pronto!")

# Teste da equipe de desenvolvimento de produto
product_idea = "Um aplicativo inteligente de gerenciamento de tarefas que usa IA para priorizar tarefas e sugerir cronogramas de trabalho otimizados"
target_users = "profissionais ocupados e trabalhadores remotos"
platform = "aplicação mobile (iOS e Android)"

product_result = collaborative_product_development(product_idea, target_users, platform)
print("📋 Plano de Desenvolvimento de Produto:")
print("=" * 50)
print(product_result)
# Jogo da Velha com Agentes A2A

Este projeto demonstra uma implementação do protocolo Agent-to-Agent (A2A) usando dois agentes de IA que jogam jogo da velha um contra o outro.

## O que é o protocolo A2A?

O [Agent-to-Agent (A2A) Protocol](https://a2a-protocol.org/latest/) é uma especificação para comunicação direta entre agentes de IA. Ele define um formato padronizado para mensagens, permitindo que agentes com diferentes capacidades possam colaborar de forma eficiente.

## Duas Implementações

Este projeto contém duas implementações do jogo da velha com agentes A2A:

1. **Implementação Personalizada** (`jogo_da_velha_a2a.py`): Uma implementação que cria manualmente o formato de mensagem A2A.

2. **Implementação Nativa** (`jogo_da_velha_a2a_nativo.py`): Uma implementação que utiliza a API nativa do Strands Agents para comunicação A2A.

A implementação nativa é mais simples e aproveita as funcionalidades integradas do framework Strands Agents, enquanto a implementação personalizada demonstra os conceitos subjacentes do protocolo A2A.

## Arquitetura

![Arquitetura A2A](a2a_architecture.png)

O diagrama acima ilustra a arquitetura A2A implementada neste projeto. Os agentes se comunicam diretamente entre si, sem um orquestrador central, e cada um toma suas próprias decisões com base em sua estratégia.

## Fluxo de Comunicação

![Fluxo de Comunicação A2A](a2a_sequence.png)

O diagrama acima ilustra o fluxo de comunicação entre os agentes durante o jogo. Cada agente analisa o tabuleiro, decide sua jogada e a executa, e então passa a vez para o outro agente.

## Estrutura de Mensagem A2A

![Estrutura de Mensagem A2A](a2a_message_structure.png)

O diagrama acima ilustra a estrutura de uma mensagem A2A, com seus metadados e conteúdo.

## Características implementadas

Neste exemplo, implementamos as seguintes características do protocolo A2A:

1. **Identidade dos agentes**: Cada agente tem seu próprio ID e personalidade (estratégico vs. agressivo).

2. **Comunicação direta**: Os agentes enviam mensagens diretamente um ao outro, sem um orquestrador central.

3. **Formato de mensagem padronizado**: Na implementação personalizada, a classe `A2AMessage` segue a estrutura do protocolo A2A com metadados e conteúdo. Na implementação nativa, isso é gerenciado pelo framework Strands Agents.

4. **Autonomia**: Cada agente toma suas próprias decisões com base em sua estratégia e no estado atual do jogo.

5. **Conversação persistente**: As mensagens são armazenadas em um histórico de conversação com IDs de conversa.

## Agentes implementados

### Agente Estratégico

Este agente prioriza:
- Bloquear o oponente quando ele está prestes a vencer
- Formar linhas, colunas ou diagonais com seu símbolo
- Ocupar posições estratégicas (centro e cantos)
- Pensar à frente sobre possíveis jogadas futuras

### Agente Agressivo

Este agente prioriza:
- Formar linhas com seu símbolo, mesmo que isso signifique ignorar bloqueios
- Controlar o centro e os cantos
- Ser imprevisível e surpreender o oponente
- Focar em vencer, não em impedir o oponente

## Como executar

### Implementação Personalizada
```bash
python jogo_da_velha_a2a.py
```

### Implementação Nativa
```bash
python jogo_da_velha_a2a_nativo.py
```

## Diferenças entre as implementações

### Implementação Personalizada (`jogo_da_velha_a2a.py`)

- Cria manualmente a estrutura de mensagem A2A
- Implementa métodos personalizados para envio e recebimento de mensagens
- Gerencia explicitamente o histórico de conversação
- Demonstra os conceitos subjacentes do protocolo A2A

### Implementação Nativa (`jogo_da_velha_a2a_nativo.py`)

- Utiliza o método `agent.send_message()` nativo do Strands Agents
- Aproveita o gerenciamento de conversação integrado do framework
- Código mais simples e direto
- Segue as melhores práticas recomendadas pela documentação do Strands Agents

## Diferenças em relação ao padrão "Agents as Tools"

No padrão "Agents as Tools", um agente orquestrador central controla o fluxo de trabalho e chama outros agentes como ferramentas. No protocolo A2A, os agentes são autônomos e se comunicam diretamente entre si, sem um orquestrador central.

Principais diferenças:

1. **Comunicação direta**: Os agentes enviam mensagens diretamente um ao outro.
2. **Autonomia**: Cada agente toma suas próprias decisões.
3. **Formato de mensagem padronizado**: As mensagens seguem um formato específico.
4. **Identidade**: Cada agente tem sua própria identidade e personalidade.

## Referências

- [Documentação do Strands Agents sobre A2A](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agent-to-agent/)
- [Especificação do protocolo A2A](https://a2a-protocol.org/latest/)

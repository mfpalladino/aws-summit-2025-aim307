# AIM307 - AWS Summit São Paulo 2025

Este repositório contém os materiais e recursos para a sessão AIM307 "Aproveitando o poder da arquitetura de Agentic AI" apresentada durante o AWS Summit São Paulo 2025.

## 📋 Pré-requisitos

### 1. Ambiente Python
- **Python 3.8+** (recomendado Python 3.11 ou superior)
- **pip** (gerenciador de pacotes Python)

### 2. Ambiente Virtual Python
Crie e ative um ambiente virtual para isolar as dependências:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 3. Instalação de Dependências
Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 4. Credenciais AWS
Configure suas credenciais AWS usando uma das opções abaixo:

#### Opção 1: AWS CLI
```bash
aws configure
```

#### Opção 2: Variáveis de Ambiente
```bash
export AWS_ACCESS_KEY_ID=sua_access_key
export AWS_SECRET_ACCESS_KEY=sua_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

#### Opção 3: Perfil AWS
```bash
export AWS_PROFILE=seu_perfil
```

### 5. Acesso aos Modelos do Amazon Bedrock
Certifique-se de ter acesso aos seguintes modelos no Amazon Bedrock:

- **Claude 4** (anthropic.claude-4)
- **Claude 3.7** (anthropic.claude-3-7)

Para solicitar acesso:
1. Acesse o console do Amazon Bedrock
2. Vá para "Model access" no menu lateral
3. Solicite acesso aos modelos necessários

### 6. Ollama Local (Para demos específicas)
Para executar as demos que utilizam modelos locais, instale o Ollama:

#### Instalação do Ollama:
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: baixe de https://ollama.ai/download
```

#### Download do modelo Llama 3:
```bash
ollama pull llama3
```

#### Iniciar o serviço Ollama:
```bash
ollama serve
```

### 7. API Key do OpenWeatherMap
Para as demos meteorológicas, você precisa de uma chave da API OpenWeatherMap:

1. Registre-se em: https://openweathermap.org/api
2. Obtenha sua API key gratuita
3. Configure a variável de ambiente:

```bash
export OPENWEATHER_API_KEY=sua_api_key_aqui
```

### 8. Verificação da Configuração
Execute este comando para verificar se tudo está configurado corretamente:

```bash
python -c "
import boto3
import os
print('✅ Boto3:', boto3.__version__)
print('✅ AWS Region:', boto3.Session().region_name)
print('✅ OpenWeather API Key:', '✅ Configurada' if os.getenv('OPENWEATHER_API_KEY') else '❌ Não configurada')
"
```

## 🚀 Executando as Demos

### Demo 1: Agente Mínimo
```bash
python 1_minimo.py
```

### Demo 2: Provedor de Modelo
```bash
python 2_provedor_modelo.py
```

### Demo 3: Agente com Ferramenta Customizada
```bash
python 3_agente_ferramenta_customizada.py
```

### Demo 4: Agente Meteorológico
```bash
python 4_agente_meteorologico.py
```

### Demo 5: Agente Meteorológico com Log
```bash
python 5_agente_meteorologico_com_log.py
```

### Demo 6: Fluxo de Trabalho Multi-Agente
```bash
cd 6_fluxo_de_trabalho_multi_agente
python 6_fluxo_de_trabalho_multi_agente.py
```

### Demo 7: Multi-Agentes como Ferramentas
```bash
cd 7_multi_agentes_como_ferramentas
python professor.py
```

### Demo 8: Multi-Agentes com Peer-to-Peer
```bash
cd 8_multi_agentes_com_peer_to_peer
python desenvolvimento_de_produto.py
```

## 📁 Estrutura do Projeto

```
aws-summit-2025/
├── 1_minimo.py                           # Demo básica de agente
├── 2_provedor_modelo.py                  # Configuração de provedores
├── 3_agente_ferramenta_customizada.py    # Agente com ferramentas customizadas
├── 4_agente_meteorologico.py             # Agente meteorológico básico
├── 5_agente_meteorologico_com_log.py     # Agente meteorológico com logging
├── 6_fluxo_de_trabalho_multi_agente/     # Demo de workflow multi-agente
├── 7_multi_agentes_como_ferramentas/     # Sistema de professor multi-agente
├── 8_multi_agentes_com_peer_to_peer/     # Comunicação peer-to-peer
├── logs/                                 # Arquivos de log das execuções
├── requirements.txt                      # Dependências Python
└── README.md                            # Este arquivo
```

## 🔧 Solução de Problemas

### Erro de Credenciais AWS
```
NoCredentialsError: Unable to locate credentials
```
**Solução**: Verifique se suas credenciais AWS estão configuradas corretamente.

### Erro de Acesso ao Bedrock
```
AccessDeniedException: User is not authorized to perform: bedrock:InvokeModel
```
**Solução**: Solicite acesso aos modelos no console do Amazon Bedrock.

### Erro de API Key OpenWeather
```
KeyError: 'OPENWEATHER_API_KEY'
```
**Solução**: Configure a variável de ambiente `OPENWEATHER_API_KEY`.

### Erro de Conexão Ollama
```
ConnectionError: Failed to connect to Ollama
```
**Solução**: Certifique-se de que o Ollama está rodando com `ollama serve`.

## 📚 Recursos Adicionais

- [Documentação Amazon Bedrock](https://docs.aws.amazon.com/bedrock/)
- [Strands Agents Framework](https://github.com/strands-ai/strands-agents)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Ollama Documentation](https://ollama.ai/docs)

## 🤝 Contribuição

Este é um projeto educacional para o AWS Summit 2025. Para dúvidas ou sugestões, entre em contato durante o evento.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

---

*Este material foi preparado para a sessão AIM307 do AWS Summit São Paulo 2025.*

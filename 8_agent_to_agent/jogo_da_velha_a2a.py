#!/usr/bin/env python3
"""
# Jogo da Velha com Agentes A2A (Implementação Nativa)

Este exemplo demonstra o uso do protocolo Agent-to-Agent (A2A) nativo do Strands Agents
para criar dois agentes de IA que jogam jogo da velha um contra o outro.

Cada agente:
- Tem sua própria identidade e estratégia
- Comunica-se diretamente com o outro agente usando a API nativa do Strands
- Toma decisões autônomas sobre seus movimentos

Referência: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agent-to-agent/
"""

from strands import Agent
from strands.models import BedrockModel
import json
import time
import random

# Modelo compartilhado para os agentes
bedrock_model = BedrockModel(model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

# Classe do jogo da velha
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def make_move(self, position):
        if self.game_over:
            return False
        
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self):
        # Linhas horizontais
        for i in range(0, 9, 3):
            if self.board[i] != ' ' and self.board[i] == self.board[i+1] == self.board[i+2]:
                self.winner = self.board[i]
                self.game_over = True
                return
        
        # Linhas verticais
        for i in range(3):
            if self.board[i] != ' ' and self.board[i] == self.board[i+3] == self.board[i+6]:
                self.winner = self.board[i]
                self.game_over = True
                return
        
        # Diagonais
        if self.board[0] != ' ' and self.board[0] == self.board[4] == self.board[8]:
            self.winner = self.board[0]
            self.game_over = True
            return
        
        if self.board[2] != ' ' and self.board[2] == self.board[4] == self.board[6]:
            self.winner = self.board[2]
            self.game_over = True
            return
        
        # Empate
        if ' ' not in self.board:
            self.game_over = True
    
    def get_board_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "game_over": self.game_over,
            "winner": self.winner
        }
    
    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")

# Agente estratégico
def create_strategic_agent(symbol):
    strategy_prompt = f"""
    Você é um agente de IA jogando jogo da velha como '{symbol}'.
    Seu objetivo é vencer o jogo usando estratégia.
    
    Regras do jogo:
    - O tabuleiro é numerado de 0 a 8:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    
    - Você deve escolher posições vazias (marcadas com ' ')
    - Você vence ao formar uma linha, coluna ou diagonal com seu símbolo
    
    Estratégia:
    1. Tente formar linhas, colunas ou diagonais com seu símbolo
    2. Bloqueie o oponente quando ele estiver prestes a vencer
    3. Prefira o centro (4) e os cantos (0, 2, 6, 8) quando disponíveis
    4. Pense à frente sobre possíveis jogadas futuras
    
    Quando receber uma mensagem com o estado do tabuleiro, analise-o e responda apenas com o número da posição escolhida (0-8).
    """
    
    return Agent(
        name=f"Strategic{symbol}Agent",
        model=bedrock_model,
        system_prompt=strategy_prompt
    )

# Agente agressivo
def create_aggressive_agent(symbol):
    strategy_prompt = f"""
    Você é um agente de IA jogando jogo da velha como '{symbol}'.
    Seu estilo é agressivo e focado em ataque.
    
    Regras do jogo:
    - O tabuleiro é numerado de 0 a 8:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    
    - Você deve escolher posições vazias (marcadas com ' ')
    - Você vence ao formar uma linha, coluna ou diagonal com seu símbolo
    
    Estratégia:
    1. Priorize formar linhas com seu símbolo, mesmo que isso signifique ignorar bloqueios
    2. Tente controlar o centro (4) e os cantos (0, 2, 6, 8)
    3. Seja imprevisível e surpreenda seu oponente
    4. Foque em vencer, não em impedir o oponente
    
    Quando receber uma mensagem com o estado do tabuleiro, analise-o e responda apenas com o número da posição escolhida (0-8).
    """
    
    return Agent(
        name=f"Aggressive{symbol}Agent",
        model=bedrock_model,
        system_prompt=strategy_prompt
    )

# Função para formatar o estado do tabuleiro para o agente
def format_board_message(game, agent_symbol):
    board_state = game.get_board_state()
    
    message = f"""
    Estado atual do tabuleiro:
    {board_state['board'][0]} | {board_state['board'][1]} | {board_state['board'][2]}
    ---------
    {board_state['board'][3]} | {board_state['board'][4]} | {board_state['board'][5]}
    ---------
    {board_state['board'][6]} | {board_state['board'][7]} | {board_state['board'][8]}
    
    Você é o jogador '{agent_symbol}'.
    É sua vez de jogar.
    
    Escolha uma posição (0-8) que esteja vazia para fazer sua jogada.
    Responda apenas com o número da posição escolhida.
    """
    
    return message

# Função para extrair a posição escolhida da resposta do agente
def extract_position(response, game):
    try:
        # Tentar extrair um número da resposta
        text = str(response).strip()
        for word in text.split():
            if word.isdigit() and 0 <= int(word) <= 8:
                return int(word)
        
        # Se não encontrar um número válido, tentar extrair o primeiro dígito
        for char in text:
            if char.isdigit() and 0 <= int(char) <= 8:
                return int(char)
        
        # Fallback para uma posição válida aleatória
        valid_positions = [i for i, val in enumerate(game.board) if val == ' ']
        return random.choice(valid_positions) if valid_positions else -1
    except:
        # Fallback para uma posição válida aleatória
        valid_positions = [i for i, val in enumerate(game.board) if val == ' ']
        return random.choice(valid_positions) if valid_positions else -1

# Função para executar o jogo
def run_tic_tac_toe_game():
    # Criar o jogo
    game = TicTacToe()
    
    # Criar os agentes
    agent_x = create_strategic_agent("X")
    agent_o = create_aggressive_agent("O")
    
    print("\n🎮 Jogo da Velha com Agentes A2A (Implementação Nativa) 🎮\n")
    print("Dois agentes de IA jogando jogo da velha usando o protocolo A2A nativo do Strands")
    print(f"Agente X: {agent_x.name} (Estratégico)")
    print(f"Agente O: {agent_o.name} (Agressivo)")
    print("\nIniciando jogo...\n")
    
    # Iniciar o jogo
    current_agent = agent_x
    other_agent = agent_o
    current_symbol = "X"
    
    # Criar uma conversa entre os agentes
    conversation_id = f"tic-tac-toe-{int(time.time())}"
    
    while not game.game_over:
        print(f"\nVez do {current_agent.name} ({current_symbol})")
        game.print_board()
        
        # Formatar a mensagem com o estado do tabuleiro
        board_message = format_board_message(game, current_symbol)
        
        # Enviar mensagem diretamente para o outro agente usando a API nativa A2A
        response = current_agent.send_message(
            recipient=other_agent,
            message=board_message,
            conversation_id=conversation_id
        )
        
        # Extrair a posição escolhida
        position = extract_position(response, game)
        
        if 0 <= position <= 8:
            move_success = game.make_move(position)
            if move_success:
                print(f"{current_agent.name} ({current_symbol}) escolheu a posição {position}")
            else:
                print(f"Movimento inválido! {current_agent.name} perde a vez.")
        else:
            print(f"Resposta inválida do {current_agent.name}. Perde a vez.")
        
        # Trocar os agentes e símbolos
        current_agent, other_agent = other_agent, current_agent
        current_symbol = "O" if current_symbol == "X" else "X"
    
    # Jogo terminou
    print("\nJogo finalizado!")
    game.print_board()
    
    if game.winner:
        winner_agent = agent_x if game.winner == "X" else agent_o
        winner_symbol = game.winner
        print(f"\nVencedor: {winner_agent.name} ({winner_symbol})")
        
        # Notificar os agentes sobre o resultado
        winner_agent.send_message(
            recipient=agent_o if winner_agent == agent_x else agent_x,
            message=f"Eu venci o jogo! O resultado final foi: {game.winner}",
            conversation_id=conversation_id
        )
    else:
        print("\nEmpate!")
        
        # Notificar os agentes sobre o empate
        agent_x.send_message(
            recipient=agent_o,
            message="O jogo terminou em empate.",
            conversation_id=conversation_id
        )
    
    # Mostrar estatísticas
    print("\nEstatísticas de comunicação:")
    print(f"ID da conversa: {conversation_id}")

if __name__ == "__main__":
    try:
        run_tic_tac_toe_game()
        
        while True:
            play_again = input("\nDeseja jogar novamente? (s/n): ")
            if play_again.lower() != 's':
                print("\nObrigado por assistir ao jogo!")
                break
            run_tic_tac_toe_game()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido. Saindo...")
    except Exception as e:
        print(f"\nOcorreu um erro: {str(e)}")

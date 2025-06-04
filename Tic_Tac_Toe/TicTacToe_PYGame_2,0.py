# Tic Tac Toe Game using Pygame with a enhanced bot player & GUI.

# Make sure to run this code in an environment where Pytjon & Pygame is installed.
# If pygame is not installed, you can install it using:    "pip install pygame"


import pygame
import random


pygame.init()


width, height = 650, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("...                                                                                               Tic Tac Toe")


background_color = (173, 216, 230)
line_color = (0, 0, 139) 
x_color = (0, 0, 0) 
o_color = (255, 255, 255)
notice_color = (0, 0, 0)  
button_play_friend_color = (0, 128, 0) 
button_play_bot_color = (0, 0, 255)  
button_hover_color = (0, 84, 153) 


font_large = pygame.font.Font(None, 170)
font_medium = pygame.font.Font(None, 50)  
font_small = pygame.font.Font(None, 30)
font_bold = pygame.font.Font(None, 50)  


lst = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
used = []
corner = [0, 2, 6, 8]
available = [0, 1, 2, 3, 4, 5, 6, 7, 8]
player_01 = "Player 01 "
player_02 = "Player 02 "
current_turn = "X"
winner = None
game_mode = None


def draw_board():
    screen.fill(background_color)
    for x in range(1, 3):
        pygame.draw.line(screen, line_color, (0, height / 3 * x), (width, height / 3 * x), 6)
        pygame.draw.line(screen, line_color, (width / 3 * x, 0), (width / 3 * x, height), 6)
    for i, mark in enumerate(lst):
        if mark != '-':
            pos = ((i % 3) * (width / 3) + (width / 6), (i // 3) * (height / 3) + (height / 6))
            draw_mark(mark, pos)

def draw_mark(mark, pos):
    color = x_color if mark == "X" else o_color
    text = font_large.render(mark, True, color)
    text_rect = text.get_rect(center=pos)
    screen.blit(text, text_rect)

def check_winner(mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6] 
    ]
    for condition in win_conditions:
        if all(lst[i] == mark for i in condition):
            return True
    return False

def play_with_bot():
    for i in available:
        lst[i] = "O"
        if check_winner("O"):
            lst[i] = "-"
            return i
        lst[i] = "-"

 
    for i in available:
        lst[i] = "X"
        if check_winner("X"):
            lst[i] = "-"
            return i
        lst[i] = "-"


    if 4 in available:
        return 4


    available_corners = [c for c in corner if c in available]
    if available_corners:
        return random.choice(available_corners)

   
    return random.choice(available)

def reset_game():
    global lst, used, corner, available, current_turn, winner
    lst = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    used = []
    corner = [0, 2, 6, 8]
    available = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    current_turn = "X"
    winner = None

def display_message(message):
    screen.fill(background_color)
    text = font_bold.render(message, True, notice_color)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)


def draw_mode_selection(selected_mode=None):
    screen.fill(background_color)
    
   
    button_width, button_height = 300, 120
    spacing = 50
    play_friend_rect = pygame.Rect((width - button_width) // 2, height // 2 - button_height - spacing, button_width, button_height)
    play_bot_rect = pygame.Rect((width - button_width) // 2, height // 2 + spacing, button_width, button_height)
    
  
    if selected_mode == 1:
        pygame.draw.rect(screen, button_hover_color, play_friend_rect)
    else:
        pygame.draw.rect(screen, button_play_friend_color, play_friend_rect)
    
    if selected_mode == 2:
        pygame.draw.rect(screen, button_hover_color, play_bot_rect)
    else:
        pygame.draw.rect(screen, button_play_bot_color, play_bot_rect)
    

    text1 = font_medium.render("Play with Friend", True, background_color)
    text2 = font_medium.render("Play with Bot", True, background_color)
    screen.blit(text1, (play_friend_rect.x + (button_width - text1.get_width()) // 2, play_friend_rect.y + (button_height - text1.get_height()) // 2))
    screen.blit(text2, (play_bot_rect.x + (button_width - text2.get_width()) // 2, play_bot_rect.y + (button_height - text2.get_height()) // 2))
    
    pygame.display.flip()
    return play_friend_rect, play_bot_rect


running = True
game_mode_selected = False

while running:
    if not game_mode_selected:
        play_friend_rect, play_bot_rect = draw_mode_selection()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = 1
                    game_mode_selected = True
                elif event.key == pygame.K_2:
                    game_mode = 2
                    game_mode_selected = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_friend_rect.collidepoint(event.pos):
                    game_mode = 1
                    game_mode_selected = True
                elif play_bot_rect.collidepoint(event.pos):
                    game_mode = 2
                    game_mode_selected = True
    else:
        draw_board()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                x, y = event.pos
                index = (x // (width // 3)) + (y // (height // 3)) * 3
                if index in available:
                    lst[index] = current_turn
                    used.append(index)
                    available.remove(index)
                    if index in corner:
                        corner.remove(index)
                    
                    if check_winner(current_turn):
                        winner = current_turn
                        display_message(f"{player_01 if current_turn == 'X' else 'BOT'} wins!")
                        reset_game()
                        game_mode_selected = False
                    elif len(used) == 9:
                        winner = "Tie"
                        display_message("It's a Tie!")
                        reset_game()
                        game_mode_selected = False
                    else:
                        current_turn = "O" if current_turn == "X" else "X"
                        if game_mode == 2 and current_turn == "O":
                            bot_move = play_with_bot()
                            lst[bot_move] = "O"
                            used.append(bot_move)
                            available.remove(bot_move)
                            if bot_move in corner:
                                corner.remove(bot_move)
                            if check_winner("O"):
                                winner = "O"
                                display_message("BOT wins!")
                                reset_game()
                                game_mode_selected = False
                            else:
                                current_turn = "X" 

pygame.quit()
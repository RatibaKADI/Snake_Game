import curses
import random

screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()

window = curses.newwin(screen_height, screen_width, 0, 0)

# Activer le mode clavier en passant True en argument
window.keypad(True)
window.timeout(100)
snk_x = screen_width // 4
snk_y = screen_height // 2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Créer la nourriture au milieu de la fenêtre
food = [screen_height // 2, screen_width // 2]
# Ajouter le caractère de nourriture
window.addch(food[0], food[1], curses.ACS_DIAMOND)
#window.addch(food[0], food[1], curses.ACS_DIAMOND | curses.color_pair(1))


# Définir la première direction à droite
key = curses.KEY_RIGHT

# Boucle de jeu
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # Nouvelle tête du serpent
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    # Collision avec les bords ou lui-même
    if (snake[0][0] in [0, screen_height] or 
    snake[0][1] in [0, screen_width] or 
    snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Manger de la nourriture
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        # Retirer la dernière partie du corps du serpent
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Mettre à jour la position du serpent
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


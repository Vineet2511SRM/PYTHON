import pygame
import random
import time

# --- Configuration & Colors ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Palettes
WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
GRAY = (100, 100, 100)
BLUE = (50, 100, 255)
BROWN = (139, 69, 19)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
PURPLE = (140, 50, 220) 
VICTORY_BG = (220, 255, 220) 

pygame.init()
font = pygame.font.SysFont("Consolas", 24)
header_font = pygame.font.SysFont("Consolas", 36, bold=True)
victory_font = pygame.font.SysFont("Consolas", 60, bold=True)

def draw_victory_banner(screen, text="GOAL ACHIEVED"):
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.set_alpha(100) 
    s.fill(GREEN)
    screen.blit(s, (0,0))

    text_surf = victory_font.render(text, True, BLACK)
    bg_rect = text_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    bg_rect.inflate_ip(40, 20)
    
    pygame.draw.rect(screen, WHITE, bg_rect, border_radius=15)
    pygame.draw.rect(screen, BLACK, bg_rect, 2, border_radius=15)
    
    rect = text_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(text_surf, rect)

    sub_surf = font.render("State: Clean | Action: NoOp", True, BLACK)
    sub_rect = sub_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
    screen.blit(sub_surf, sub_rect)

def run_classic_mode(screen):
    agent_loc = "A" 
    world_state = {"A": True, "B": True} 
    agent_belief = {"A": "Unknown", "B": "Unknown"}
    
    score = 0
    running = True
    finished = False
    action = "START"

    def randomize_dirt():
        return {
            "A": random.choice([True, False]),
            "B": random.choice([True, False])
        }

    while running:
        bg_color = VICTORY_BG if finished else WHITE
        screen.fill(bg_color)

        pygame.draw.rect(screen, BLACK, (100, 200, 250, 250), 5)
        pygame.draw.rect(screen, BLACK, (450, 200, 250, 250), 5)
        
        screen.blit(header_font.render("A", True, BLACK), (210, 160))
        screen.blit(header_font.render("B", True, BLACK), (560, 160))

        if world_state["A"]: pygame.draw.circle(screen, BROWN, (225, 325), 60)
        if world_state["B"]: pygame.draw.circle(screen, BROWN, (575, 325), 60)

        agent_x = 225 if agent_loc == "A" else 575
        agent_rect = pygame.Rect(agent_x - 40, 285, 80, 80)

        agent_color = PURPLE if action == "NoOp" else RED
        pygame.draw.rect(screen, agent_color, agent_rect, border_radius=10)

        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, 120))
        screen.blit(font.render("CLASSIC MODE (2 rooms)", True, WHITE), (20, 20))
        screen.blit(font.render(f"Belief State: {agent_belief}", True, GREEN), (20, 50))
        screen.blit(font.render("Press 'R' to Randomize Dirt", True, (150, 150, 150)), (20, 80))
        
        action_color = PURPLE if action == "NoOp" else BLUE
        screen.blit(header_font.render(f"ACTION: {action}", True, action_color), (300, 500))

        if finished:
            draw_victory_banner(screen)

        pygame.display.flip()
        
        time.sleep(1.0) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                if event.key == pygame.K_r: 
                    world_state = randomize_dirt()
                    agent_belief = {"A": "Unknown", "B": "Unknown"}
                    finished = False
                    action = "RESET"
                    score = 0

        if not finished and action != "RESET":
            is_current_dirty = world_state[agent_loc]
            agent_belief[agent_loc] = "Dirty" if is_current_dirty else "Clean"

            if agent_belief["A"] == "Clean" and agent_belief["B"] == "Clean":
                action = "NoOp"
                finished = True
                
            elif is_current_dirty:
                action = "SUCK"
                world_state[agent_loc] = False
                score += 10
                
            elif agent_loc == "A":
                action = "RIGHT"
                agent_loc = "B"
                score -= 1
                
            elif agent_loc == "B":
                action = "LEFT"
                agent_loc = "A"
                score -= 1
        elif action == "RESET":
            action = "START"

def run_grid_mode(screen):
    GRID_SIZE = 10 
    CELL = 600 // GRID_SIZE
    OFFSET_X = 200 
    
    grid = [[1 if random.random() < 0.4 else 0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    visited = set()
    ax, ay = 0, 0 
    visited.add((ax, ay))
    stack = [(ax, ay)] 
    
    score = 0
    finished = False
    action = "START"
    delay = 0.1
    
    running = True
    while running:
        bg_color = VICTORY_BG if finished else BLACK
        screen.fill(bg_color)

        pygame.draw.rect(screen, (30, 30, 30), (0, 0, OFFSET_X, SCREEN_HEIGHT))
        screen.blit(font.render("GRID MODE", True, WHITE), (10, 20))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 90))
        
        act_color = PURPLE if action == "NoOp" else BLUE
        screen.blit(font.render(f"Action:{action}", True, act_color), (5, 210))

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(OFFSET_X + x*CELL, y*CELL, CELL, CELL)
                
                color = (50, 50, 50) 
                if (x, y) in visited: color = (100, 100, 150) 
                if grid[y][x] == 1: color = (100, 50, 0) 
                if (x, y) == (ax, ay): color = PURPLE if finished else RED
                
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1) 
                
                if grid[y][x] == 1:
                    pygame.draw.circle(screen, (150, 100, 50), (OFFSET_X + x*CELL + CELL//2, y*CELL + CELL//2), CELL//4)

        if finished:
            draw_victory_banner(screen)

        pygame.display.flip()
        time.sleep(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                if event.key == pygame.K_UP: delay = max(0.01, delay - 0.05)
                if event.key == pygame.K_DOWN: delay += 0.05
        if not finished:

            if grid[ay][ax] == 1:
                action = "SUCK"
                grid[ay][ax] = 0
                score += 10
            else:
                moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                unvisited_neighbors = []
                
                for dx, dy in moves:
                    nx, ny = ax + dx, ay + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        if (nx, ny) not in visited:
                            unvisited_neighbors.append((nx, ny))

                if unvisited_neighbors:
                    action = "EXPLORE (Rand)"
                    nx, ny = random.choice(unvisited_neighbors)
                    ax, ay = nx, ny
                    visited.add((ax, ay))
                    stack.append((ax, ay))
                    score -= 1

                elif len(stack) > 1:
                    action = "BACKTRACK"
                    stack.pop()
                    ax, ay = stack[-1]
                    score -= 1

                else:
                    finished = True
                    action = "NoOp"

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Vacuum World Problem")
    
    while True:
        screen.fill((30, 30, 40))
        title = header_font.render("VACUUM WORLD", True, WHITE)
        opt1 = font.render("1. Classic", True, GREEN)
        opt2 = font.render("2. Grid", True, BLUE)
        exit_txt = font.render("Press 1 or 2 (Esc to Quit)", True, (150, 150, 150))
        
        screen.blit(title, (250, 100))
        screen.blit(opt1, (250, 250))
        screen.blit(opt2, (250, 300))
        screen.blit(exit_txt, (250, 450))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: run_classic_mode(screen)
                if event.key == pygame.K_2: run_grid_mode(screen)
                if event.key == pygame.K_ESCAPE: pygame.quit(); return

if __name__ == "__main__":
    main_menu()
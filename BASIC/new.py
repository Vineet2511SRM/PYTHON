import pygame 
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DNA Strand Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# DNA parameters
dna_radius = 100
num_turns = 10
angle_increment = math.pi / 12  # Angle step for helix
base_pairs = [('A', 'T'), ('G', 'C')]  # Base pairs

# Function to draw the DNA helix
def draw_dna():
    screen.fill(WHITE)
    for i in range(num_turns * 12):
        angle = i * angle_increment
        x1 = int(WIDTH // 2 + dna_radius * math.cos(angle))
        y1 = int(HEIGHT // 2 + dna_radius * math.sin(angle) + i * 2)
        
        # Complementary strand
        x2 = int(WIDTH // 2 - dna_radius * math.cos(angle))
        
        # Base pair colors
        if i % 2 == 0:
            color = BLUE
            base_pair = base_pairs[i % 2]
        else:
            color = RED
            base_pair = base_pairs[(i+1) % 2]
        
        # Draw base pairs
        pygame.draw.circle(screen, color, (x1, y1), 5)
        pygame.draw.circle(screen, color, (x2, y1), 5)
        
        # Display base pair labels
        font = pygame.font.SysFont(None, 24)
        text1 = font.render(base_pair[0], True, BLACK)
        text2 = font.render(base_pair[1], True, BLACK)
        screen.blit(text1, (x1, y1))
        screen.blit(text2, (x2, y1))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    # Draw DNA
    draw_dna()
    pygame.display.flip()

# Quit Pygame
pygame.quit()

def edit_sequence(sequence):
    # Edit a random base pair in the sequence
    edit_index = random.randint(0, len(sequence) - 1)
    new_base = random.choice(base_pairs)
    sequence[edit_index] = new_base
    return sequence

def simulate_inheritance(parent1, parent2):
    offspring = []
    for i in range(len(parent1)):
        gene_from_mom = parent1[i]
        gene_from_dad = parent2[i]
        if random.random() > 0.5:
            offspring.append(gene_from_mom)
        else:
            offspring.append(gene_from_dad)
    return offspring

# Example genes from both parents
parent1_genes = [('A', 'T'), ('G', 'C'), ('G', 'C'), ('A', 'T')]
parent2_genes = [('A', 'T'), ('A', 'T'), ('G', 'C'), ('G', 'C')]

offspring_genes = simulate_inheritance(parent1_genes, parent2_genes)
print("Offspring Genes:", offspring_genes)

# Traits prediction based on simple Mendelian rules
def predict_traits(offspring_genes):
    trait_counts = {"Dominant": 0, "Recessive": 0}
    for gene in offspring_genes:
        if gene == ('A', 'G') or gene == ('T', 'C'):
            trait_counts["Dominant"] += 1
        else:
            trait_counts["Recessive"] += 1
    
    # Display probabilities
    dominant_ratio = trait_counts["Dominant"] / len(offspring_genes)
    recessive_ratio = trait_counts["Recessive"] / len(offspring_genes)
    print(f"Probability of Dominant Traits: {dominant_ratio*100}%")
    print(f"Probability of Recessive Traits: {recessive_ratio*100}%")

# Run prediction
predict_traits(offspring_genes)



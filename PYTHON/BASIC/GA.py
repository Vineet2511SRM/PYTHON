import pygame
import random
import string

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genetic Algorithm Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)


# Genetic Algorithm Parameters
TARGET = "HELLO GENETIC ALGORITHM"
POP_SIZE = 100
MUTATION_RATE = 0.01
GENERATION = 0

# Function to create a random string of the same length as the TARGET
def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + " ") for _ in range(length))

# Individual class representing a single solution
class Individual:
    def __init__(self, dna=None):
        self.dna = dna if dna else random_string(len(TARGET))
        self.fitness = 0

    def calculate_fitness(self):
        self.fitness = sum(1 for i, char in enumerate(self.dna) if char == TARGET[i])

    def mutate(self):
        dna_list = list(self.dna)
        for i in range(len(dna_list)):
            if random.random() < MUTATION_RATE:
                dna_list[i] = random.choice(string.ascii_uppercase + " ")
        self.dna = ''.join(dna_list)

# Genetic Algorithm functions
def create_population(size):
    return [Individual() for _ in range(size)]

def select_parents(population):
    return random.choices(
        population, weights=[ind.fitness for ind in population], k=2
    )

def crossover(parent1, parent2):
    midpoint = random.randint(0, len(parent1.dna))
    child_dna = parent1.dna[:midpoint] + parent2.dna[midpoint:]
    return Individual(child_dna)

# Evolve a new generation
def evolve_population(population):
    global GENERATION
    GENERATION += 1
    new_population = []
    for _ in range(len(population)):
        parent1, parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        child.mutate()
        child.calculate_fitness()
        new_population.append(child)
    return new_population

# Display information on screen
def display_info(generation, best_individual):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 36)
    text1 = font.render(f"Generation: {generation}", True, BLACK)
    text2 = font.render(f"Best Fit: {best_individual.dna}", True, BLUE)
    text3 = font.render(f"Fitness: {best_individual.fitness}", True, BLACK)
    screen.blit(text1, (20, 20))
    screen.blit(text2, (20, 80))
    screen.blit(text3, (20, 140))

# Initialize population
population = create_population(POP_SIZE)
for individual in population:
    individual.calculate_fitness()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Evolve population and find the best individual
    population = evolve_population(population)
    best_individual = max(population, key=lambda ind: ind.fitness)
    
    # Display the current generation and the best solution found so far
    display_info(GENERATION, best_individual)
    pygame.display.flip()
    
    # Slow down the loop with a delay
    pygame.time.delay(10)  # Delay of 100 milliseconds per generation
    
    # Check if the target is reached
    if best_individual.dna == TARGET:
        print(f"Target reached in generation {GENERATION}")
        running = False

if running == False:
    out = input("Press any key to exit.")
    pygame.quit()

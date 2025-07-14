import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
num_creatures = 10
num_food_sources = 20
mutation_rate = 0.01
max_generations = 5000
steps_per_gen = 50
initial_learning_rate = 0.01  
learning_rate_increase = 0.005  
creatures = np.random.rand(num_creatures, 2) * 100
food_sources = np.random.rand(num_food_sources, 2) * 100
def fitness(creature, food_sources):
    distances = np.linalg.norm(food_sources - creature, axis=1)
    return 1 / np.min(distances)
def selection(fitness_scores):
    total_fitness = np.sum(fitness_scores)
    probabilities = fitness_scores / total_fitness
    return np.random.choice(len(fitness_scores), p=probabilities)

#produce offspring
def crossover(parent1, parent2):
    crossover_point = np.random.randint(len(parent1))
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] += np.random.randn() * 0.1
    return individual


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.set_title("Creature Movement")
ax2.set_title("Fitness Over Generations")
ax2.set_xlabel("Generation")
ax2.set_ylabel("Fitness")
fitness_history = []  

def update(frame):
    global creatures, food_sources, learning_rate

    
    if frame >= max_generations:
        print("Maximum generations reached. Stopping execution.")
        out = input("Press any key to exit")
        plt.close(fig)
        return  

    learning_rate = min(initial_learning_rate + (frame // steps_per_gen) * learning_rate_increase, 1.0)

    
    for i in range(num_creatures):
        closest_food = np.argmin(np.linalg.norm(food_sources - creatures[i], axis=1))
        direction_to_food = food_sources[closest_food] - creatures[i]
        direction_to_food /= np.linalg.norm(direction_to_food)

        random_direction = np.random.randn(2) * 0.1
        movement = (1 - learning_rate) * random_direction + learning_rate * direction_to_food

        creatures[i] += movement
        creatures[i] = np.clip(creatures[i], 0, 100)

        
        if np.linalg.norm(food_sources[closest_food] - creatures[i]) < 1:
            food_sources[closest_food] = np.random.rand(2) * 100

    
    ax1.clear()
    ax1.scatter(creatures[:, 0], creatures[:, 1], s=20, c='blue')
    ax1.scatter(food_sources[:, 0], food_sources[:, 1], s=50, c='red')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.set_title(f"Generation: {frame // steps_per_gen + 1}")

    
    if frame % steps_per_gen == steps_per_gen - 1:
        fitness_scores = np.array([fitness(creature, food_sources) for creature in creatures])
        average_fitness = np.mean(fitness_scores)
        best_fitness = np.max(fitness_scores)

    
        fitness_history.append((average_fitness, best_fitness))

        new_generation = []
        for _ in range(num_creatures):
            parent1 = creatures[selection(fitness_scores)]
            parent2 = creatures[selection(fitness_scores)]
            child1, child2 = crossover(parent1, parent2)
            new_generation.append(mutation(child1, mutation_rate))
            new_generation.append(mutation(child2, mutation_rate))
        creatures = np.array(new_generation)

    
    ax2.clear()
    ax2.set_title("Fitness Over Generations")
    ax2.set_xlabel("Generation")
    ax2.set_ylabel("Fitness")
    generations = range(1, len(fitness_history) + 1)
    average_fitness_values = [fit[0] for fit in fitness_history]
    best_fitness_values = [fit[1] for fit in fitness_history]

    ax2.plot(generations, average_fitness_values, label='Average Fitness', color='blue')
    ax2.plot(generations, best_fitness_values, label='Best Fitness', color='orange')
    ax2.legend()
    
    if best_fitness_values:
        ax2.set_ylim(0, max(best_fitness_values) * 1.1)  

ani = animation.FuncAnimation(fig, update, frames=max_generations * steps_per_gen, interval=10)

plt.show()
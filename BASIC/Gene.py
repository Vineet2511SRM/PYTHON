import random
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
parent1_genes = ['A-T', 'G-C', 'G-C', 'A-T']
parent2_genes = ['A-T', 'A-T', 'G-C', 'G-C']

offspring_genes = simulate_inheritance(parent1_genes, parent2_genes)
print("Offspring Genes:", offspring_genes)

# Traits prediction based on simple Mendelian rules
def predict_traits(offspring_genes):
    trait_counts = {"Dominant": 0, "Recessive": 0}
    for gene in offspring_genes:
        if gene == ('A', 'T') or gene == ('G', 'C'):
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

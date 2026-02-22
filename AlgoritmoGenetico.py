# algoritimo genético

import random
from tqdm.auto import tqdm

def generate_population(size=100, dimensions=8):
  """
  Define a quantidade da populacao inicial e a dimensão do tabuleiro das rainhas.
  """
  population = []
  for i in range(size):
    while(True):
      individual = []
      for j in range(dimensions):
        individual.append(random.randint(1, dimensions))
      if individual not in population:
        break
    population.append(individual)
  return population

def fitness_fn(individual):
  """
  Calcula o "fitness" de um estado. "individual" se refere a lista com as posições das rainhas em um determinado estado.
  """
  fitness = 0
  for i in range(0, len(individual) - 1):
    for j in range(i+1, len(individual)):
      if individual[i] == individual[j]:
        fitness += 1
      if abs(i - j) == abs(individual[i] - individual[j]):
        fitness += 1
  return fitness

def random_selection(population, fitness):
  """
  Seleciona aleatoriamente um individuo, podendo ser uma combinação entre dois genes fortes ou um gene forte e um aleatório.
  """
  selected = selection(population, fitness, num_selected=2)
  random_selected = random.choice(population)
  if random.random() < 0.5:
    strongest_gene = selected[0]
    another_strong = selected[1]
  else:
    strongest_gene = selected[1]
    another_strong = selected[0]

  if random.random() < 0.5:
    return strongest_gene, random_selected
  else:
    return another_strong, strongest_gene

def selection(population, fitness, num_selected=1):
  """
  Seleciona o melhor "fit" dentre a população.
  """
  sorted_population = sorted(population, key=fitness)
  best = sorted_population[:num_selected]
  if num_selected == 1:
    return best[0]
  return best

def mutate(individual):
  """
  Realiza uma mutação (uma alteração de posição de uma rainha) em um determinado indice.
  """
  idx = random.randint(0, len(individual) - 1)
  individual[idx] = random.randint(1, len(individual))
  return individual

def reproduce(x, y):
  """
  Realiza uma reprodução de dois estados.
  """
  n = len(x)
  c = random.randint(0, n-1)
  if random.random() < 0.5:
    child = x[:c] + y[c:]
  else:
    child = y[:c] + x[c:]
  return child

def genetic_algorithm(population, fitness, num_generations=20, mutation_rate=0.01):
  """
  Executa o algoritmo genético na população fornecida pelo numero de gerações inseridos, seguindo a taxa de mutação
  também inserida e a função de fitness.
  """
  best_individual = random.choice(population)

  best_per_generation = []
  for i in tqdm(range(num_generations)):
    new_population = []
    for j in range(len(population)):
      x, y = random_selection(population, fitness)
      child = reproduce(x, y)
      if random.random() <= mutation_rate:
        child = mutate(child)
      new_population.append(child)

    population = new_population
    current_best_individual = selection(population, fitness)

    fitness_current = fitness(current_best_individual)
    fitness_best = fitness(best_individual)
    if fitness_current < fitness_best:
      best_individual = current_best_individual

    best_per_generation.append(best_individual)
    print(f'{best_individual}: {fitness_best}')

  return best_individual, best_per_generation


# Streamlit

import streamlit as st
import matplotlib.pyplot as plt

st.title("Algoritmo Genético: Problema das N-Rainhas")

st.write("""
Visualização do Algoritmo Genético aplicado ao problema das N-Rainhas.
Use os controles abaixo para configurar o experimento.
""")

num_queens = st.slider("Número de rainhas (N):", 4, 15, 8)
num_generations = st.slider("Número de gerações:", 10, 1500, 500)
initial_population = st.slider("Tamanho inicial da população:", 10, 2000, 100)
mutation_rate = st.slider("Taxa de mutação:", 0.0, 0.7, 0.01)

def plot_board(individual):
    n = len(individual)
    fig, ax = plt.subplots(figsize=(n, n))

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                ax.add_patch(
                    plt.Rectangle((j, i), 1, 1, fill=True, alpha=0.3)
                )

    # Desenhar rainhas
    for col, row in enumerate(individual):
        ax.text(
            col + 0.5,
            row - 0.5,
            "♛",
            fontsize=28,
            ha='center',
            va='center'
        )

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Tabuleiro de Xadrez - N Rainhas")
    ax.set_aspect('equal')
    ax.invert_yaxis()

    st.pyplot(fig)

if 'history' not in st.session_state:
    st.session_state.history = None

if st.button("Executar Algoritmo Genético"):

    with st.spinner("Executando algoritmo genético...", show_time=True):
        population = generate_population(
            size=initial_population,
            dimensions=num_queens
        )

        best, best_per_generation = genetic_algorithm(
            population,
            fitness_fn,
            num_generations=num_generations,
            mutation_rate=mutation_rate
        )

    best_fitness = fitness_fn(best)

    st.success(f"Melhor indivíduo: {best}")
    st.info(f"Fitness (número de conflitos): {best_fitness}")

    st.session_state.history = best_per_generation

    # Renderizar tabuleiro com Pyplot
if st.session_state.history is not None:
    selected_gen = st.slider("Ver evolução da Geração:", 1, len(st.session_state.history))
    st.info(f"Fitness (número de conflitos): {fitness_fn(st.session_state.history[selected_gen-1])} \n Individuo: {st.session_state.history[selected_gen-1]}")
    plot_board(st.session_state.history[selected_gen-1])
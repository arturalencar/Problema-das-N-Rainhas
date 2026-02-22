# Algoritmo Genético: Problema das N-Rainhas 👑

Este repositório contém uma implementação do clássico **Problema das N-Rainhas** resolvido através de um **Algoritmo Genético**. Além da lógica computacional, o projeto foca na experiência do usuário ao fornecer uma interface gráfica interativa onde é possível visualizar a evolução da solução em tempo real.

## Equipe do Projeto
- Carlos Artur Alencar Cruz
- Guilherme Inácio Santos Paes
- Irwing Felipe Pereira Vieira
- Raphael Matos da Silva Gonçalves
- Renan Nunes Andrade Sampaio

## 💻 Sobre o Projeto

### Funcionalidades da Interface (Front-end)
* **Controles Interativos:** Sliders para ajuste instantâneo dos hiperparâmetros (Número de Rainhas, Gerações, População e Mutação).
* **Renderização Visual:** Plotagem dinâmica do tabuleiro de xadrez e das rainhas usando Matplotlib, adaptando-se automaticamente ao tamanho de `N` escolhido.
* **Histórico de Evolução:** Capacidade de navegar por gerações passadas e visualizar o estado do tabuleiro e a diminuição dos conflitos ao longo do tempo.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem base para a lógica do algoritmo genético.
* **Streamlit:** Framework para a construção da interface web interativa.
* **Matplotlib:** Renderização gráfica bidimensional do tabuleiro.
* **Tqdm:** Barra de progresso para o acompanhamento do processamento no terminal.

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina.

### 2. Instalação das Dependências
Execute o seguinte comando no seu terminal para instalar as bibliotecas necessárias:

```bash
pip install streamlit matplotlib tqdm
```
(Nota para usuários Linux/WSL: Caso enfrente problemas de pacotes do sistema ao instalar as bibliotecas, atualize sua lista de pacotes com sudo apt update antes de rodar o comando acima).

### 3. Rodando a Aplicação
Inicie o servidor local do Streamlit executando o arquivo principal:

```bash
python -m streamlit run AlgoritmoGenetico.py
```
(Se o diretório de binários do Python já estiver configurado no seu PATH, você pode usar apenas ```streamlit run AlgoritmoGenetico.py```)

Acesse a interface no seu navegador através do endereço gerado no terminal (geralmente ```http://localhost:8501```).
#

### 🧠 Estrutura do Algoritmo
O Algoritmo Genético simula o processo de evolução natural dividido nas seguintes etapas:

- **População Inicial:** Geração de distribuições aleatórias de rainhas no tabuleiro.

- **Fitness (Aptidão):** Função que calcula o número de conflitos (ataques mútuos) entre as rainhas. O objetivo principal da aplicação é minimizar esse valor a zero.

- **Seleção e Crossover (Cruzamento):** Escolha dos melhores indivíduos da geração atual para reprodução, misturando seus "genes" (posições das rainhas) para criar uma nova geração de descendentes.

- **Mutação:** Alteração aleatória da posição de uma ou mais rainhas em um indivíduo para garantir a diversidade genética da população e evitar que o algoritmo fique preso em mínimos locais.

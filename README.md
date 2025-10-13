# Implementações de Computação Gráfica para a N1

## Implementação 5 - Quadtree with Canvas 2D

Este projeto implementa uma **Quadtree interativa** utilizando **HTML5 Canvas 2D** e **JavaScript puro**.
A aplicação desenha um quadrado principal que pode ser **subdividido em quatro quadrantes** ao ser clicado.
Cada subdivisão segue o mesmo princípio recursivo, permitindo visualizar de forma intuitiva a estrutura hierárquica da Quadtree.

🛠️ **Tecnologias**

* **HTML5 Canvas 2D** — para renderização gráfica dos quadrantes
* **JavaScript (ES6+)** — para manipulação de eventos e lógica de subdivisão
* **CSS** — para estilização simples da interface

💡 **Conceito**

A **Quadtree** é uma estrutura de dados hierárquica amplamente usada em computação gráfica, compressão de imagens e simulações físicas.
Ela divide recursivamente uma área bidimensional em quatro partes menores, facilitando operações espaciais como detecção de colisão e indexação geográfica.

---

## Implementação 7 - The Labyrinth of Zelda

Um mini-jogo 2D de aventura e puzzle com labirintos gerados proceduralmente, desenvolvido em Python utilizando PyGame.

📜 Sobre o Jogo  
Inspirado nos clássicos jogos de aventura e puzzle, "The Labyrinth of Zelda" coloca o jogador em um labirinto que muda a cada partida. O objetivo é explorar, encontrar todos os fragmentos da Triforce espalhados pelo mapa e escapar pelo portal que se abre após completar a coleta.  
O principal desafio técnico foi a criação de um algoritmo de geração procedural de labirintos, garantindo que cada nível seja único, jogável e possua sempre um caminho válido até a saída.

✨ Features  
- 🌀 Labirintos Infinitos: Gerados com o algoritmo recursive backtracking, permitindo infinitas combinações.  
- 🧱 Sistema de Colisão: Baseado em retângulos, impede que o jogador atravesse as paredes.  
- 🎯 Progressão Simples: Colete todos os fragmentos da Triforce para liberar o portal e avançar.  
- 🔊 Feedback Visual e Sonoro: Sprite do jogador muda conforme o movimento; música de fundo e efeitos sonoros para passos, coleta de itens e conclusão de nível.

🚀 Como Executar  
**Pré-requisitos:**  
- Python 3 instalado no sistema.

**Instalação e Execução:**  
1. Clone este repositório ou baixe os arquivos:  
   `git clone https://github.com/seu-usuario/implementacoes-computacao-grafica.git`  
2. Acesse a pasta do projeto:  
   `cd "Implementação 7"`  
3. Instale a biblioteca PyGame:  
   `pip install pygame`  
4. Execute o jogo:  
   `python main.py`

🎮 Controles  
- Mover para cima: ↑ (Seta para cima)  
- Mover para baixo: ↓ (Seta para baixo)  
- Mover para esquerda: ← (Seta para esquerda)  
- Mover para direita: → (Seta para direita)

🛠️ Tecnologias  
- Linguagem: Python  
- Biblioteca: PyGame  
- Algoritmo de Geração: Recursive Backtracking

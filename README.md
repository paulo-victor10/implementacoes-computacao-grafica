# Implementações de Computação Gráfica para a N1

## Implementação 1 - OpenGL com GLUT

Este projeto apresenta experimentos visuais desenvolvidos em OpenGL com o auxílio da biblioteca GLUT, explorando conceitos fundamentais de computação gráfica, como gradientes de cor, formas geométricas básicas e transformações visuais.

🛠️ **Tecnologias**

- OpenGL (Core e Fixed Pipeline)
- GLUT (Gerenciamento de janelas e eventos)
- C/C++

---

## Implementação 3 — Interpolação de Cores #B

Geração de uma grade de cores interpoladas a partir de **4 cores iniciais (A, B, C, D)**.
O projeto permite comparar a interpolação nos espaços **RGB** e **HSL**, visualizando como as transições mudam entre os modelos de cor.

🛠️ **Tecnologias**

* 🖥️ **HTML** – estrutura da página
* 🎨 **CSS** – layout e estilo
* ⚙️ **JavaScript** – lógica de interpolação
* 🌈 **[Chroma.js](https://gka.github.io/chroma.js/)** – manipulação e interpolação de cores (lerp)

🚀 **Funcionalidades**

* Seleção de 4 cores iniciais
* Interpolação linear entre as cores (horizontal e vertical)
* Alternância entre **RGB** e **HSL**
* Exibição da grade final com o resultado

▶️ **Como usar**

1. Abra `index.html` no navegador
2. Escolha as cores A, B, C e D
3. Gere a interpolação
4. Compare os resultados RGB × HSL

---

## Implementação 4 - Gráficos 2D com PyCairo

Este projeto implementa a criação de gráficos vetoriais 2D utilizando a biblioteca **PyCairo**, os *bindings* em Python para a poderosa biblioteca gráfica Cairo. O foco é explorar a manipulação de formas básicas, cores e aplicação de transformações com o uso de *looping* e estados de contexto. A atividade foi dividida em duas partes principais:

#### (a) Design da Carranca Geométrica e Transformações

Criação de uma figura abstrata ("Carranca Geométrica") composta unicamente por formas primitivas (retângulo, círculos, triângulos e semicírculo). O principal desafio técnico foi a implementação de uma função de desenho de seta (`draw_arrow`) que aceita rotação.

💡 **Conceitos Chave**

* **Transformações:** Utilização de `cr.translate()` e `cr.rotate()` dentro da função `draw_arrow` para posicionar e orientar a seta (nariz) em qualquer ângulo.
* **Isolamento de Estado:** Uso de `cr.save()` e `cr.restore()` para garantir que as transformações aplicadas à seta não afetem a posição e orientação dos demais elementos do desenho (corpo, olhos, boca).
* **Caminhos Complexos:** Criação da boca utilizando `cr.arc()` e `cr.close_path()` para formar um semicírculo preenchido.

Ps.: Foi escolhida a figura de uma Carranca como elemento criativo para a execução da atividade, preservando as formas sugeridas nas instruções, mas adicionando novas formas, cores, coordenadas e tamanhos.

#### (b) Prática de Formas e Geração com *Looping*

Implementação de padrões geométricos através de estruturas de repetição (`for`), demonstrando como a geometria, posição e cor podem ser variadas de forma algorítmica.

🛠️ **Tecnologias**

- **Python**
- **PyCairo** (Bindings Python para a biblioteca Cairo)

---

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

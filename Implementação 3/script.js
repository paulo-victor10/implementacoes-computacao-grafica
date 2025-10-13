// Faz o layout da grid (n x n) usando CSS Grid e cria as divs
function buildGrid(n, container) {
  // limpa
  container.innerHTML = '';
  // configura o grid
  container.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
  container.style.gridTemplateRows = `repeat(${n}, 1fr)`;
  // cria n*n células
  const total = n * n;
  for (let i = 0; i < total; i++) {
    const cell = document.createElement('div');
    cell.className = 'grid-cell';
    container.appendChild(cell);
  }
}

// Faz a interpolação bilinear usando chroma.mix
function fillGrid(A, B, C, D, n, mode, container) {
  // container's children are the grid cells in row-major order
  const cells = Array.from(container.children);
  for (let row = 0; row < n; row++) {
    const tY = (n === 1) ? 0 : row / (n - 1);
    // ponto à esquerda (entre A e C) e à direita (entre B e D)
    const left = chroma.mix(A, C, tY, mode);
    const right = chroma.mix(B, D, tY, mode);

    for (let col = 0; col < n; col++) {
      const tX = (n === 1) ? 0 : col / (n - 1);
      const idx = row * n + col;
      const mixed = chroma.mix(left, right, tX, mode);
      // seta o background como string css
      cells[idx].style.background = mixed.css();
    }
  }
}

// Função principal chamada ao clicar
function generate() {
  const A = document.getElementById('colorA').value;
  const B = document.getElementById('colorB').value;
  const C = document.getElementById('colorC').value;
  const D = document.getElementById('colorD').value;
  const mode = document.getElementById('mode').value; // 'rgb' ou 'hsl'
  let n = parseInt(document.getElementById('n').value, 10);
  if (!n || n < 1) n = 8;

  const container = document.getElementById('gridContainer');

  // Ajusta o tamanho da grid (em pixels) se quiser fixo
  // container.style.width/height já no index.html, mas pode ajustar aqui.

  buildGrid(n, container);
  fillGrid(A, B, C, D, n, mode, container);
}

// Garante que elementos existam
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('generate').addEventListener('click', generate);
  // desenha inicialmente
  generate();
});

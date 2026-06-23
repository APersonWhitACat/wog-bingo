import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Wings of Glory Bingo",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
header[data-testid="stHeader"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
.stApp {
    background: #06070b;
}
</style>
""",
    unsafe_allow_html=True,
)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<style>
:root {
  --bg: #06070b;
  --bg2: #0b0f18;
  --cell: #141a25;
  --cell2: #171f2d;
  --line: #303846;
  --line2: #596171;
  --gold: #e5b85a;
  --gold2: #c58e2b;
  --text: #edf1f7;
  --muted: #9aa4b4;
  --green: #136b45;
  --green2: #21b873;
  --purple: #38285b;
  --red: #d94e65;
  --blue: #56b7d8;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  background:
    radial-gradient(circle at 50% 0%, rgba(229,184,90,.12), transparent 22%),
    radial-gradient(circle at 8% 35%, rgba(86,183,216,.06), transparent 18%),
    radial-gradient(circle at 92% 35%, rgba(217,78,101,.05), transparent 18%),
    linear-gradient(180deg, #080a10 0%, #05060a 100%);
  color: var(--text);
  font-family: Inter, "Segoe UI", Arial, sans-serif;
  overflow-x: hidden;
}

.app {
  width: min(94vw, 650px);
  margin: 0 auto;
  padding: 10px 8px 26px;
  position: relative;
}

.header {
  position: relative;
  text-align: center;
  padding: 6px 8px 4px;
  margin-bottom: 4px;
}

.title {
  font-weight: 900;
  letter-spacing: -0.045em;
  line-height: .96;
  font-size: clamp(34px, 6.7vw, 56px);
  color: var(--gold);
  text-shadow: 0 0 14px rgba(229,184,90,.25);
  animation: titleGlow 4.5s ease-in-out infinite;
}

.title small {
  display: block;
  font-size: .62em;
  margin-top: .08em;
}

@keyframes titleGlow {
  0%,100% { filter: brightness(.95); transform: translateY(0); }
  50% { filter: brightness(1.13); transform: translateY(-1px); }
}

.toolbar {
  width: fit-content;
  max-width: 100%;
  margin: 5px auto 10px;
  padding: 5px;
  background: rgba(13, 17, 26, .9);
  border: 1px solid rgba(255,255,255,.08);
  display: flex;
  gap: 5px;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 22px rgba(0,0,0,.25);
}

.icon-btn {
  width: 34px;
  height: 34px;
  border: 1px solid rgba(229,184,90,.35);
  background: #14100a;
  color: var(--gold);
  font-size: 17px;
  font-weight: 900;
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: transform .14s ease, box-shadow .14s ease, border-color .14s ease, filter .14s ease;
}

.icon-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 14px rgba(229,184,90,.2);
  border-color: var(--gold);
  filter: brightness(1.12);
}

.icon-btn:active { transform: scale(.96); }

.board-select {
  height: 34px;
  border: 1px solid rgba(229,184,90,.35);
  background: #101722;
  color: var(--gold);
  font-weight: 800;
  outline: none;
  padding: 0 6px;
  cursor: pointer;
}

.stage {
  position: relative;
  width: 100%;
  min-height: 10px;
}

.floaty {
  position: fixed;
  pointer-events: none;
  color: rgba(229,184,90,.45);
  font-size: 16px;
  animation: floaty 5.5s ease-in-out infinite alternate;
  z-index: 0;
}

.floaty.f1 { left: 8vw; top: 22vh; animation-delay: 0s; }
.floaty.f2 { right: 10vw; top: 28vh; animation-delay: .8s; color: rgba(86,183,216,.35); }
.floaty.f3 { left: 12vw; bottom: 18vh; animation-delay: 1.3s; color: rgba(217,78,101,.28); }
.floaty.f4 { right: 14vw; bottom: 22vh; animation-delay: 2s; }

@keyframes floaty {
  from { transform: translateY(0) rotate(-8deg); opacity: .25; }
  to { transform: translateY(-18px) rotate(8deg); opacity: .8; }
}

.boards {
  display: grid;
  gap: 12px;
  justify-content: center;
  position: relative;
  z-index: 2;
}

.boards.one {
  grid-template-columns: minmax(300px, min(80vmin, 520px));
}

.boards.two,
.boards.three,
.boards.four {
  grid-template-columns: repeat(2, minmax(270px, 1fr));
  width: min(94vw, 850px);
  margin-left: 50%;
  transform: translateX(-50%);
}

.boards.five,
.boards.six {
  grid-template-columns: repeat(3, minmax(230px, 1fr));
  width: min(96vw, 980px);
  margin-left: 50%;
  transform: translateX(-50%);
}

.board-shell {
  padding: 3px;
  background: #1b2029;
  border: 2px solid var(--line2);
  box-shadow: 0 0 18px rgba(0,0,0,.35), 0 0 20px rgba(229,184,90,.07);
  animation: boardIn .25s ease both;
}

@keyframes boardIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.board {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2px;
  background: var(--line);
  padding: 2px;
  aspect-ratio: 1 / 1;
}

.cell {
  position: relative;
  overflow: hidden;
  border: 1px solid #2f3848;
  background: var(--cell);
  color: var(--text);
  font-size: clamp(9px, 1.55vw, 13px);
  line-height: 1.08;
  font-weight: 850;
  text-align: center;
  padding: 5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  transition: transform .13s ease, filter .13s ease, border-color .13s ease, box-shadow .13s ease, background .13s ease;
}

.cell:nth-child(even) { background: var(--cell2); }

.boards.two .cell,
.boards.three .cell,
.boards.four .cell { font-size: clamp(8px, 1vw, 11px); }

.boards.five .cell,
.boards.six .cell { font-size: clamp(7px, .75vw, 9px); }

.cell:hover {
  transform: translateY(-1px);
  border-color: rgba(229,184,90,.7);
  box-shadow: 0 0 10px rgba(229,184,90,.12);
  filter: brightness(1.08);
}

.cell.free {
  background: var(--purple);
  color: var(--gold);
  border-color: rgba(229,184,90,.65);
  font-style: italic;
  font-size: clamp(12px, 1.8vw, 17px);
}

.cell.marked {
  background: linear-gradient(180deg, var(--green2), var(--green));
  color: #edfff5;
  border-color: rgba(46,232,142,.78);
  box-shadow: inset 0 0 14px rgba(255,255,255,.08), 0 0 12px rgba(46,232,142,.18);
  animation: markPop .2s ease;
}

.cell.marked::after {
  content: "✓";
  position: absolute;
  right: 5px;
  bottom: 0px;
  font-size: 16px;
  opacity: .35;
}

@keyframes markPop {
  0% { transform: scale(.97); }
  70% { transform: scale(1.035); }
  100% { transform: scale(1); }
}

.cell.rolling:not(.free) {
  animation: softRoll .28s ease;
}

@keyframes softRoll {
  0% { filter: brightness(.7); transform: translateY(3px); }
  70% { filter: brightness(1.25); transform: translateY(-2px); }
  100% { filter: brightness(1); transform: translateY(0); }
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.68);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 50;
  padding: 20px;
}

.modal-backdrop.show {
  display: flex;
  animation: fadeIn .16s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal {
  width: min(92vw, 390px);
  background: #101722;
  border: 1px solid rgba(229,184,90,.25);
  padding: 18px;
  box-shadow: 0 0 36px rgba(0,0,0,.55);
  animation: modalIn .2s ease;
}

@keyframes modalIn {
  from { transform: translateY(8px) scale(.98); opacity: 0; }
  to { transform: translateY(0) scale(1); opacity: 1; }
}

.modal h2 {
  margin: 0 0 10px;
  color: var(--gold);
  font-size: 30px;
  line-height: 1;
}

.modal p {
  color: var(--text);
  margin: 8px 0;
  font-weight: 720;
}

.close {
  margin-top: 14px;
  width: 100%;
  height: 36px;
  border: 1px solid rgba(229,184,90,.35);
  background: #14100a;
  color: var(--gold);
  font-weight: 900;
  cursor: pointer;
}

.bingo-modal .modal { text-align: center; }

.bingo-modal h2 {
  font-size: clamp(52px, 10vw, 86px);
  animation: jackpot .72s ease-in-out infinite alternate;
  text-shadow: 0 0 16px var(--gold), 0 0 32px var(--red);
}

@keyframes jackpot {
  from { transform: scale(1); filter: brightness(1); }
  to { transform: scale(1.055); filter: brightness(1.28); }
}

.confetti {
  position: fixed;
  top: -20px;
  font-size: 18px;
  z-index: 60;
  animation: fall 1.25s linear forwards;
}

@keyframes fall {
  to { transform: translateY(110vh) rotate(380deg); opacity: .2; }
}

@media (max-width: 760px) {
  .boards.two,
  .boards.three,
  .boards.four,
  .boards.five,
  .boards.six {
    grid-template-columns: 1fr;
    width: min(94vw, 520px);
  }
  .cell,
  .boards.two .cell,
  .boards.three .cell,
  .boards.four .cell,
  .boards.five .cell,
  .boards.six .cell {
    font-size: clamp(9px, 2.35vw, 12px);
  }
}
</style>
</head>
<body>
  <div class="floaty f1">✦</div>
  <div class="floaty f2">♦</div>
  <div class="floaty f3">●</div>
  <div class="floaty f4">✧</div>

  <div class="app">
    <div class="header">
      <div class="title">Wings of Glory<small>Low Rank Bingo</small></div>
    </div>

    <div class="toolbar">
      <button class="icon-btn" title="Roll" onclick="rollBoards()">🎲</button>
      <button class="icon-btn" title="Reset" onclick="resetMarks()">↺</button>
      <button class="icon-btn" title="Rules" onclick="openRules()">?</button>
      <select class="board-select" id="boardCount" title="Boards" onchange="setBoardCount(this.value)">
        <option value="1">1 board</option>
        <option value="2">2 boards</option>
        <option value="3">3 boards</option>
        <option value="4">4 boards</option>
        <option value="5">5 boards</option>
        <option value="6">6 boards</option>
      </select>
    </div>

    <div class="stage">
      <div id="boards" class="boards one"></div>
    </div>
  </div>

  <div id="rulesModal" class="modal-backdrop" onclick="closeRules(event)">
    <div class="modal">
      <h2>Rules</h2>
      <p>• Click a square when it happens.</p>
      <p>• Free space starts marked.</p>
      <p>• 5 in a row wins.</p>
      <p>• Rows, columns, diagonals count.</p>
      <button class="close" onclick="hideRules()">Close</button>
    </div>
  </div>

  <div id="bingoModal" class="modal-backdrop bingo-modal" onclick="hideBingo()">
    <div class="modal">
      <h2>BINGO!</h2>
      <p>jackpot hit</p>
      <button class="close" onclick="hideBingo()">Close</button>
    </div>
  </div>

<script>
const ITEMS = [
  '"add 5th gen aircrafts!"',
  'DOGSHIT opinion or suggestion',
  'corny ass profile/pfp',
  '"errrmm is all bvr so it\\'s LAME"',
  'chaff = flare',
  'thinks they\\'re good',
  'nerf f14a or phoenix missiles',
  'compares wog to wt',
  "doesn't know any bfm/acm",
  '"codes?"',
  'add their favorite niche aircraft',
  '"i have a life/whats wrong with low rank"',
  'realized they have no image perms',
  '"My rank ingame is higher"',
  'extremely biased',
  'intentional rule breaking',
  '"when update?" bro the update is soon chilllll',
  'bitching about killstealing',
  '"(decent plane) is so bad"',
  '"(premium plane) is p2w..."',
  '"add (insert nation) tree!"',
  "can't lose their argument",
  'rants about russian aircrafts',
  'huge fuckass ego'
];

let boards = [];
let marked = [];
let boardCount = 1;
let rolling = false;

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function makeBoard() {
  const items = shuffle(ITEMS);
  const board = [];
  let idx = 0;
  for (let i = 0; i < 25; i++) {
    if (i === 12) board.push("FREE SPACE");
    else board.push(items[idx++]);
  }
  return board;
}

function setBoardCount(n) {
  boardCount = Math.max(1, Math.min(6, Number(n)));
  while (boards.length < boardCount) {
    boards.push(makeBoard());
    marked.push(new Set([12]));
  }
  while (boards.length > boardCount) {
    boards.pop();
    marked.pop();
  }
  render();
}

function classForCount() {
  if (boardCount === 1) return "one";
  if (boardCount === 2) return "two";
  if (boardCount === 3) return "three";
  if (boardCount === 4) return "four";
  if (boardCount === 5) return "five";
  return "six";
}

function render() {
  const root = document.getElementById("boards");
  root.className = "boards " + classForCount();
  root.innerHTML = "";

  for (let b = 0; b < boardCount; b++) {
    const shell = document.createElement("div");
    shell.className = "board-shell";

    const board = document.createElement("div");
    board.className = "board";

    for (let i = 0; i < 25; i++) {
      const cell = document.createElement("div");
      cell.className = "cell";
      if (i === 12) cell.classList.add("free");
      if (marked[b].has(i)) cell.classList.add("marked");
      cell.textContent = boards[b][i];
      cell.onclick = () => toggleCell(b, i);
      board.appendChild(cell);
    }

    shell.appendChild(board);
    root.appendChild(shell);
  }
}

function toggleCell(b, i) {
  if (i === 12 || rolling) return;

  if (marked[b].has(i)) marked[b].delete(i);
  else marked[b].add(i);

  render();

  if (hasBingo(marked[b])) {
    showBingo();
  }
}

function winLines() {
  const lines = [];
  for (let r = 0; r < 5; r++) lines.push([0,1,2,3,4].map(c => r * 5 + c));
  for (let c = 0; c < 5; c++) lines.push([0,1,2,3,4].map(r => r * 5 + c));
  lines.push([0,6,12,18,24]);
  lines.push([4,8,12,16,20]);
  return lines;
}

function hasBingo(set) {
  return winLines().some(line => line.every(i => set.has(i)));
}

function rollBoards() {
  if (rolling) return;
  rolling = true;

  const allCells = () => Array.from(document.querySelectorAll(".cell:not(.free)"));
  let steps = 10;

  function spin(step) {
    const tempBoards = Array.from({length: boardCount}, () => makeBoard());
    const cells = allCells();

    cells.forEach((cell, idx) => {
      const boardIndex = Math.floor(idx / 24);
      const innerIndex = idx % 24;
      const board = tempBoards[boardIndex] || tempBoards[0];
      const text = board.filter((_, i) => i !== 12)[innerIndex] || ITEMS[Math.floor(Math.random() * ITEMS.length)];
      cell.textContent = text;
      cell.classList.add("rolling");
    });

    if (step < steps) {
      setTimeout(() => spin(step + 1), 55 + step * 10);
    } else {
      boards = Array.from({length: boardCount}, () => makeBoard());
      marked = Array.from({length: boardCount}, () => new Set([12]));
      rolling = false;
      render();
    }
  }

  spin(0);
}

function resetMarks() {
  marked = Array.from({length: boardCount}, () => new Set([12]));
  render();
}

function openRules() {
  document.getElementById("rulesModal").classList.add("show");
}

function hideRules() {
  document.getElementById("rulesModal").classList.remove("show");
}

function closeRules(e) {
  if (e.target.id === "rulesModal") hideRules();
}

function showBingo() {
  document.getElementById("bingoModal").classList.add("show");
  confettiBurst();
}

function hideBingo() {
  document.getElementById("bingoModal").classList.remove("show");
}

function confettiBurst() {
  const shapes = ["✦", "★", "♦", "●", "♠", "♥"];
  const colors = ["#ffd166", "#ef476f", "#06d6a0", "#4cc9f0", "#b517ff", "#ffffff"];

  for (let i = 0; i < 30; i++) {
    const s = document.createElement("div");
    s.className = "confetti";
    s.textContent = shapes[Math.floor(Math.random() * shapes.length)];
    s.style.left = Math.random() * 100 + "vw";
    s.style.color = colors[Math.floor(Math.random() * colors.length)];
    s.style.animationDelay = Math.random() * .15 + "s";
    document.body.appendChild(s);
    setTimeout(() => s.remove(), 1500);
  }
}

document.addEventListener("keydown", e => {
  if (e.key === "Escape") {
    hideRules();
    hideBingo();
  }
});

boards = [makeBoard()];
marked = [new Set([12])];
render();
</script>
</body>
</html>
"""

components.html(html, height=980, scrolling=True)

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
    background: #080a10;
}
</style>
""",
    unsafe_allow_html=True,
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<style>
:root {
  --bg: #080a10;
  --cell: #171f31;
  --cell2: #1b263b;
  --gold: #f6c95f;
  --gold2: #ffb703;
  --text: #f3f6fb;
  --muted: #9da8ba;
  --green: #17915b;
  --green2: #20c979;
  --purple: #57358b;
  --red: #ef476f;
  --blue: #4cc9f0;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  background: radial-gradient(circle at top, rgba(246,201,95,.14), transparent 28%),
              radial-gradient(circle at 18% 25%, rgba(76,201,240,.08), transparent 22%),
              radial-gradient(circle at 85% 18%, rgba(181,23,255,.08), transparent 20%),
              var(--bg);
  color: var(--text);
  font-family: Inter, "Segoe UI", Arial, sans-serif;
  overflow-x: hidden;
}

.app {
  width: min(96vw, 720px);
  margin: 0 auto;
  padding: 16px 10px 28px;
}

.header {
  position: relative;
  text-align: center;
  padding: 12px 8px 8px;
  margin-bottom: 8px;
}

.title {
  font-weight: 950;
  letter-spacing: -0.04em;
  line-height: 0.94;
  font-size: clamp(38px, 8vw, 70px);
  color: var(--gold);
  text-shadow: 0 0 20px rgba(246,201,95,.28);
  transform-origin: center;
  animation: titleGlow 4s ease-in-out infinite;
}

.title small {
  display: block;
  font-size: .64em;
  letter-spacing: -0.03em;
  margin-top: .08em;
}

@keyframes titleGlow {
  0%,100% { filter: brightness(1); transform: translateY(0); }
  50% { filter: brightness(1.14); transform: translateY(-1px); }
}

.spark {
  position: absolute;
  color: var(--gold);
  opacity: .85;
  font-size: 20px;
  animation: float 2.2s ease-in-out infinite alternate;
}

.spark.left { left: 10%; top: 32px; }
.spark.right { right: 10%; top: 32px; animation-delay: .4s; }

@keyframes float {
  from { transform: translateY(0) rotate(-4deg); opacity: .65; }
  to { transform: translateY(-7px) rotate(4deg); opacity: 1; }
}

.toolbar {
  width: fit-content;
  max-width: 100%;
  margin: 0 auto 12px;
  padding: 7px;
  background: rgba(17, 23, 36, .92);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 999px;
  display: flex;
  gap: 6px;
  align-items: center;
  justify-content: center;
  box-shadow: 0 12px 30px rgba(0,0,0,.25);
}

.icon-btn {
  width: 38px;
  height: 38px;
  border-radius: 999px;
  border: 1px solid rgba(246,201,95,.28);
  background: linear-gradient(180deg, #2b210f, #17120a);
  color: var(--gold);
  font-size: 18px;
  font-weight: 900;
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease, filter .15s ease;
}

.icon-btn:hover {
  transform: translateY(-2px) scale(1.04);
  box-shadow: 0 0 18px rgba(246,201,95,.24);
  border-color: var(--gold);
  filter: brightness(1.12);
}

.icon-btn:active { transform: translateY(0) scale(.96); }

.board-select {
  height: 38px;
  border-radius: 999px;
  border: 1px solid rgba(246,201,95,.28);
  background: #111724;
  color: var(--gold);
  font-weight: 900;
  outline: none;
  padding: 0 8px;
  cursor: pointer;
}

.boards {
  display: grid;
  gap: 14px;
  justify-content: center;
}

.boards.one {
  grid-template-columns: minmax(310px, 570px);
}

.boards.two,
.boards.three,
.boards.four {
  grid-template-columns: repeat(2, minmax(280px, 1fr));
  width: min(96vw, 980px);
  margin-left: 50%;
  transform: translateX(-50%);
}

.boards.five,
.boards.six {
  grid-template-columns: repeat(3, minmax(250px, 1fr));
  width: min(98vw, 1160px);
  margin-left: 50%;
  transform: translateX(-50%);
}

.board-shell {
  padding: 5px;
  border-radius: 18px;
  background: linear-gradient(135deg, #ffb703, #f6c95f 36%, #815600);
  box-shadow: 0 0 28px rgba(255,183,3,.22);
  animation: boardIn .35s ease both;
}

@keyframes boardIn {
  from { opacity: 0; transform: translateY(8px) scale(.985); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.board {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 3px;
  background: #21190b;
  border-radius: 14px;
  padding: 5px;
  aspect-ratio: 1 / 1;
}

.cell {
  position: relative;
  overflow: hidden;
  border: 1px solid #34425a;
  border-radius: 10px;
  background: linear-gradient(180deg, var(--cell2), var(--cell));
  color: var(--text);
  font-size: clamp(9px, 1.75vw, 14px);
  line-height: 1.08;
  font-weight: 900;
  text-align: center;
  padding: 5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  transition: transform .16s ease, filter .16s ease, border-color .16s ease, box-shadow .16s ease, background .16s ease;
}

.boards.two .cell,
.boards.three .cell,
.boards.four .cell { font-size: clamp(8px, 1.1vw, 12px); }

.boards.five .cell,
.boards.six .cell { font-size: clamp(7px, .85vw, 10px); }

.cell:hover {
  transform: translateY(-2px);
  border-color: rgba(246,201,95,.85);
  box-shadow: 0 0 16px rgba(246,201,95,.15);
  filter: brightness(1.08);
}

.cell.free {
  background: linear-gradient(180deg, #6b3fb0, var(--purple));
  color: var(--gold);
  border-color: rgba(246,201,95,.8);
  font-style: italic;
  font-size: clamp(12px, 2vw, 18px);
}

.cell.marked {
  background: linear-gradient(180deg, var(--green2), var(--green));
  color: #ecfff4;
  border-color: rgba(46,232,142,.85);
  box-shadow: inset 0 0 18px rgba(255,255,255,.08), 0 0 12px rgba(46,232,142,.22);
  animation: markPop .22s ease;
}

.cell.marked::after {
  content: "✓";
  position: absolute;
  right: 6px;
  bottom: 2px;
  font-size: 18px;
  opacity: .42;
}

@keyframes markPop {
  0% { transform: scale(.96); }
  70% { transform: scale(1.045); }
  100% { transform: scale(1); }
}

.rolling .cell:not(.free) { animation: slot .52s ease-in-out infinite; }

@keyframes slot {
  0% { filter: brightness(.8); transform: translateY(0); }
  50% { filter: brightness(1.35); transform: translateY(-2px); }
  100% { filter: brightness(.85); transform: translateY(0); }
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.72);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 50;
  padding: 20px;
}

.modal-backdrop.show {
  display: flex;
  animation: fadeIn .18s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal {
  width: min(92vw, 420px);
  background: linear-gradient(180deg, #161e2d, #0e1420);
  border: 1px solid rgba(246,201,95,.28);
  border-radius: 22px;
  padding: 20px;
  box-shadow: 0 0 40px rgba(0,0,0,.55), 0 0 28px rgba(246,201,95,.12);
  animation: modalIn .22s ease;
}

@keyframes modalIn {
  from { transform: translateY(10px) scale(.97); opacity: 0; }
  to { transform: translateY(0) scale(1); opacity: 1; }
}

.modal h2 {
  margin: 0 0 10px;
  color: var(--gold);
  font-size: 32px;
  line-height: 1;
}

.modal p {
  color: var(--text);
  margin: 8px 0;
  font-weight: 750;
}

.close {
  margin-top: 14px;
  width: 100%;
  height: 38px;
  border-radius: 12px;
  border: 1px solid rgba(246,201,95,.28);
  background: #251a08;
  color: var(--gold);
  font-weight: 900;
  cursor: pointer;
}

.bingo-modal .modal { text-align: center; }

.bingo-modal h2 {
  font-size: clamp(54px, 12vw, 92px);
  animation: jackpot .75s ease-in-out infinite alternate;
  text-shadow: 0 0 18px var(--gold), 0 0 36px var(--red);
}

@keyframes jackpot {
  from { transform: scale(1); filter: brightness(1); }
  to { transform: scale(1.06); filter: brightness(1.35); }
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
    width: min(96vw, 570px);
  }
  .cell,
  .boards.two .cell,
  .boards.three .cell,
  .boards.four .cell,
  .boards.five .cell,
  .boards.six .cell {
    font-size: clamp(9px, 2.5vw, 13px);
  }
}
</style>
</head>
<body>
  <div class="app">
    <div class="header">
      <div class="spark left">✦</div>
      <div class="spark right">✦</div>
      <div class="title">Wings of Glory<small>Low Rank Bingo</small></div>
    </div>

    <div class="toolbar">
      <button class="icon-btn" title="Roll" onclick="rollBoards(true)">🎲</button>
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

    <div id="boards" class="boards one"></div>
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

function rollBoards(animated) {
  if (rolling) return;
  rolling = true;

  if (!animated) {
    boards = Array.from({length: boardCount}, () => makeBoard());
    marked = Array.from({length: boardCount}, () => new Set([12]));
    rolling = false;
    render();
    return;
  }

  const root = document.getElementById("boards");
  let steps = 16;

  function spin(step) {
    boards = Array.from({length: boardCount}, () => makeBoard());
    marked = Array.from({length: boardCount}, () => new Set([12]));
    render();
    root.classList.add("rolling");

    if (step < steps) {
      setTimeout(() => spin(step + 1), 35 + step * 7);
    } else {
      boards = Array.from({length: boardCount}, () => makeBoard());
      marked = Array.from({length: boardCount}, () => new Set([12]));
      rolling = false;
      render();
      root.classList.remove("rolling");
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
  const modal = document.getElementById("bingoModal");
  modal.classList.add("show");
  confettiBurst();
}

function hideBingo() {
  document.getElementById("bingoModal").classList.remove("show");
}

function confettiBurst() {
  const shapes = ["✦", "★", "♦", "●", "♠", "♥"];
  const colors = ["#ffd166", "#ef476f", "#06d6a0", "#4cc9f0", "#b517ff", "#ffffff"];

  for (let i = 0; i < 36; i++) {
    const s = document.createElement("div");
    s.className = "confetti";
    s.textContent = shapes[Math.floor(Math.random() * shapes.length)];
    s.style.left = Math.random() * 100 + "vw";
    s.style.color = colors[Math.floor(Math.random() * colors.length)];
    s.style.animationDelay = Math.random() * .18 + "s";
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

components.html(html, height=1150, scrolling=True)

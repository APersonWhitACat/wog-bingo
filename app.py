import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Wings of Glory Bingo",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
header[data-testid="stHeader"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #070910; }
iframe { display: block; margin: 0 auto; }
</style>
""", unsafe_allow_html=True)

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
:root{
  --bg:#070910;
  --cell:#172033;
  --cell2:#1b2740;
  --grid:#4a3510;
  --gold:#ffd166;
  --gold2:#ffb703;
  --purple:#b517ff;
  --free:#5b3a93;
  --green1:#258f55;
  --green2:#39b875;
  --text:#f8fafc;
  --muted:#aeb8c8;
}
*{box-sizing:border-box}
html,body{
  margin:0;
  background:var(--bg);
  color:var(--text);
  font-family:"Segoe UI",Arial,sans-serif;
  overflow:hidden;
}
.app{
  width:535px;
  max-width:100vw;
  height:620px;
  max-height:100vh;
  margin:0 auto;
  padding:7px 8px 5px;
  background:var(--bg);
  display:flex;
  flex-direction:column;
}
.header{
  text-align:center;
  flex:0 0 auto;
}
.icon-row{
  height:26px;
  width:100%;
  position:relative;
}
.icon-box{
  position:absolute;
  top:2px;
  width:25px;
  height:25px;
  display:grid;
  place-items:center;
  border:1px solid rgba(255,209,102,.55);
  color:var(--gold);
  background:#101522;
  font-size:15px;
  box-shadow:0 0 7px rgba(255,209,102,.25);
}
.icon-box.left{left:110px}
.icon-box.right{
  right:110px;
  color:#a93cff;
  border-color:rgba(169,60,255,.65);
  box-shadow:0 0 8px rgba(169,60,255,.32);
}
.title{
  color:var(--gold);
  font-size:25px;
  line-height:1;
  font-weight:800;
  text-shadow:0 0 8px rgba(255,209,102,.35);
}
.subtitle{
  margin-top:4px;
  color:#c5d0de;
  font-size:15px;
  font-weight:800;
  letter-spacing:.07em;
  text-transform:uppercase;
  text-shadow:0 0 4px rgba(197,208,222,.22);
}
.controls{
  display:flex;
  justify-content:center;
  align-items:center;
  gap:4px;
  margin:9px auto 7px;
  flex:0 0 auto;
}
.btn{
  height:30px;
  min-width:58px;
  border:0;
  background:#251a08;
  color:var(--gold);
  font-family:"Segoe UI",Arial,sans-serif;
  font-size:12px;
  font-weight:700;
  padding:0 10px;
  cursor:pointer;
}
.btn:hover{background:#3a280b;color:#fff1bd}
.btn:active{filter:brightness(.85)}
.neon{
  height:4px;
  margin:0 24px 7px;
  background:var(--purple);
  box-shadow:0 0 8px rgba(181,23,255,.9);
  flex:0 0 auto;
}
.outer{
  background:var(--gold2);
  padding:3px;
  flex:1 1 auto;
  min-height:0;
  display:flex;
  box-shadow:0 0 9px rgba(255,183,3,.28);
}
.inner{
  background:#2b210e;
  padding:3px;
  flex:1 1 auto;
  min-height:0;
  display:flex;
}
.board{
  flex:1 1 auto;
  min-height:0;
  display:grid;
  grid-template-columns:repeat(5,1fr);
  grid-template-rows:repeat(5,1fr);
  gap:3px;
  background:var(--grid);
}
.cell{
  position:relative;
  background:var(--cell);
  color:var(--text);
  display:flex;
  align-items:center;
  justify-content:center;
  text-align:center;
  white-space:pre-line;
  padding:4px;
  font-size:11px;
  line-height:1.13;
  font-weight:800;
  overflow:hidden;
  cursor:pointer;
  user-select:none;
  transition:filter .10s ease, transform .10s ease, background .10s ease, color .10s ease;
}
.cell.alt{background:var(--cell2)}
.cell:hover:not(.free){filter:brightness(1.12)}
.cell.free{
  background:var(--free)!important;
  color:var(--gold);
  font-size:18px;
  font-style:italic;
  font-weight:800;
  cursor:default;
  text-shadow:0 0 5px rgba(255,209,102,.26);
}
.cell.marked{
  background:var(--green1)!important;
  color:#ecfff4;
}
.cell.marked.alt{
  background:var(--green2)!important;
}
.cell.pulse1{background:#40c985!important;color:#ecfff4}
.cell.pulse2{background:#22a86a!important;color:#ecfff4}
.cell.pop{animation:pop .20s ease}
@keyframes pop{
  0%{transform:scale(.96);filter:brightness(1.25)}
  70%{transform:scale(1.035);filter:brightness(1.12)}
  100%{transform:scale(1);filter:brightness(1)}
}
.cell.roll{animation:roll .18s ease}
@keyframes roll{
  0%{filter:brightness(.72)}
  70%{filter:brightness(1.26)}
  100%{filter:brightness(1)}
}
.overlay{
  position:fixed;
  inset:0;
  display:none;
  align-items:center;
  justify-content:center;
  background:#000;
  z-index:40;
  text-align:center;
  overflow:hidden;
}
.overlay.show{display:flex}
.bingo-main{
  position:relative;
  z-index:3;
  color:var(--gold);
  font-size:56px;
  font-weight:900;
  line-height:1;
  text-shadow:0 0 12px rgba(255,209,102,.9);
  animation:bingoPulse .55s ease-in-out infinite alternate;
}
@keyframes bingoPulse{
  from{transform:scale(.95);filter:brightness(1)}
  to{transform:scale(1.12);filter:brightness(1.25)}
}
.bingo-sub{
  position:relative;
  z-index:3;
  margin-top:10px;
  font-size:15px;
  font-weight:800;
  color:#ffffff;
}
.bingo-hint{
  position:relative;
  z-index:3;
  margin-top:16px;
  font-size:9px;
  color:var(--muted);
}
.star{
  position:fixed;
  z-index:2;
  pointer-events:none;
  font-weight:900;
  animation:star .55s ease forwards;
}
@keyframes star{
  from{opacity:1;transform:scale(.6) rotate(0deg)}
  to{opacity:0;transform:scale(1.7) rotate(100deg)}
}
.rules{
  position:fixed;
  inset:0;
  display:none;
  align-items:center;
  justify-content:center;
  background:rgba(0,0,0,.72);
  z-index:35;
}
.rules.show{display:flex}
.card{
  width:360px;
  max-width:92vw;
  background:#000;
  border:2px solid var(--gold2);
  padding:18px;
}
.card h2{
  margin:0 0 10px;
  color:var(--gold);
  font-size:30px;
}
.card p{
  margin:8px 0;
  font-size:14px;
  font-weight:700;
}
.card button{width:100%;margin-top:12px}
</style>
</head>
<body>
<div class="app">
  <div class="header">
    <div class="icon-row">
      <div class="icon-box left">▦</div>
      <div class="icon-box right">▣</div>
    </div>
    <div class="title">✦ Wings of Glory ✦</div>
    <div class="subtitle">Low Rank Bingo</div>
  </div>

  <div class="controls">
    <button class="btn" onclick="rollBoard()">Roll 👁</button>
    <button class="btn" onclick="resetMarks()">Reset</button>
    <button class="btn" onclick="showRules()">Bingo?</button>
    <button class="btn" onclick="toggleFull()">Full</button>
  </div>

  <div class="neon"></div>

  <div class="outer">
    <div class="inner">
      <div class="board" id="board"></div>
    </div>
  </div>
</div>

<div class="rules" id="rules" onclick="rulesBackdrop(event)">
  <div class="card">
    <h2>Rules</h2>
    <p>• Click a square when it happens</p>
    <p>• FREE SPACE is already marked</p>
    <p>• 5 in a row = BINGO</p>
    <p>• Rows, columns, diagonals count</p>
    <button class="btn" onclick="hideRules()">Close</button>
  </div>
</div>

<div class="overlay" id="bingoOverlay" onclick="hideBingo()">
  <div>
    <div class="bingo-main" id="bingoText">BINGO!</div>
    <div class="bingo-sub">JACKPOT HIT</div>
    <div class="bingo-hint">click anywhere or press Esc to close</div>
  </div>
</div>

<script>
const ITEMS = __ITEMS_JSON__;
const colors = ["#ffd166","#4cc9f0","#ef476f","#06d6a0","#ffffff"];
let board = [];
let marked = new Set([12]);
let rolling = false;

function shuffle(arr){
  const a=[...arr];
  for(let i=a.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    const t=a[i]; a[i]=a[j]; a[j]=t;
  }
  return a;
}
function makeBoard(){
  const list=shuffle(ITEMS);
  const b=[];
  let x=0;
  for(let i=0;i<25;i++){
    b.push(i===12 ? "FREE SPACE" : list[x++]);
  }
  return b;
}
function wrapText(text){
  if(text==="FREE SPACE") return "FREE\nSPACE";
  const max=13;
  const words=text.split(" ");
  const lines=[];
  let line="";
  for(let i=0;i<words.length;i++){
    const w=words[i];
    if(line==="") line=w;
    else if((line+" "+w).length<=max) line=line+" "+w;
    else{lines.push(line); line=w;}
  }
  if(line) lines.push(line);
  return lines.join("\n");
}
function render(){
  const root=document.getElementById("board");
  root.innerHTML="";
  for(let i=0;i<25;i++){
    const c=document.createElement("div");
    const row=Math.floor(i/5);
    const col=i%5;
    c.className="cell";
    if((row+col)%2===1)c.classList.add("alt");
    if(i===12)c.classList.add("free");
    if(marked.has(i))c.classList.add("marked");
    c.dataset.i=i;
    c.textContent=wrapText(board[i]);
    c.onclick=function(){toggleCell(i);};
    root.appendChild(c);
  }
}
function cellAt(i){
  return document.querySelector('.cell[data-i="'+i+'"]');
}
function setNewBoard(){
  board=makeBoard();
  marked=new Set([12]);
  render();
}
function toggleCell(i){
  if(i===12 || rolling)return;
  const c=cellAt(i);
  if(marked.has(i)){
    marked.delete(i);
    c.classList.remove("marked","pulse1","pulse2","pop");
    const row=Math.floor(i/5);
    const col=i%5;
    c.className="cell";
    if((row+col)%2===1)c.classList.add("alt");
  }else{
    marked.add(i);
    pulseCell(c,0);
  }
  if(hasBingo())showBingo();
}
function pulseCell(c,step){
  c.classList.remove("marked","pulse1","pulse2","pop");
  void c.offsetWidth;
  if(step===0)c.classList.add("pulse1");
  if(step===1)c.classList.add("pulse2");
  if(step===2)c.classList.add("marked");
  c.classList.add("pop");
  if(step<2)setTimeout(function(){pulseCell(c,step+1);},70);
}
function rollBoard(){
  if(rolling)return;
  rolling=true;
  const finalB=makeBoard();
  let step=0;
  function spin(){
    const temp=makeBoard();
    for(let i=0;i<25;i++){
      const c=cellAt(i);
      if(!c)continue;
      if(i===12){
        c.className="cell free";
        c.textContent="FREE\nSPACE";
      }else{
        c.textContent=wrapText(temp[i]);
        c.className="cell";
        const row=Math.floor(i/5);
        const col=i%5;
        if((row+col)%2===1)c.classList.add("alt");
        c.style.background=randomPick(["#172033","#1b2740","#2a1f3d","#263554"]);
        c.style.color=randomPick(["#f8fafc","#ffd166","#4cc9f0"]);
        c.classList.add("roll");
      }
    }
    if(step<13){
      step++;
      setTimeout(spin,30+step*6);
    }else{
      document.querySelectorAll(".cell").forEach(function(c){
        c.style.background="";
        c.style.color="";
      });
      board=finalB;
      marked=new Set([12]);
      rolling=false;
      render();
    }
  }
  spin();
}
function resetMarks(){
  marked=new Set([12]);
  render();
}
function winLines(){
  const lines=[];
  for(let r=0;r<5;r++)lines.push([0,1,2,3,4].map(function(c){return r*5+c;}));
  for(let c=0;c<5;c++)lines.push([0,1,2,3,4].map(function(r){return r*5+c;}));
  lines.push([0,6,12,18,24]);
  lines.push([4,8,12,16,20]);
  return lines;
}
function hasBingo(){
  return winLines().some(function(line){
    return line.every(function(i){return marked.has(i);});
  });
}
function showBingo(){
  document.getElementById("bingoOverlay").classList.add("show");
  bingoAnim(0);
}
function hideBingo(){
  document.getElementById("bingoOverlay").classList.remove("show");
}
function bingoAnim(step){
  const overlay=document.getElementById("bingoOverlay");
  if(!overlay.classList.contains("show"))return;
  const text=document.getElementById("bingoText");
  text.style.color=randomPick(colors);
  text.style.fontSize=randomPick(["50px","56px","62px","58px"]);
  for(let i=0;i<5;i++){
    const s=document.createElement("div");
    s.className="star";
    s.textContent=randomPick(["✦","✧","★","♦","●"]);
    s.style.left=(Math.random()*100)+"vw";
    s.style.top=(Math.random()*100)+"vh";
    s.style.fontSize=(10+Math.random()*12)+"px";
    s.style.color=randomPick(colors);
    document.body.appendChild(s);
    setTimeout(function(){s.remove();},560);
  }
  if(step<28)setTimeout(function(){bingoAnim(step+1);},90);
  else{
    text.style.color="#ffd166";
    text.style.fontSize="56px";
  }
}
function showRules(){document.getElementById("rules").classList.add("show");}
function hideRules(){document.getElementById("rules").classList.remove("show");}
function rulesBackdrop(e){if(e.target.id==="rules")hideRules();}
function randomPick(arr){return arr[Math.floor(Math.random()*arr.length)];}
function toggleFull(){
  try{
    if(document.fullscreenElement)document.exitFullscreen();
    else document.documentElement.requestFullscreen();
  }catch(e){}
}
document.addEventListener("keydown",function(e){
  if(e.key==="Escape"){hideBingo();hideRules();}
});
setNewBoard();
</script>
</body>
</html>
"""

html = html.replace("__ITEMS_JSON__", '["\\"add 5th gen aircrafts!\\"", "DOGSHIT opinion or suggestion", "corny ass profile/pfp", "\\"errrmm is all bvr so it\'s LAME\\"", "chaff = flare", "thinks they\'re good", "nerf f14a or phoenix missiles", "compares wog to wt", "doesn\'t know any bfm/acm", "\\"codes?\\"", "add their favorite niche aircraft", "\\"i have a life/whats wrong with low rank\\"", "realized they have no image perms", "\\"My rank ingame is higher\\"", "extremely biased", "intentional rule breaking", "\\"when update?\\" bro the update is soon chilllll", "bitching about killstealing", "\\"(decent plane) is so bad\\"", "\\"(premium plane) is p2w...\\"", "\\"add (insert nation) tree!\\"", "can\'t lose their argument", "rants about russian aircrafts", "huge fuckass ego"]')

components.html(html, height=620, scrolling=False)

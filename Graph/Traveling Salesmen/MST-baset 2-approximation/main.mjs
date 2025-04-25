import { MSTPrim } from "./MSTPrim.mjs";
import {drawEdge, drawVertice} from "./draw.mjs";

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const result = document.getElementById("result");

let verticesPos = [];

let G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]];


let mstTree = [];

const numVertices = G[0].length;

for (let i = 0; i < numVertices; i++) {
  verticesPos.push([getRandomArbitrary(20, 780), getRandomArbitrary(20, 780)]);
}

function getRandomArbitrary(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

drawGraph();


function drawGraph() {
  for (let i = 0; i < numVertices; i++) {
    for (let j = 0; j < numVertices; j++) {
      if (i !== j && G[i][j] !== 0){
        drawEdge(ctx, verticesPos[i][0], verticesPos[i][1], verticesPos[j][0], verticesPos[j][1], 1, "black");
        ctx.font = "20px serif";
        ctx.fillText(G[i][j], (verticesPos[i][0] + verticesPos[j][0]) / 2, (verticesPos[i][1] + verticesPos[j][1]) / 2);
      }
      drawVertice(ctx, verticesPos[i][0], verticesPos[i][1], "red", i);
    }
  }
}

document.getElementById("prim").onclick = async function () {
  let parent = await MSTPrim(ctx, G, verticesPos);
    
    mstTree = Array(numVertices).fill().map(() => []);
    console.log(mstTree);
    for (let v = 1; v < numVertices; v++) {
        let u = parent[v];
        mstTree[u].push(v);
        mstTree[v].push(u);
    }
};

document.getElementById("tsp").onclick = async function () {
    let visited = new Array(numVertices).fill(false);
    let path = [];
    
    function preorder(u) {
        visited[u] = true;
        path.push(u);
        for (let v of mstTree[u]) {
            if (!visited[v]) {
                preorder(v);
            }
        }
    }
    
    preorder(0);
    
    path.push(path[0]);
    
    let totalDistance = 0;
    for (let i = 0; i < path.length - 1; i++) {
        totalDistance += G[path[i]][path[i+1]];
    }
    
    result.innerHTML = `Ścieżka: ${path.join(" → ")}<br>Całkowita długość: ${totalDistance}`;
    
    ctx.strokeStyle = "blue";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(verticesPos[path[0]][0], verticesPos[path[0]][1]);
    for (let i = 1; i < path.length; i++) {
        ctx.lineTo(verticesPos[path[i]][0], verticesPos[path[i]][1]);
    }
    ctx.stroke();
};

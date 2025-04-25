
import {drawEdge, drawVertice} from "./draw.mjs";

export async function MSTPrim(ctx, G, verticesPos) {
    const numVertices = G[0].length;
    let selected = new Array(numVertices).fill(0);
    let parent = new Array(numVertices).fill(-1)
    let numOfEdges = 0;
    selected[0] = true;
    drawVertice(ctx, verticesPos[0][0], verticesPos[0][1], "green");
    while (numOfEdges < numVertices - 1) {
      let minimum = Infinity;
      let x = 0;
      let y = 0;
      for (let i = 0; i < numVertices; i++) {
        if (selected[i]) {
          for(let j = 0; j < numVertices; j++) {
            if (!selected[j] && G[i][j] !== 0) {
              if (minimum > G[i][j]) {
                minimum = G[i][j];
                x = i;
                y = j;
              }
            }
          }
        }
      }
      selected[y] = true;
      parent[y] = x;
      await new Promise(resolve => {
        setTimeout(() => {
          drawEdge(ctx, verticesPos[x][0], verticesPos[x][1], verticesPos[y][0], verticesPos[y][1], 4, "green");
          drawVertice(ctx, verticesPos[y][0], verticesPos[y][1], "green", typeof y === undefined ? 0 : y);
          resolve();
        }, 3000);
      });
    
      numOfEdges++; 
    }

    return parent;
  }
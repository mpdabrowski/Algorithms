export function drawEdge(context, x1, y1, x2, y2, lineWidth, color) {
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.lineWidth = lineWidth;
    context.strokeStyle = color;
    context.stroke();
  }
  
export function drawVertice(context, x, y, color, num) {
    context.beginPath();
    context.arc(x, y, 20, 0, 2 * Math.PI);
    context.fillStyle = color;
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = "black";
    context.fillStyle = "black";
    context.font = "25px serif";
    context.fillText(num, x, y);
    context.stroke();
  }
window.addEventListener('DOMContentLoaded', () => {
  const ctx = document.getElementById('tempChart').getContext('2d');

  const data = tempData;
  const maxTemp = Math.max(...data);

  const canvasWidth = ctx.canvas.width;
  const canvasHeight = ctx.canvas.height;
  const barWidth = canvasWidth / data.length;

  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  data.forEach((temp, index) => {
    const barHeight = (temp / maxTemp) * (canvasHeight - 20);
    ctx.fillStyle = '#007bff';
    ctx.fillRect(index * barWidth + 5, canvasHeight - barHeight - 10, barWidth - 10, barHeight);

    ctx.fillStyle = '#000';
    ctx.font = '14px Arial';
    ctx.fillText(temp + '°C', index * barWidth + 5, canvasHeight - barHeight - 15);
  });

  ctx.beginPath();
  ctx.moveTo(0, canvasHeight - 10);
  ctx.lineTo(canvasWidth, canvasHeight - 10);
  ctx.stroke();
});

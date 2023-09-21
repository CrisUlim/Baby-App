document.addEventListener('DOMContentLoaded', function () {
  const socket = io.connect('http://' + document.domain + ':' + location.port + '/temperature');

  socket.on('update_temperature', function (data) {
      updateChart(data.temperature, data.time);
  });

  const ctx = document.getElementById('temperatureChart').getContext('2d');
  const labels = [];
  const data = [];

  const chart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: labels,
          datasets: [{
              label: 'Temperature (°C)',
              borderColor: 'rgb(75, 192, 192)',
              borderWidth: 2,
              data: data,
          }]
      },
      options: {
          animation: false,
          scales: {
              x: {
                  type: 'time',
                  time: {
                      unit: 'second',
                      displayFormats: {
                          second: 'HH:mm:ss'
                      }
                  }
              },
              y: {
                  beginAtZero: true,
                  suggestedMin: 0,
                  suggestedMax: 40
              }
          }
      }
  });

  function updateChart(temperature, time) {
      if (labels.length >= 10) {
          labels.shift();
          data.shift();
      }
      labels.push(time);
      data.push(temperature);
      chart.update();
  }
});

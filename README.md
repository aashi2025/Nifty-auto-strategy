# Nifty-auto-strategy
<!DOCTYPE html>
<html>
<head>
  <title>Nifty Auto Strategy</title>
  <style>
    body { font-family: Arial; text-align: center; padding: 20px; background: #f0f0f0; }
    .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; }
    .alert { color: green; font-size: 20px; margin-top: 20px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Nifty Auto Strategy</h2>
    <p>Strategy: Trendline Breakout + WMA Bounce</p>
    <button onclick="generateAlert()">Check Signal</button>
    <div id="output" class="alert"></div>
  </div>

  <script>
    function generateAlert() {
      const price = 23853.75; // Sample value
      const wma = 23851.20;
      const breakoutLevel = 23840;
      const sl = 23790;
      const target = 23920;
      
      if (price > breakoutLevel && price > wma) {
        document.getElementById("output").innerText = 
          `Breakout Confirmed! Buy Nifty at ${price}, SL: ${sl}, Target: ${target}`;
      } else {
        document.getElementById("output").innerText = "No trade right now.";
      }
    }
  </script>
</body>
</html>

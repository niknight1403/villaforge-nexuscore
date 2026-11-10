const http = require('http');

async function runSmokeTest() {
  console.log('Starting NexusCore Smoke Test...');
  
  // Simulate API Gateway check
  const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', version: '1.0.0' }));
  });

  server.listen(3000, () => {
    console.log('Server running on port 3000');
    
    http.get('http://localhost:3000', (res) => {
      if (res.statusCode === 200) {
        console.log('Smoke Test Passed: API Gateway reachable.');
        process.exit(0);
      } else {
        console.error('Smoke Test Failed: API Gateway returned status', res.statusCode);
        process.exit(1);
      }
    }).on('error', (e) => {
      console.error('Smoke Test Failed: Connection error', e);
      process.exit(1);
    });
  });
}

runSmokeTest();
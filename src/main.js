const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', version: '1.0.0' }));
  } else {
    res.writeHead(404);
    res.end();
  }
});

if (process.argv.includes('--smoke-test')) {
  server.listen(3000, () => {
    console.log('Smoke test: Server running');
    process.exit(0);
  });
} else {
  server.listen(3000);
}
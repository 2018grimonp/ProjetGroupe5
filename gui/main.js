var http = require("http");
var fs= require("fs");
var path="results.txt"

var hostname = '127.0.0.1';
var port = 8080;



fs.readFile(path,'utf8',function(err,data){
	if(err) throw err;
	chartsData=data.split("#");
});



var server = http.createServer();

server.on("request",function (req,res){
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

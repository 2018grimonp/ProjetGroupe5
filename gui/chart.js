
//var L=[24,56,10];
//var titles=["Proportion de commentaires en français","Truc","Machin","Super Machin"];
var colors=["#ff3f15","#10a913","orange","black"];
//var title="Graphique 1";

var canvas;
var ctx;
var w;
var h;

var radius=200;


window.onload=function(){
	w = document.getElementById("canvas").parentNode.clientWidth; 
	h = document.getElementById("canvas").parentNode.clientHeight;
	canvas=document.getElementById("canvas");
	canvas.style.width=w+"px";
	canvas.style.height=h+"px";
	canvas.width=w;
	canvas.height=h;	
	ctx=canvas.getContext('2d');

	document.getElementById("title").innerHTML=title;

	var arc=0;
	for(var i=0;i<L.length;i++){
		ctx.beginPath();
		ctx.moveTo(w/2,h/1.7);
		ctx.fillStyle=colors[i];
		ctx.arc(w/2,h/1.7,radius,arc,2*Math.PI*L[i]/100.0+arc);
		arc=arc+2*Math.PI*L[i]/100.0;
		ctx.fill();
		ctx.closePath();
	}
	ctx.beginPath();
	ctx.moveTo(w/2,h/1.7);
	ctx.fillStyle=colors[colors.length-1];
	ctx.arc(w/2,h/1.7,radius,arc,2*Math.PI);
	ctx.fill();
	ctx.closePath();

	ctx.font="40px Georgia";
	ctx.fillText(note,100,h/2);

	var txt=[];
	for(var i=0;i<titles.length-1;i++){
		txt=txt+"<br><div style='padding:10px;background-color:"+colors[i]+"'>"+titles[i]+"</div>";
	}
	txt=txt+"<br><div style='padding:10px;z-index:2;background-color:"+colors[colors.length-1]+"'>"+titles[colors.length-1]+"</div>";
	document.getElementById("txt").innerHTML=txt;


	
}


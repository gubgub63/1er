var mon_elt = document.getElementById("espace_de_dessin");
var mes_coord = document.getElementById("coord");
mon_elt.addEventListener("click",dessin,false);
var ctx = mon_elt.getContext("2d");
	  
function dessin(evt) {
	var mousePos = getMousePos(mon_elt, evt);
	var x=mousePos.x;
	var y=mousePos.y;   
	mes_coord.innerHTML = "X="+Math.floor(x)+" Y="+Math.floor(y);
	
	
	var points = []
	points.push([x,y]);
	
	for (var i = 0; i < points.length; i++) {
		var R = 10
		ctx.beginPath();
		ctx.arc(points[i][0],points[i][1], R, 0, 2 * Math.PI);
		ctx.fill();
		points[i]
		
		}

}

	
	  
// fonction qui détermine la position de la souris par rapport à la page et
// par rapport à la position du canvas dans la page
// x et y sont alors les coordonnées de la souris par rapport à l'espace du canvas
function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
    x: evt.clientX - rect.left,
	        y: evt.clientY - rect.top
	        };
}



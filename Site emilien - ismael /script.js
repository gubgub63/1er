var objets = document.querySelectorAll('h1');
function change_texte(e) { 
	alert(e.target.firstChild.nodeValue)
	e.target.style.backgroundColor='blue';
    e.target.style.color='green';
}
for(var i = 0; i < objets.length; i++) {
	objets[i].onclick =change_texte
}
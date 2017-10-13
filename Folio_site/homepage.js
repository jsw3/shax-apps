/* 

written by Joe Wallace, October 2017

create_titles function creates links, specifies href attributes from titles array, then appends them appropriately 
also adds the listener that takes user to Preface on clicking the image

*/

function create_titles() {
	var titles = ['The Tempest', 'The Two Gentlemen of Verona', 'The Merry Wiues of Windsor', 
	'Measvre, For Measure', 'The Comedie of Errors', 'Much adoe about Nothing', "Loues Labour's lost", 
	'A Midsommer Nights Dreame', 'The Merchant of Venice', 'As you Like it', 'The Taming of the Shrew', 
	"All's Well, that Ends Well", 'Twelfe Night, Or what you will', 'The Winters Tale', 
	'The life and death of King John', 'The life and death of King Richard the Second', 
	'The First Part of Henry the Fourth', 'The Second Part of Henry the Fourth', 'The Life of Henry the Fift', 
	'The first Part of Henry the Sixt', 'The second Part of Henry the Sixt', 'The third Part of Henry the Sixt', 
	'The Tragedie of Richard the Third', 'The Famous History of the Life of King Henry the Eight', 
	'The Tragedie of Coriolanus', 'The Tragedie of Titus Andronicus', 'The Tragedie of Romeo and Juliet', 
	'The Life of Timon of Athens', 'The Tragedie of Julius Caesar', 'The Tragedie of Macbeth', 'The Tragedie of Hamlet', 
	'The Tragedie of King Lear', 'The Tragedie of Othello, the Moore of Venice', 'The Tragedie of Anthonie, and Cleopatra', 
	'The Tragedie of Cymbeline'];
	var $ = function(id){return document.getElementById(id);};
	var i;
	// for each title create a link to the full text of the play
	for (i = 0; i < titles.length; i++) { 
		var play = document.createElement("a");
		play.href = titles[i]+".html";
		play.innerHTML = titles[i]+"<br>";
		$("one").appendChild(play);
	}
	
	// create copyright notice
	var date = new Date();
	var year = date.getFullYear();
	var copyright = document.createTextNode("@ Joseph Wallace "+ year);
	$("copyright").appendChild(copyright);
	
	// add event listeners for image
	$("title_page").addEventListener("click", function(){location="Preface.html";});
}

function onLoad(f) {
	if (onLoad.loaded) {
		window.setTimeout(f, 0);
	}
	else if (window.addEventListener) {
		window.addEventListener("load", f, false);
	}
	else if (window.attachEvent) {
		window.attachEvent("onload", f);
	}
}
onLoad.loaded = false;
onLoad(function(){onLoad.loaded=true;});
onLoad(create_titles);

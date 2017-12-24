var schedule = {{ schedule|tojson|safe }}
console.log(String(schedule))
var permutations = Object.keys(schedule).length;
console.log(String(permutations))
var div = document.getElementById("samptext")


//for (var i = 0; i < permutations; i++) {
//	document.getElementById("samptext").innerHTML += (String(schedule[i]))
//	document.getElementById("samptext").innerHTML += (linebreak)
//}

window.onload = function start() {
	for (var i = 0; i < permutations; i++) {
		document.getElementById("samptext").innerHTML += (String(schedule[i]))
		document.getElementById("samptext").innerHTML += "<br>"
	}
}

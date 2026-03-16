async function generate(){

let prompt = document.getElementById("prompt").value;

let response = await fetch("http://localhost:5000/generate",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({prompt:prompt})
})

let data = await response.json();

document.getElementById("result").innerText =
"Modelo creado: " + data.file;

}

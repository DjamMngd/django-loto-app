window.onload = function() {
    // votre code ici
    let parent = document.getElementById("background_tirages");
    let numeros = document.getElementsByClassName("numeros");

    for (let i = 0; i < numeros.length; i++) {
        let fontSize = (parent.offsetHeight * 0.4) + "px";
        numeros[i].style.fontSize = fontSize;
    }

    let button = document.getElementById("generate_random_numbers");
    if (button) {
        button.addEventListener("click", getNewNumbers);
    }
};

function getNewNumbers() {
    $.ajax({
        url: 'generate_numbers',
        type: 'GET',
        success: function(response) {
            let numero_1 = document.getElementById("numero_1");
            let numero_2 = document.getElementById("numero_2");
            let numero_3 = document.getElementById("numero_3");
            let numero_4 = document.getElementById("numero_4");
            let numero_5 = document.getElementById("numero_5");
            let numeroChance = document.getElementById("numeroChance");
            numero_1.innerHTML = response.random_tirage_loto[0];
            numero_2.innerHTML = response.random_tirage_loto[1];
            numero_3.innerHTML = response.random_tirage_loto[2];
            numero_4.innerHTML = response.random_tirage_loto[3];
            numero_5.innerHTML = response.random_tirage_loto[4];
            numeroChance.innerHTML = response.random_tirage_loto[5];
        }
    });
}
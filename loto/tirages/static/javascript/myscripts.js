window.onload = function() {
    let parent = document.getElementById("background_tirages");
    let numeros = document.getElementsByClassName("numeros");

    for (let i = 0; i < numeros.length; i++) {
        let fontSize = (parent.offsetHeight * 0.26) + "px";
        numeros[i].style.fontSize = fontSize;
    }

    let buttonLoto = document.getElementById("generate_random_loto_numbers");
    let buttonEuroMillion = document.getElementById("generate_random_euroMillion_numbers");
    if (buttonLoto) {
        buttonLoto.addEventListener("click", getNewLotoNumbers, false);
    }
    if (buttonEuroMillion) {
        buttonEuroMillion.addEventListener("click", getNewEuroMillionNumbers, false);
    }
}

// Fonction onresize qui va permettre de redimentionner mes caractères en fonction 
// de la taille du navigateur qui changera en temps réel

let resizeTimer;
window.onresize = function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
        let parent = document.getElementById("background_tirages");
        let numeros = document.getElementsByClassName("numeros");
        for (let i = 0; i < numeros.length; i++) {
            let fontSize = (parent.offsetHeight * 0.26) + "px";
            numeros[i].style.fontSize = fontSize;
        }
    })
}

function getNewLotoNumbers() {
    $.ajax({
        url: newRandomNumbersURL,
        type: 'GET',
        success: function(response) 
        {
            //alert("test");
            //console.log(response);
            let numero_1 = document.getElementById("numero_1_loto_random");
            let numero_2 = document.getElementById("numero_2_loto_random");
            let numero_3 = document.getElementById("numero_3_loto_random");
            let numero_4 = document.getElementById("numero_4_loto_random");
            let numero_5 = document.getElementById("numero_5_loto_random");
            let numeroChance_1 = document.getElementById("numeroChance_1_loto_random");
            numero_1.innerHTML = response.random_tirage_loto[0];
            numero_2.innerHTML = response.random_tirage_loto[1];
            numero_3.innerHTML = response.random_tirage_loto[2];
            numero_4.innerHTML = response.random_tirage_loto[3];
            numero_5.innerHTML = response.random_tirage_loto[4];
            numeroChance_1.innerHTML = response.random_tirage_loto[5];
        }
    })
}

function getNewEuroMillionNumbers() {
    $.ajax({
        url: newRandomNumbersURL,
        type: 'GET',
        success: function(response) 
        {
            //alert("test");
            //console.log(response);
            let numero_1 = document.getElementById("numero_1_euroMillion_random");
            let numero_2 = document.getElementById("numero_2_euroMillion_random");
            let numero_3 = document.getElementById("numero_3_euroMillion_random");
            let numero_4 = document.getElementById("numero_4_euroMillion_random");
            let numero_5 = document.getElementById("numero_5_euroMillion_random");
            let numeroChance_1 = document.getElementById("numeroChance_1_euroMillion_random");
            let numeroChance_2 = document.getElementById("numeroChance_2_euroMillion_random");
            numero_1.innerHTML = response.random_tirage_euroMillion[0];
            numero_2.innerHTML = response.random_tirage_euroMillion[1];
            numero_3.innerHTML = response.random_tirage_euroMillion[2];
            numero_4.innerHTML = response.random_tirage_euroMillion[3];
            numero_5.innerHTML = response.random_tirage_euroMillion[4];
            numeroChance_1.innerHTML = response.random_tirage_euroMillion[5];
            numeroChance_2.innerHTML = response.random_tirage_euroMillion[6];
        }
    })
}

// Fonction pour faire apparaitre le footer que lorsque nous sommes en bas de la page

// // Récupérez l'élément footer
// const footer = document.getElementById("footer");

// // Ajoutez un écouteur d'événement pour le défilement de la page
// window.addEventListener("scroll", () => {
//   // Récupérez la position de défilement de la page
//   const scrollPos = window.scrollY;

//   // Récupérez la hauteur de la page
//   const height = document.body.offsetHeight - window.innerHeight;

//   // Vérifiez si l'utilisateur est arrivé en bas de la page
//   if (scrollPos >= height) {
//     // Ajoutez la classe "visible" à l'élément footer pour le rendre visible
//     footer.classList.add("visible");
//   } else {
//     // Sinon, enlevez la classe "visible" pour cacher le footer
//     footer.classList.remove("visible");
//   }
// });
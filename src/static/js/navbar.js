function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function escribirTexto(span, velocidad = 100) {
    // Prevenir ejecución múltiple
    if (span.escribiendo) return;

    span.escribiendo = true;
    const texto = span.getAttribute("data-text") || span.dataset.original || span.textContent;

    // Guarda el texto original si no existe
    if (!span.dataset.original) {
        span.dataset.original = texto;
    }

    span.textContent = "";
    span.style.opacity = 1;
    span.style.display = "inline";

    for (let i = 0; i < texto.length; i++) {
        span.textContent += texto[i];
        await esperar(velocidad);
    }

    span.escribiendo = false;
}

function desaparecerTexto(span, velocidad = 50) {
    const textoOriginal = span.dataset.original || span.textContent;
    let i = 0;

    const intervalo = setInterval(() => {
        if (i < textoOriginal.length) {
            span.textContent = textoOriginal.slice(i + 1);
            i++;
        } else {
            clearInterval(intervalo);
            span.style.opacity = 0;  // ⚠️ Usamos opacity en lugar de display
        }
    }, velocidad);
}

let navbar = document.getElementById("fullscreen-menu");
let txtBtns = document.querySelectorAll(".nav-btn-texto");

let timeoutEnter = null;
let timeoutLeave = null;

navbar.addEventListener("mouseenter", () => {
    clearTimeout(timeoutLeave);

    timeoutEnter = setTimeout(() => {
        if (navbar.classList.contains("navbar-hidden")) {
            navbar.classList.remove("navbar-hidden");

            txtBtns.forEach(span => {
                span.style.display = "inline";
                escribirTexto(span, 20);
            });
        }
    }, 100);
});

navbar.addEventListener("mouseleave", () => {
    clearTimeout(timeoutEnter);

    timeoutLeave = setTimeout(() => {
        if (!navbar.classList.contains("navbar-hidden")) {
            navbar.classList.add("navbar-hidden");

            txtBtns.forEach(span => {
                desaparecerTexto(span, 15);
            });
        }
    }, 200);
});

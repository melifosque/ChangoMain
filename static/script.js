document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM completamente cargado.");

    const openBtn = document.getElementById("open-btn");
    const closeBtn = document.getElementById("close-btn");
    const sideMenu = document.getElementById("sidemenu");

    console.log(openBtn, closeBtn, sideMenu); // Verifica si los elementos están siendo seleccionados correctamente

    if (openBtn && closeBtn && sideMenu) {
        openBtn.addEventListener("click", function() {
            sideMenu.style.width = "250px";
        });

        closeBtn.addEventListener("click", function() {
            sideMenu.style.width = "0";
        });

        // Cerrar el menú al hacer clic fuera de él (opcional)
        document.addEventListener("click", function(event) {
            if (event.target === sideMenu) {
                sideMenu.style.width = "0";
            }
        });

        // Mostrar y ocultar submenús (opcional)
        const adminMenu = document.getElementById("adminMenu");
        const submenuToggle = document.querySelector(".bx-search"); // Reemplazar con el selector correcto si es necesario

        if (adminMenu && submenuToggle) {
            submenuToggle.addEventListener("click", function() {
                adminMenu.classList.toggle("oculto");
            });
        }
    } else {
        console.log("Alguno de los elementos necesarios no está presente.");
    }
});

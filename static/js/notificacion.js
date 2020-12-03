//Titulo de la notificación
Push.create("ArduRobotica- DuocUC", {

    //Texto del cuerpo de la notificación
    body: "Abrir Home de ArduRobotica",

    icon: "https://cdn.discordapp.com/attachments/776832412360638524/783912072516993034/logo_push.png", //Icono de la notificación
    timeout: 6000, //Tiempo de duración de la notificación


    onClick: function() {
        //Función que se cumple al realizar clic cobre la notificación
        window.location = "http://localhost:8000/"; //Redirige a la siguiente web
        this.close(); //Cierra la notificación
    },
});

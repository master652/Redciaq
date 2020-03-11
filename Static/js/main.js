
function cerrar(){
    $.ajax({
    type:"GET",
    url:"Salir",
    data:{
    },
    success: function(data){
        location.reload();
    }
});}
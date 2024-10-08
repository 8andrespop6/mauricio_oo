fetch(url)
.then (function(response){
    if (Response.ok){
        return response.text()
    } else {
        	throw "error en la llamada"
    }
    })
    .then (function(texto){
        console.log(texto);
    })

    .catch (function(error){
        console.log(error);
        document.write(error)
        swal(error)

        swal({
            title: "Advertencia",
            text: error,
            icon: "warning",
            button: true,
            dangerMode: true,
          });
    })
}
function opcion1(){
    var t1 = document.querySelector("#t1");
    var t2 = document.querySelector("#t2");
    var t3 = document.querySelector("#t3");
    t1.value = "";
    t2.value = "";
    t3.value = "";
}

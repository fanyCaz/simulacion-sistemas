
let imprimirGrafica = (contaminante,fechas,niveles) =>{
    GRAFICA = document.getElementById('contaminante-'+contaminante);
    let diaGrafica = document.getElementById('dia-contaminante-'+contaminante);
    //FECHAS
    let dates = [];
    var x = 0;
    while(fechas[x]){
        dates.push( fechas[x] );
        x++;
    }
    //HORAS
    let hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23];
    //NIVEL DE CONTAMINANTE
    let contaminantesMes = [];
    for(j = 0; j < dates.length; j++){
        let nivelesContaminanteDia = [];
        for(i = 0; i < 23; i++){
            nivelesContaminanteDia.push( niveles[i][j] );   //nivel contaminante de dia j, a hora i
        }
        contaminantesMes.push(nivelesContaminanteDia);
        //console.log(nivelesContaminanteDia);
    }
    //MOSTRAR GRAFICA
    var contadorDia = 0;
    var t = setInterval(()=>{
        diaGrafica.innerHTML = "";
        if(contadorDia > dates.length - 1){
            clearInterval(t);
            return;
        }
        diaGrafica.innerHTML = contadorDia+1;
        console.log("dia en el que eesta : " + contadorDia);
        console.log(contaminantesMes[contadorDia]);
        var data = [
            {
                title: 'Niveles de ' + contaminante,
                x: hours,
                y: contaminantesMes[contadorDia],
                type: 'scatter',
            }
        ];
        Plotly.newPlot(GRAFICA, data);
        contadorDia++;
    },1000);

}

let traerNivelesContaminante = (url,contaminante)=>{
    xhttp = new XMLHttpRequest();
    console.log(url);
    xhttp.open("GET",url,true);
    xhttp.send();
    xhttp.onreadystatechange = () =>{
        console.log(xhttp.readyState);
        if(xhttp.readyState == XMLHttpRequest.DONE){
            if(xhttp.status == 200){
                console.log("datos bien traidos");
                var response = JSON.parse( xhttp.responseText );
                var fechas = JSON.parse( response.Datos[0].fechas );
                var niveles = JSON.parse( response.Datos[1].niveles );
                imprimirGrafica(contaminante,fechas,niveles);
            }else{
                console.log("no lo trajo bien, hay error");
            }
        }else{
            console.log("not yet, wait for it");
        }
    };
}
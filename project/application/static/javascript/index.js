
var info = (contaminante) => {
    switch(contaminante){
        case 'PM10' : 
            return 'info PM10';
        case 'CO' : 
            return 'info CO';
        case 'Ozono' : 
            return 'info Ozono';
        case 'PM25' : 
            return 'info PM25';
        case 'SO2' : 
            return 'info SO2';
        case 'NO2' : 
            return 'info NO2';
    }
}


let imprimirGrafica = (contaminante,fechas,niveles,hora_max) =>{
    
    //HTML
        //HORA
        let horaMax = document.getElementById('hora-cont');
        horaMax.innerHTML = "La hora con mayor nivel de contaminante es " + hora_max;
        //INFO
        let infoCont = document.getElementById('info-cont');
        console.log(contaminante);
        infoCont.innerHTML = info(contaminante);
        //GRAFICA
        GRAFICA = document.getElementById('contaminante-grafica');
        document.getElementById( "contaminante-info" ).style.display="block";
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
            let nivelesContaminanteDia = [];
            for(i = 0; i < 23; i++){
                nivelesContaminanteDia.push( niveles[i] );   //nivel contaminante promedio
            }
            //MOSTRAR GRAFICA
            console.log(nivelesContaminanteDia);
            var contadorDia = 0;
            var data = [
                {
                    title: 'Niveles de ' + contaminante,
                    x: hours,
                    y: nivelesContaminanteDia,
                    type: 'scatter',
                }
            ];
            Plotly.newPlot(GRAFICA, data);

}

let traerNivelesContaminante = (url,contaminante)=>{
    document.getElementById( "contaminante-info" ).style.display= "none";
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
                var hora_max = JSON.parse( response.Datos[2].hora_maxima )
                imprimirGrafica(contaminante,fechas,niveles,hora_max);
            }else{
                console.log("no lo trajo bien, hay error");
            }
        }else{
            console.log("not yet, wait for it");
        }
    };
}
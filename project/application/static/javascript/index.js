
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
};

let imprimirGraficaReal = (contaminante,fechas,niveles,hora_max,prediccionCont) =>{
    console.log(prediccionCont["0.0"][1] );
    //HTML
        //HORA
        let horaMax = document.getElementById('hora-cont');
        horaMax.innerHTML = "La hora con mayor nivel de contaminante es " + hora_max;
        //INFO
        let infoCont = document.getElementById('info-cont');
        console.log(contaminante);
        infoCont.innerHTML = info(contaminante);
        //CONTAMINANTE
        let predicciones = []
        predicciones.push(0);
        var y = 1;
        
        while(prediccionCont["0.0"][y]){
            predicciones.push(prediccionCont["0.0"][y]);
            y++;
        }
        console.log(predicciones);
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

            var trace1 = {
                type: 'scatter',
                mode: 'lines',
                name : 'Predicciones',
                x : hours,
                y : predicciones,
                line: {color: '#17BECF'}
            };

            var trace2 = {
                type: 'scatter',
                mode: 'lines',
                name : 'Datos Reales',
                x : hours,
                y : nivelesContaminanteDia,
                line: {color: '#504d63'}
            }

            var data = [trace1,trace2];

            var layout = {
                title: 'Nivel de contaminante '+ contaminante,
                xaxis: {
                    range: [0,23],
                },
                yaxis: {
                    range: [0,23]
                }
            };
            Plotly.newPlot(GRAFICA, data, layout);
            document.querySelector('[data-title="Autoscale"]').click();
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
                var hora_max = JSON.parse( response.Datos[2].hora_maxima );
                var prediccionCont = JSON.parse( response.Datos[1].predicciones )
                imprimirGraficaReal(contaminante,fechas,niveles,hora_max,prediccionCont);
            }else{
                console.log("no lo trajo bien, hay error");
            }
        }else{
            console.log("not yet, wait for it");
        }
    };
};
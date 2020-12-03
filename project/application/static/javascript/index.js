
var info = (contaminante) => {
    switch(contaminante){
        case 'PM10' :
            return '¿Que es?: <br/>La combustión de carburantes fósiles generada por el tráfico<br/>(una de las principales fuentes de contaminación por partículas en las ciudades)<br/>puede producir diversos tipos de partículas: partículas grandes,<br/>por la liberación de materiales inquemados (cenizas volátiles),<br/>partículas finas, formadas por la condensación de materiales vaporizados durante la combustión,<br/>y partículas secundarias, mediante reacciones atmosféricas de contaminantes desprendidos como gases.<br/>En relación con sus efectos sobre la salud se suelen distinguir; las PM10<br/>(partículas “torácicas” menores de 10 μm que pueden penetrar hasta las vías respiratorias bajas)<br/> Sus efectos son: <br/>Numerosas enfermedades respiratorias como el asma<br/>problemas cardiovasculares<br/>cáncer de pulmón';
        case 'CO' :
            return '¿Que es?: <br/>Se produce cuando los combustibles a base de carbono, tales como queroseno, <br/>gasolina, gas natural, propano, carbón o madera se queman sin suficiente oxígeno, <br/>lo que provoca una combustión incompleta.<br/>Sus efectos son: <br/>Envenenamiento';
        case 'Ozono' :            
            return '¿Que es?: <br/>Debido a la reacción química entre los óxidos de nitrógeno (NOx)<br/>y los compuestos orgánicos volátiles (COV) en presencia de luz solar.<br/>Las principales fuentes de emisión de los NOx y los COVson los vehículos que utilizan combustibles fósiles,<br/>fugas de gas LP y gas natural, las industrias y las estaciones de gasolina.<br/>Sus efectos son:<br/>Al ser un contaminante ambiental, sus elevadas concentraciones puede provocar daños en la salud<br/>como irritar el sistema respiratorio, agravar el asma y las enfermedades pulmonares crónicas,<br/>reducir la función pulmonar';
        case 'PM25' :
            return '¿Que es?: <br/>La combustión de carburantes fósiles generada por el tráfico<br/>(una de las principales fuentes de contaminación por partículas en las ciudades)<br/>puede producir diversos tipos de partículas: partículas grandes,<br/>por la liberación de materiales inquemados (cenizas volátiles),<br/>partículas finas, formadas por la condensación de materiales vaporizados durante la combustión,<br/>y partículas secundarias, mediante reacciones atmosféricas de contaminantes desprendidos como gases.<br/>En relación con sus efectos sobre la salud se suelen distinguir; las PM10<br/>(partículas “torácicas” menores de 2.5 μm que pueden penetrar hasta las vías respiratorias bajas)<br/> Sus efectos son: <br/>Numerosas enfermedades respiratorias como el asma<br/>problemas cardiovasculares<br/>cáncer de pulmón';
        case 'SO2' :
            return '¿Que es?: <br/>Esta es causada principalmente por la combustión de productos petrolíferos<br/>y la quema de carbón en centrales eléctricas y calefacciones centrales. <br/>Existen también algunas fuentes naturales, como es el caso de los volcanes.<br/>El SO2 también se emplea en la industria del papel como agente blanqueador.<br/>Sus efectos son: <br/>•Dificultad para respirar.<br/>•Inflamación de las vías respiratorias<br/>•Irritación ocular por formación de ácido sulfuroso sobre las mucosas húmedas<br/>•Alteraciones psíquicas <br/>•Edema pulmonar<br/>•Paro cardíaco<br/>•Colapso circulatorio<br/>•Queratitis';
        case 'NO2' :
            return '¿Que es?: <br/>Es un gas más denso que el aire color marrón rojizo de olor acre. <br/>Se toma como referencia para medir los niveles de contaminación entre las muchas <br/>sustancias que emiten los vehículos a motor, como el dióxido y monóxido de carbono, <br/>los óxidos de azufre o partículas en suspensión.<br/>Sus efectos son: <br/>Esto afecta a las vías respiratorias y puede agravar enfermedades cardiovasculares. <br/>Los síntomas de los niños con bronquitis o asma se agravan. <br/>En general, en infantes se ha observado un menor desarrollo de la capacidad pulmonar.';
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
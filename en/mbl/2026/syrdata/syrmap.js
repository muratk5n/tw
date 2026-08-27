

function init() {
    map = L.map('map').setView([35,38], 6);
    
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '<a href="https://www.google.com/maps/d/u/0/viewer?mid=1liqnO9iSvshTLwgPB3q9sJTgfUI">Suriyak Maps</a>'
    }).addTo(map);

}    

function plot_blocks(block, dashes) {
    // Helper function to plot multi-ring blocks safely
    function drawBlock(blockData, color) {
        if (!blockData) return;

        blockData.forEach(function(ring) {
            var points = ring.map(function(coord) {
                // Swap [longitude, latitude] to Leaflet's [latitude, longitude]
                return [coord[1], coord[0]];
            });

            var line = new L.Polyline(points, {
                color: color,
                weight: 2,
                dashArray: dashes,
                dashOffset: '0'
            });
            line.addTo(map);
        });
    }

    drawBlock(blocks["HTS"], 'green');
    drawBlock(blocks["TR"], 'lightgreen');
    drawBlock(blocks["ISR"], 'black');
    drawBlock(blocks["DRUZE"], 'magenta');
    drawBlock(blocks["SDF"], 'orange');
    drawBlock(blocks["ISIS"], 'brown');
}

function plot(before,after) {

    console.log(before);
    console.log(after);
    
    url = `/tw/en/mbl/${before}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);

    plot_blocks(blocks, '3 3');
    
    url = `/tw/en/mbl/${after}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);

    plot_blocks(blocks, '0 0');
    
    // ---------------------------------------------------
    var legend = L.control({position: 'topright'});

    legend.onAdd = function (map) {
	var div = L.DomUtil.create('div', 'info legend'),
	    
	    grades = [["Druze","magenta"],["TR","lightgreen"],["HTS","green"],
		      ["ISR","black"],["SDF","orange"],["ISIS","brown"]];

	// loop through our density intervals and generate a label with a colored square for each interval
	for (var i = 0; i < grades.length; i++) {
            div.innerHTML += "<span style='color:" + grades[i][1] + ";'>" + grades[i][0] + "</span>,&nbsp;";
	}
	return div;
    };

    legend.addTo(map);
    
       
}

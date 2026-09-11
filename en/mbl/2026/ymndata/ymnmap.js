
function plot(before,after) {

    console.log(before);
    console.log(after);
    
    url = `/tw/en/mbl/${before}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);
    blocks.forEach(function(res) {    
	bef = []
	res.forEach(function(x) {
	    bef.push([x[1],x[0]]);
	});    
	var linebef = new L.Polyline(bef, {
	    color: 'darkblue', weight: 2, opacity: 0.5, smoothFactor: 1
	});
	linebef.addTo(map);
    });
    
    url = `/tw/en/mbl/${after}`;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url = url, false ); 
    xmlHttp.send( null );
    result = xmlHttp.responseText;
    blocks = JSON.parse(result);
    blocks.forEach(function(res) {        
	aft = []
	res.forEach(function(x) {
	    aft.push([x[1],x[0]]);
	});    
	var lineaft = new L.Polyline(aft, {
	    color: 'red', weight: 2, opacity: 0.5, smoothFactor: 1
	});
	lineaft.addTo(map);
    });

}

function init() {
    map = L.map('map').setView([15.1027, 45.203], 9);

    L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
	maxZoom: 20,
	subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
	attribution: '&copy; Google Maps | <a href="https://www.google.com/maps/d/viewer?mid=1k_5mC2oHM9Lj4I5irFA0pkXbqKQ">Suriyak Maps</a>'
    }).addTo(map);

}

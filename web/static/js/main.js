function log(foo) {
    return console.log(foo);
}

function randomColorHex() {
    // Creds: http://www.paulirish.com/2009/random-hex-color-code-snippets/
    var color = Math.floor(Math.random()*16777215).toString(16);
    return '#' + color;
}

function rando(max) {
    return Math.floor(Math.random() * max);
}

function randomColor(max) {
    // return a random color,
    // in rgba format
    if(isNaN(max)) {
        max = 255;
    }
    return 'rgb(' + rando(max) + ',' + rando(max) + ',' + rando(max) + ')';
}

function getSVG(id, dims, container) {
    // Courtesy of ... christabor.github.io/etude/
    return d3.select(container || '#svg-container')
    .append('svg').attr('id', id)
    .attr('width', dims.w || dims.width)
    .attr('height', dims.h || dims.height);
}

var namebot = (function(){
    var json_val   = $('#json-data').html();
    var data    = $.parseJSON(json_val);
    var height = 200;
    var width = 500;
    var dims = {'width': width, 'height': height};
    var PADDING = 20;

    function init() {

        var bar_width = 10;
        var letter_freq = d3.values(data.metrics.first_letter_freq.data);
        var letter_freq_letters = d3.keys(data.metrics.first_letter_freq.data);

        var color_scale = d3.scale.linear()
        .domain([0, d3.max(letter_freq)])
        .range(['gray', 'orange']);

        var chart_scale = d3.scale.linear()
        .domain([0, d3.max(letter_freq)])
        .range([1, height - PADDING]);

        /*
            Letter frequency chart

         */

        // first letter frequency
        var $fl = getSVG('flf', dims, '#chart-first_letter_freq');
        $fl.selectAll('rect')
        .data(letter_freq)
        .enter()
        .append('rect')
        .attr('width', bar_width)
        .attr('x', function(d, i){return i * 20;})
        .attr('y', 10)
        .attr('fill', function(d){return color_scale(d);})
        .attr('height', function(d){return chart_scale(d);});

        // letter frequency count
        $fl.selectAll('.label')
        .data(letter_freq)
        .enter()
        .append('text')
        .attr('font-size', 10)
        .attr('text-anchor', 'middle')
        .text(function(d){return d;})
        .attr('x', function(d, i){return i * 20 + bar_width / 2;})
        .attr('y', function(d){return chart_scale(d) + bar_width * 2.2;})
        .attr('fill', function(d){return color_scale(d);});

        // letters
        $fl.selectAll('.frequencies')
        .data(letter_freq_letters)
        .enter()
        .append('text')
        .attr('font-size', 10)
        .attr('text-anchor', 'middle')
        .text(function(d){return d;})
        .attr('x', function(d, i){return i * 20 + bar_width / 2;})
        .attr('y', 0)
        .attr('fill', 'orange');

        /*
            Letter length

         */

        var length_data = data.metrics.length.data;

        var color_scale_l = d3.scale.linear()
        .domain([0, d3.max(length_data)])
        .range(['gray', 'orange']);

        var chart_scale_l = d3.scale.linear()
        .domain([0, d3.max(length_data)])
        .range([1, height - PADDING]);

        var $length = getSVG('length', dims, '#chart-length');
        $length.selectAll('.length-bars')
        .data(data.metrics.length.data)
        .enter()
        .append('rect')
        .attr('width', bar_width)
        .attr('x', function(d, i){return i * 20;})
        .attr('y', 10)
        .attr('fill', function(d){return color_scale_l(d);})
        .attr('height', function(d){return chart_scale_l(d);});

        // letter frequency count
        $length.selectAll('.length-labels')
        .data(data.metrics.length.data)
        .enter()
        .append('text')
        .attr('font-size', 10)
        .attr('text-anchor', 'middle')
        .text(function(d){return d;})
        .attr('x', function(d, i){return i * 20 + bar_width / 2;})
        .attr('y', function(d){return chart_scale_l(d) + bar_width * 2.2;})
        .attr('fill', function(d){return color_scale_l(d);});
    }

    return {
        'init': init
    };

})();

$(document).ready(namebot.init);

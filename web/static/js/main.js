$(document).ready(function(){
    var json_val   = $('#json-data').html();
    var metrics    = $.parseJSON(json_val);
    var chart_opts = {
        percentageInnerCutout: 30,
        animation: false,
        segmentShowStroke: false,
        animateScale: false,
        scaleShowLabels: false
    };
    var canvases   = document.querySelectorAll('canvas');

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

    function addChart(key, value) {
        var id = $(this).find('canvas').attr('id');
        log(id);
        addNewPieChart(canvases[key], metrics.metrics[id], true, true);
        return;
    }

    function populateCharts() {
        log(metrics.metrics);
        if(!canvases.length) return;
        $('.chart-container').each(addChart);
        return;
    }

    function addNewPieChart(canvas, data, use_key, add_labels) {
        var container = $('#' + canvas.id);
        var sections;
        var clean_data;
        var chart;
        var labels = [];
        var label_container = $('#chart-' + canvas.id).find('.labels');
        log(label_container);

        // remove if no data (_always_ expected to be null)
        if((!data.data && !data.summary) || !data.data) {
            container.parent().fadeTo(10, 0.4);
            container.remove();
            return;
        }

        // for large datasets we'll turn it off
        // (for now)
        if(data.data.length > 100) return;

        clean_data = [];

        // build chart data
        $.each(data.data, function(k, section){
            var label;
            var color = randomColor(200);
            var label_text;

            // build value/color map
            // per chart.js specifications
            // (k + ': ' + section),
            clean_data.push({
                value: section,
                color: color
            });

            // add custom labels if necessary
            if(add_labels) {
                label_text = (use_key ? k + ': ' + section : section);
                label = '<span class="label" style="background-color:' + color + '">' + label_text + '</span>';
                labels.push(label);
            }
            return;
        });

        log(clean_data);
        log([{'value': 40, 'color': randomColorHex()}, {'value': 20, 'color': randomColorHex()}, {'value': 40, 'color': randomColorHex()}]);

        // add labels if specified

        label_container.html('<p>Labels: </p>' + labels.join(''));

        // init chart
        chart = new Chart(canvas.getContext('2d'))
        .Doughnut(clean_data, chart_opts);

        // add generated summary
        label_container.append('<p>Summary: ' + (data.summary || 'No summary.') + '</p>');

        return;
    }

    populateCharts();
    return;
});

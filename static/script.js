document.querySelector("#submit > input").addEventListener('click', function() {

    document.getElementById("output").removeAttribute("style")

    var hop_var = $('#variety').val();
    var prod_type = $('#format').val();
    var amount = $('#amount').val();
    
    fetch('/predict/', {
        method: 'POST',
        body: JSON.stringify({'hop_var': hop_var, 'prod_type': prod_type, 'amount': amount}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(async response => {

        response = await response.json();

        if ('No results' in response) {
            $('#output1').html('<div class="alert alert-success" role="alert">No data to predict such combination</div><br/>');
            $('#output2').html('');
            $('#output3').html('');
            return;
        }

        var min_citrus = parseFloat(response.min_predictions[0][0].toFixed(2));
        var min_herbal = parseFloat(response.min_predictions[0][1].toFixed(2));
        var min_hoppy = parseFloat(response.min_predictions[0][2].toFixed(2));

        var average_citrus = parseFloat(response.average_predictions[0][0].toFixed(2));
        var average_herbal = parseFloat(response.average_predictions[0][1].toFixed(2));
        var average_hoppy = parseFloat(response.average_predictions[0][2].toFixed(2));

        var max_citrus = parseFloat(response.max_predictions[0][0].toFixed(2));
        var max_herbal = parseFloat(response.max_predictions[0][1].toFixed(2));
        var max_hoppy = parseFloat(response.max_predictions[0][2].toFixed(2));

        $('#output1').html('<div class="alert alert-success" role="alert">Minimum Citrus: <strong>' + min_citrus + '</strong><br/>Minimum Herbal (herbaceous): <strong>' + min_herbal + '</strong><br/>Minimum overall hoppy intensity: <strong>' + min_hoppy + '</strong></div><br/>');

        $('#output2').html('<div class="alert alert-success" role="alert">Average Citrus: <strong>' + average_citrus + '</strong><br/>Average Herbal (herbaceous): <strong>' + average_herbal + '</strong><br/>Average overall hoppy intensity: <strong>' + average_hoppy + '</strong></div><br/>');

        $('#output3').html('<div class="alert alert-success" role="alert">Maximum Citrus: <strong>' + max_citrus + '</strong><br/>Maximum Herbal (herbaceous): <strong>' + max_herbal + '</strong><br/>Maximum overall hoppy intensity: <strong>' + max_hoppy + '</strong></div><br/>');
        console.log("test")
        generate_chart(response.min_predictions, response.average_predictions, response.max_predictions)
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function generate_chart(min_predictions, average_predictions, max_predictions) {

    var max, min, average, chart;

    for(var i = 0; i < 3; i++) {
        switch(i) {
            case 0: chart = '#overall .chart_div'; break;
            case 1: chart = '#herbal .chart_div'; break;
            case 2: chart = '#citrus .chart_div'; break;
        }
        max = parseFloat(max_predictions[0][i]).toFixed(2)
        min = parseFloat(min_predictions[0][i]).toFixed(2)
        average = parseFloat(average_predictions[0][i]).toFixed(2)

        display_chart(chart, max, min, average)
    }
}

function display_chart(chart, max, min, average) {
    document.querySelector(chart).innerHTML = `

        <div class="labels">
            <p>min</p>
            <p>avg</p>
            <p>max</p>
        </div>
        <div class="chart">
            <span class="avg-line"></span>
        </div>
        <div class="values">
            <p>${min}</p>
            <p>${average}</p>
            <p>${max}</p>
        </div>
    `;
}
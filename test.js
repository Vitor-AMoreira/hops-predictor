$.ajax({
    url: '/predict/Centennial/Cryo',
    type: 'GET',
    success: function(data) {
        var minPredictions = data.min_predictions;
        var maxPredictions = data.max_predictions;
        var averagePredictions = data.average_predictions;
        // Display the predicted values on the webpage using JavaScript
    }
});
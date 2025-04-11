// Weather widget functionality
document.addEventListener('DOMContentLoaded', function() {
    const weatherWidget = document.getElementById('weather-widget');
    
    if (weatherWidget) {
        fetchWeatherData();
    }
    
    // Function to fetch weather data from the API
    function fetchWeatherData() {
        // In a real application, this would be a call to a weather API
        // For demonstration, we'll use mock data
        // setTimeout to simulate API call
        setTimeout(() => {
            const weatherData = {
                temperature: 28,
                condition: "Sunny",
                location: "Delhi Region",
                humidity: 65,
                windSpeed: 10
            };
            
            updateWeatherWidget(weatherData);
        }, 1000);
    }
    
    // Function to update the weather widget with data
    function updateWeatherWidget(data) {
        if (weatherWidget) {
            let iconClass = 'fa-sun';
            
            // Determine icon based on condition
            switch(data.condition.toLowerCase()) {
                case 'cloudy':
                    iconClass = 'fa-cloud';
                    break;
                case 'rainy':
                    iconClass = 'fa-cloud-rain';
                    break;
                case 'stormy':
                    iconClass = 'fa-bolt';
                    break;
                case 'snowy':
                    iconClass = 'fa-snowflake';
                    break;
                case 'foggy':
                    iconClass = 'fa-smog';
                    break;
                case 'partly cloudy':
                    iconClass = 'fa-cloud-sun';
                    break;
                default:
                    iconClass = 'fa-sun';
            }
            
            // Update widget HTML
            weatherWidget.innerHTML = `
                <div class="weather-content">
                    <div class="weather-icon">
                        <i class="fas ${iconClass}"></i>
                    </div>
                    <div class="weather-info">
                        <h3>Current Weather</h3>
                        <div class="weather-temp">${data.temperature}°C</div>
                        <div>${data.condition}, ${data.location}</div>
                    </div>
                </div>
                <div class="weather-details">
                    <div>Humidity: ${data.humidity}%</div>
                    <div>Wind: ${data.windSpeed} km/h</div>
                </div>
            `;
            
            // Show the widget
            weatherWidget.style.display = 'block';
        }
    }
    
    // In a real application, you could periodically update the weather
    // setInterval(fetchWeatherData, 600000); // update every 10 minutes
});
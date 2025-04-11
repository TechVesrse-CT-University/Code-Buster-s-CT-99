// Soil Management Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const soilGrid = document.getElementById('soil-grid');
    
    
    // Sample soil data
    const soilsData = [
        {
            id: 1,
            name: "Clay Soil",
            imageUrl: "https://img.freepik.com/free-photo/broken-bronzer-makeup-powder-background_53876-101325.jpg?semt=ais_hybrid&w=740",
            characteristics: [
                { text: "High nutrient content", type: "positive" },
                { text: "Good water retention", type: "positive" },
                { text: "Poor drainage can lead to waterlogging", type: "negative" },
                { text: "Can be difficult to work with when wet", type: "negative" }
            ]
        },
        {
            id: 2,
            name: "Sandy Soil",
            imageUrl: "https://ecogardener.com/cdn/shop/articles/Improving_Sandy_Soil_Choosing_a_Soil_Amendment-min.jpg?v=1722484898",
            characteristics: [
                { text: "Good drainage", type: "positive" },
                { text: "Warms up quickly in spring", type: "positive" },
                { text: "Poor nutrient retention", type: "negative" },
                { text: "Requires frequent watering", type: "negative" }
            ]
        },
        {
            id: 3,
            name: "Loamy Soil",
            imageUrl: "https://images.unsplash.com/photo-1590682680695-43b964a3ae17?auto=format&fit=crop&w=400&h=250&q=80",
            characteristics: [
                { text: "Excellent structure for plant growth", type: "positive" },
                { text: "Good nutrient retention", type: "positive" },
                { text: "Balanced water drainage and retention", type: "positive" },
                { text: "Supports diverse microbial life", type: "positive" }
            ]
        },
        {
            id: 4,
            name: "Silty Soil",
            imageUrl: "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=400&h=250&q=80https://images.unsplash.com/photo-1595857819937-8d15130b4add?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&h=350&q=80",
            characteristics: [
                { text: "Good fertility and water retention", type: "positive" },
                { text: "Smooth texture that's easy to work with", type: "positive" },
                { text: "Can become compacted easily", type: "negative" },
                { text: "Prone to erosion when dry", type: "negative" }
            ]
        }
    ];
    
    // Show soil cards after a brief delay to simulate loading
    setTimeout(() => {
        renderSoilCards();
    }, 1000);

    function getSoilRecommendation() {
        const ph = parseFloat(document.getElementById("ph").value);
        const n = document.getElementById("nitrogen").value;
        const p = document.getElementById("phosphorus").value;
        const k = document.getElementById("potassium").value;
        const texture = document.getElementById("texture").value;
        const water = document.getElementById("water").value;
      
        let crop = "⚠️ Please complete all inputs.";
        let fertilizer = "❗";
        let irrigationTip = "💧";
        let soilTip = "🧱";
      
        if (ph && n && p && k && texture && water) {
          if (ph >= 6 && ph <= 7 && n === "Medium" && p === "Medium" && k === "Medium" && texture === "Loamy") {
            crop = "🌾 Ideal for wheat, maize, rice, and barley.";
            fertilizer = "🧪 Use balanced NPK 10-10-10.";
          } else if (n === "Low") {
            crop = "🌿 Legumes like beans and peas fix nitrogen.";
            fertilizer = "💡 Use nitrogen-rich fertilizers like urea.";
          } else if (ph < 6) {
            crop = "🥕 Acid-loving crops: carrots, potatoes, radish.";
            fertilizer = "🧪 Apply lime and organic compost.";
          } else {
            crop = "🪴 Consider tomatoes, onions, or spinach depending on climate.";
            fertilizer = "🧪 Use soil-specific organic mix.";
          }
      
          if (water === "Low") {
            irrigationTip = "💧 Drip irrigation & mulch for moisture retention.";
          } else if (water === "High") {
            irrigationTip = "⚠️ Ensure proper drainage; risk of root rot.";
          } else {
            irrigationTip = "💦 Water 2–3 times/week depending on weather.";
          }
      
          if (texture === "Clay") {
            soilTip = "🧱 Clay retains water. Add compost for aeration.";
          } else if (texture === "Sandy") {
            soilTip = "🏜️ Sandy drains fast. Add organic matter.";
          } else if (texture === "Loamy") {
            soilTip = "🌿 Loamy is ideal. Maintain with compost.";
          } else if (texture === "Silty") {
            soilTip = "💧 Silty is fertile but may compact. Add mulch.";
          }
        }
      
        document.getElementById("advisorOutput").innerHTML = `
          <h4>🌾 Crop Recommendation:</h4><p>${crop}</p>
          <h4>🧪 Fertilizer Advice:</h4><p>${fertilizer}</p>
          <h4>💧 Watering Tip:</h4><p>${irrigationTip}</p>
          <h4>🧱 Soil Health Tip:</h4><p>${soilTip}</p>
        `;
        document.getElementById("advisorOutput").style.display = "block";
      }
      
    
    // Function to render soil cards
    function renderSoilCards() {
        if (!soilGrid) return;
        
        let cardsHTML = '';
        
        soilsData.forEach(soil => {
            let characteristicsHTML = '';
            
            soil.characteristics.forEach(char => {
                const iconClass = char.type === 'positive' ? 'fa-check' : 'fa-times';
                characteristicsHTML += `
                    <li class="${char.type}">
                        <i class="fas ${iconClass}"></i>
                        <span>${char.text}</span>
                    </li>
                `;
            });
            
            cardsHTML += `
                <div class="soil-card">
                    <div class="soil-image">
                        <img src="${soil.imageUrl}" alt="${soil.name}">
                    </div>
                    <div class="soil-details">
                        <h3 class="soil-name">${soil.name}</h3>
                        <ul class="soil-characteristics">
                            ${characteristicsHTML}
                        </ul>
                    </div>
                </div>
            `;
        });
        
        soilGrid.innerHTML = cardsHTML;
    }
    
      
    
      
});
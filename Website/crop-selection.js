// Crop Selection Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const cropSelectionForm = document.getElementById('crop-selection-form');
    const cropResults = document.getElementById('crop-results');
    const loadingIndicator = document.getElementById('loading-indicator');
    
    // Sample crop data
    const cropsData = [
        {
            id: 1,
            name: "Rice",
            imageUrl: "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&h=350&q=80",
            description: "A staple food crop that thrives in water-logged conditions with high temperatures.",
            season: "Kharif",
            waterRequirement: "High",
            soilType: "clay",
            region: "east"
        },
        {
            id: 2,
            name: "Wheat",
            imageUrl: "https://images.unsplash.com/photo-1437252611977-07f74518abd7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8d2hlYXR8ZW58MHx8MHx8fDA%3D",
            description: "A rabi crop that requires moderately cool climate during growing season and bright sunshine at maturity.",
            season: "Rabi",
            waterRequirement: "Moderate",
            soilType: "loamy",
            region: "north"
        },
        {
            id: 3,
            name: "Cotton",
            imageUrl: "https://t3.ftcdn.net/jpg/02/30/14/32/360_F_230143255_R9DbrztVKjX3G7MZBL8DdbLxjxccJJnb.jpg",
            description: "A cash crop that requires warm climate, abundant sunshine and moderate rainfall.",
            season: "Kharif",
            waterRequirement: "Moderate",
            soilType: "sandy",
            region: "central"
        },
        {
            id: 4,
            name: "Sugarcane",
            imageUrl: "https://www.pepperhub.in/wp-content/uploads/2024/01/cultivation-of-sugarcane.webp",
            description: "A long duration crop that requires hot and humid climate with adequate rainfall or irrigation.",
            season: "Multiple",
            waterRequirement: "High",
            soilType: "loamy",
            region: "south"
        },
        {
            id: 5,
            name: "Maize",
            imageUrl: "https://media.istockphoto.com/id/1133692494/photo/corn-cob-with-green-leaves-growth-in-agriculture-field-outdoor.jpg?s=612x612&w=0&k=20&c=xFYeDDO46cJ73fXEvqt0NFV6mSugjXoDAxdBNqno9Ac=",
            description: "A versatile crop that can be grown in various seasons and requires moderate temperature and rainfall.",
            season: "Kharif",
            waterRequirement: "Moderate",
            soilType: "loamy",
            region: "west"
        },
        {
            id: 6,
            name: "Potatoes",
            imageUrl: "https://images.unsplash.com/photo-1590165482129-1b8b27698780?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&h=350&q=80",
            description: "A cool-season crop that requires well-drained, loose soil and consistent moisture.",
            season: "Rabi",
            waterRequirement: "Moderate",
            soilType: "sandy",
            region: "north"
        }
    ];
    
    // Show initial recommendations (3 random crops)
    showInitialRecommendations();
    
    // Handle form submission
    if (cropSelectionForm) {
        cropSelectionForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const region = document.getElementById('region').value;
            const soilType = document.querySelector('input[name="soilType"]:checked')?.value;
            
            // Show loading state
            if (loadingIndicator) {
                loadingIndicator.style.display = 'flex';
            }
            if (cropResults) {
                cropResults.style.display = 'none';
            }
            
            // Simulate API call delay
            setTimeout(() => {
                getRecommendedCrops(region, soilType);
            }, 1000);
        });
    }
    
    // Function to show initial crop recommendations
    function showInitialRecommendations() {
        if (cropResults) {
            // Get 3 random crops for initial display
            const initialCrops = cropsData.sort(() => 0.5 - Math.random()).slice(0, 3);
            renderCropCards(initialCrops);
        }
    }
    
    // Function to get crop recommendations based on region and soil type
    function getRecommendedCrops(region, soilType) {
        // Filter crops based on region and soil type
        let filteredCrops = cropsData;
        
        if (region && soilType) {
            filteredCrops = cropsData.filter(crop => 
                crop.region === region && crop.soilType === soilType
            );
        } else if (region) {
            filteredCrops = cropsData.filter(crop => crop.region === region);
        } else if (soilType) {
            filteredCrops = cropsData.filter(crop => crop.soilType === soilType);
        }
        
        // Hide loading state
        if (loadingIndicator) {
            loadingIndicator.style.display = 'none';
        }
        if (cropResults) {
            cropResults.style.display = 'grid';
        }
        
        // Render results
        renderCropCards(filteredCrops);
    }
    
    // Function to render crop cards
    function renderCropCards(crops) {
        if (!cropResults) return;
        
        if (crops.length === 0) {
            cropResults.innerHTML = `
                <div class="no-results">
                    <p>No crop recommendations found for your selection. Please try different criteria.</p>
                </div>
            `;
            return;
        }
        
        let cardsHTML = '';
        
        crops.forEach(crop => {
            cardsHTML += `
                <div class="crop-card">
                    <div class="crop-image">
                        <img src="${crop.imageUrl}" alt="${crop.name}">
                    </div>
                    <div class="crop-details">
                        <h3 class="crop-name">${crop.name}</h3>
                        <div class="crop-badges">
                            <span class="crop-badge badge-season">${crop.season} Season</span>
                            <span class="crop-badge badge-water">${crop.waterRequirement} Water</span>
                        </div>
                        <p class="crop-description">${crop.description}</p>
                        <a href="#" class="crop-link">View detailed guide <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            `;
        });
        
        cropResults.innerHTML = cardsHTML;
    }
});
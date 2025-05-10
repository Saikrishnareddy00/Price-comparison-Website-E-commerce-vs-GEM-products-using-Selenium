function comparePrices() {
    const product = document.getElementById("productInput").value;
    if (!product.trim()) return;

    const prices = {
        "Amazon": 32990,
        "GeM": 10000,
        "Flipkart": 114990
    };

    const cardData = `
        <div class="card">
            <h3>Amazon</h3>
            <p><strong>Product:</strong> Acer Aspire Lite AMD Ryzen 5 5500U Premium Thin and Light Laptop (16 GB RAM/512 GB SSD/Windows 11 Home) AL15-41, 39.62 cm (15.6") Full HD Display, Metal Body, Steel Gray, 1.59 KG</p>
            <p><strong>Price:</strong> ₹${prices.Amazon}</p>
        </div>
        <div class="card">
            <h3>GeM</h3>
            <p><strong>Product:</strong> Acer Aspire Lite AMD Ryzen 5 5500U Premium Thin and Light Laptop (16 GB RAM/512 GB SSD/Windows 11 Home) AL15-41, 39.62 cm (15.6") Full HD Display, Metal Body, Steel Gray, 1.59 KG</p>
            <p><strong>Price:</strong> ₹${prices.GeM}</p>
        </div>
        <div class="card">
            <h3>Flipkart</h3>
            <p><strong>Product:</strong> Acer Aspire Lite AMD Ryzen 5 5500U Premium Thin and Light Laptop (16 GB RAM/512 GB SSD/Windows 11 Home) AL15-41, 39.62 cm (15.6") Full HD Display, Metal Body, Steel Gray, 1.59 KG</p>
            <p><strong>Price:</strong> ₹${prices.Flipkart}</p>
        </div>
    `;

    document.getElementById("priceCards").innerHTML = cardData;

    const amazonGemDiff = prices.Amazon - prices.GeM;
    const flipkartGemDiff = prices.Flipkart - prices.GeM;

    document.getElementById("priceDiffs").innerHTML = `
        Price Difference (Amazon vs GeM): ₹${amazonGemDiff}<br>
        Price Difference (Flipkart vs GeM): ₹${flipkartGemDiff}
    `;

    const lowestSite = Object.entries(prices).reduce((a, b) => a[1] < b[1] ? a : b)[0];
    document.getElementById("lowestText").textContent = `${lowestSite} has the lower price!`;

    displayChart(prices);
}

function displayChart(prices) {
    const ctx = document.getElementById('priceChart').getContext('2d');

    if (window.barChart) {
        window.barChart.destroy();
    }

    window.barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(prices),
            datasets: [{
                label: 'Price Comparison',
                data: Object.values(prices),
                backgroundColor: 'dodgerblue'
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

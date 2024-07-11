document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = '/api/prices';
    const cryptoList = document.getElementById('crypto-prices');

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const cryptoIds = ['bitcoin', 'ethereum', 'ripple'];
            cryptoIds.forEach(id => {
                const li = document.createElement('li');
                li.textContent = `${id}: $${data[id].usd}`;
                cryptoList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

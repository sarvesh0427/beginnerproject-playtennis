document.getElementById('predictBtn').addEventListener('click', async () => {
    // 1. Collect values from the form
    const data = {
        outlook: document.getElementById('outlook').value,
        temperature: document.getElementById('temp').value,
        humidity: document.getElementById('humidity').value,
        wind: document.getElementById('wind').value
    };

    const resultContainer = document.getElementById('resultContainer');
    const resultValue = document.getElementById('resultValue');

    try {
        // 2. Send the data to the FastAPI backend
        const response = await fetch('https://beginnerproject-playtennis.onrender.com/predict', {method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // 3. Process the response
        const result = await response.json();
        
        // 4. Update the UI
        resultValue.innerText = result.play_tennis === 'Yes' ? '✅ Play Tennis!' : '❌ Stay Inside';
        resultContainer.classList.remove('hidden');

    } catch (error) {
        console.error('Error:', error);
        alert('Make sure your FastAPI server is running!');
    }
});
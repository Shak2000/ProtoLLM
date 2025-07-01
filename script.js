// script.js

document.addEventListener('DOMContentLoaded', () => {
    // Get references to DOM elements
    const trainingText = document.getElementById('trainingText');
    const trainButton = document.getElementById('trainButton');
    const trainStatus = document.getElementById('trainStatus');
    const promptInput = document.getElementById('promptInput');
    const energySlider = document.getElementById('energySlider');
    const energyValue = document.getElementById('energyValue');
    const queryButton = document.getElementById('queryButton');
    const llmResponse = document.getElementById('llmResponse');
    const queryStatus = document.getElementById('queryStatus');

    // Update energy value display when slider moves
    energySlider.addEventListener('input', () => {
        energyValue.textContent = energySlider.value;
    });

    // Event listener for the Train button
    trainButton.addEventListener('click', async () => {
        const text = trainingText.value.trim(); // Get text from textarea and remove leading/trailing whitespace
        if (!text) {
            trainStatus.textContent = 'Please enter some text to train the LLM.';
            trainStatus.style.color = 'red';
            return;
        }

        trainStatus.textContent = 'Training LLM...';
        trainStatus.style.color = '#2563EB'; // Blue-600

        try {
            // Send a POST request to the /train endpoint
            const response = await fetch(`/train?text=${encodeURIComponent(text)}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                trainStatus.textContent = 'LLM trained successfully!';
                trainStatus.style.color = '#16A34A'; // Green-600
                trainingText.value = ''; // Clear the textarea after successful training
            } else {
                const errorData = await response.text();
                trainStatus.textContent = `Error training LLM: ${errorData}`;
                trainStatus.style.color = 'red';
            }
        } catch (error) {
            trainStatus.textContent = `Network error: ${error.message}`;
            trainStatus.style.color = 'red';
            console.error('Error during training:', error);
        }
    });

    // Event listener for the Generate Message button
    queryButton.addEventListener('click', async () => {
        const prompt = promptInput.value.trim(); // Get prompt from input and remove leading/trailing whitespace
        const energy = parseFloat(energySlider.value) / 10.0; // Convert slider value to a float between 0 and 0.9

        if (!prompt) {
            queryStatus.textContent = 'Please enter a prompt to generate a message.';
            queryStatus.style.color = 'red';
            llmResponse.textContent = 'LLM response will appear here...';
            llmResponse.style.color = '#6B7280'; // Gray-500
            llmResponse.style.fontStyle = 'italic';
            return;
        }

        llmResponse.textContent = 'Generating message...';
        llmResponse.style.color = '#2563EB'; // Blue-600
        llmResponse.style.fontStyle = 'normal';
        queryStatus.textContent = ''; // Clear previous status

        try {
            // Send a GET request to the /gen_message endpoint
            const response = await fetch(`/gen_message?message=${encodeURIComponent(prompt)}&energy=${energy}`);

            if (response.ok) {
                const message = await response.text(); // Get the generated message as plain text
                llmResponse.textContent = message;
                llmResponse.style.color = '#1F2937'; // Gray-800
                llmResponse.style.fontStyle = 'normal';
                queryStatus.textContent = 'Message generated successfully!';
                queryStatus.style.color = '#16A34A'; // Green-600
            } else {
                const errorData = await response.text();
                llmResponse.textContent = `Error: ${errorData}`;
                llmResponse.style.color = 'red';
                llmResponse.style.fontStyle = 'normal';
                queryStatus.textContent = 'Failed to generate message.';
                queryStatus.style.color = 'red';
            }
        } catch (error) {
            llmResponse.textContent = `Network error: ${error.message}`;
            llmResponse.style.color = 'red';
            llmResponse.style.fontStyle = 'normal';
            queryStatus.textContent = 'Failed to connect to the server.';
            queryStatus.style.color = 'red';
            console.error('Error during message generation:', error);
        }
    });
});

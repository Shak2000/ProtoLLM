# Proto-LLM

A simple prototype language model implementation that demonstrates basic text generation using Markov chains. This project includes both a command-line interface and a web-based UI built with FastAPI.

## Overview

Proto-LLM is a minimalist language model that learns word patterns from training text and generates new text based on those patterns. It uses a probabilistic approach where each word is followed by words that appeared after it in the training data, with frequencies determining the likelihood of selection.

## Features

- **Text Training**: Train the model on any text input
- **Message Generation**: Generate text based on prompts with adjustable "talkativeness"
- **Web Interface**: Modern, responsive web UI with real-time interaction
- **Command Line Interface**: Traditional CLI for direct interaction
- **Energy/Talkativeness Control**: Adjust output length from 0 (short) to 9 (verbose)

## Project Structure

```
proto-llm/
├── main.py           # Core ProtoLLM class and CLI interface
├── app.py            # FastAPI web application
├── index.html        # Web interface HTML
├── styles.css        # Custom styling for the web UI
├── script.js         # Frontend JavaScript functionality
└── README.md         # This file
```

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn
```

## Usage

### Web Interface

1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

2. Open your browser and navigate to `http://localhost:8000`

3. Use the web interface to:
   - **Train the LLM**: Enter text in the training section and click "Train LLM"
   - **Generate Messages**: Enter a prompt, adjust talkativeness (0-9), and click "Generate Message"

### Command Line Interface

Run the CLI version directly:

```bash
python main.py
```

Follow the prompts to:
1. Train on text files
2. Generate messages with custom energy levels
3. Exit the program

## How It Works

### Training Process

The Proto-LLM builds a word map during training:
- Each word is mapped to words that follow it in the training text
- Frequencies are tracked for each word pair
- A "Grand Total" count enables weighted random selection

### Text Generation

Generation uses a Markov chain approach:
1. Start with the input prompt words
2. For each word, probabilistically select the next word based on training data
3. Continue until reaching a sentence ending punctuation
4. Energy level controls the probability of stopping at sentence boundaries

### Energy/Talkativeness Levels

- **0-2**: Very brief responses, stops quickly at sentence endings
- **3-5**: Moderate length responses
- **6-8**: Longer, more elaborate responses
- **9**: Maximum verbosity, rarely stops at sentence endings

## API Endpoints

### Web Interface
- `GET /` - Serves the main HTML interface
- `GET /styles.css` - Serves CSS styling
- `GET /script.js` - Serves JavaScript functionality

### API
- `POST /train` - Train the model with text data
  - Body: `{"text": "your training text here"}`
- `GET /gen_message` - Generate a message
  - Query params: `message` (required), `energy` (optional, default 0.8)

## Example Usage

### Training Example
```python
llm = ProtoLLM()
llm.train("The quick brown fox jumps over the lazy dog. The dog was sleeping.")
```

### Generation Example
```python
response = llm.gen_message("The quick", energy=0.8)
print(response)  # Might output: "The quick brown fox jumps over the lazy dog."
```

## Web Interface Features

- **Modern Design**: Clean, responsive interface with Tailwind CSS
- **Real-time Feedback**: Status updates during training and generation
- **Interactive Controls**: Slider for energy adjustment with live preview
- **Error Handling**: Clear error messages for network issues or invalid inputs
- **Responsive Layout**: Works on desktop and mobile devices

## Limitations

- **Simple Model**: Uses basic Markov chains, not neural networks
- **Memory Storage**: No persistent storage between sessions
- **Limited Context**: Only considers immediate word predecessors
- **No Semantic Understanding**: Purely statistical word relationships

## Development

### Running in Development Mode

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### File Structure Details

- **main.py**: Core ProtoLLM class with training and generation logic
- **app.py**: FastAPI application with REST endpoints
- **index.html**: Single-page web interface with two main sections
- **styles.css**: Custom styling for range sliders and fonts
- **script.js**: Client-side JavaScript for API communication

## License

This project is provided as-is for educational and demonstration purposes.

## Contributing

This is a prototype project. Feel free to fork and modify for your own learning purposes.

## Future Enhancements

- Persistent model storage
- Better text preprocessing
- N-gram support (beyond single words)
- Model export/import functionality
- Advanced text generation parameters

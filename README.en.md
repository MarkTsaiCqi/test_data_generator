# Test Data Generator

This is a Python toolset for generating test data, capable of creating various types of test files including images, audio, and text.

## Features

- Image Generation
  - Random color images
  - Gradient images
  - Support for multiple formats (PNG, JPEG, BMP, etc.)

- Audio Generation
  - Sine wave audio
  - White noise
  - WAV format support

- Text Generation
  - Random articles
  - Name lists
  - Address lists
  - Multi-language support

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Generate all test data:
```bash
python main.py
```

2. Generate specific types of test data:
```bash
# Generate images
python image/generator.py

# Generate audio
python audio/generator.py

# Generate text
python text/generator.py
```

## Output Directories

Generated test files will be saved in the following directories:
- Images: `generated_images/`
- Audio: `generated_audio/`
- Text: `generated_text/`

## Notes

- Generated test data is for testing purposes only
- Audio generation requires additional system dependencies (e.g., ffmpeg)
- Text generation supports multiple languages, which can be switched by modifying the Faker locale parameter 
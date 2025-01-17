---
title: Expressly
emoji: 📉
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
short_description: Expressly - Text Transformation App
---

Checkout the Hugging Face Spaces [here](https://huggingface.co/spaces/DeepakPant93/expressly)

# Expressly - Text Transformation App Web UI

This document provides an overview of the web UI for the Expressly - Text Transformation App, which is built using Gradio to provide an interactive and user-friendly experience.

## Key Features

### Intuitive User Interface

The web UI allows users to interact seamlessly with the backend to transform text based on their preferences. The interface includes options to specify:

- **Format**: Define the type of content (e.g., post, email, blog, etc.).
- **Tone**: Set the desired communication style (e.g., professional, casual, inspirational, etc.).
- **Target Audience**: Tailor content for specific platforms or audiences (e.g., LinkedIn post, marketing email, etc.).

For a detailed list of supported formats, tones, and target audiences, refer to the [Expressly Wiki](https://github.com/DeepakPant93/expressly/wiki).

### Real-Time Output

Users can input their text and immediately receive a transformed version based on their selected preferences. The output is displayed in real-time and can be easily copied for use.

## Prerequisites

1. Ensure you have Python installed on your system.
2. Install Gradio if not already installed:
   ```bash
   pip install gradio
   ```

## Running the Web UI

To start the web interface:

1. Navigate to the `web` folder of the Expressly project.
2. Run the following command:
   ```bash
   python app.py
   ```
3. Open the provided local URL in your browser to access the UI.

## Customization

1. **Modify the UI Layout**:
   - Edit `app.py` to change the layout or styling of the Gradio interface.
2. **Integrate Additional Features**:
   - Add new options or inputs in `app.py` to expand the functionality of the web UI.
3. **Connect with Backend**:
   - Ensure the backend API endpoints are correctly configured in the `app.py` file to handle user inputs and return responses.

## Folder Structure

```
/web
├── app.py               # Main Gradio application file
└── README.md            # Documentation for the web UI
```


- For advanced customizations or troubleshooting, refer to the Gradio documentation: [https://gradio.app/](https://gradio.app/).

This web UI serves as the front-end interface for the Expressly - Text Transformation App, providing users with an easy and efficient way to transform text based on their needs.

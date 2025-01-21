

# Weather App - Cameroon

## Overview
The Weather App is a Python-based desktop application built using Tkinter that provides current weather data and future weather predictions for various regions in Cameroon. It fetches weather information from the [wttr.in API](https://wttr.in) and displays it in an interactive and user-friendly GUI.

## Features
- Fetch and display current weather data such as condition, temperature, pressure, wind speed, and predictions for morning, afternoon, and evening.
- View weather icons representing the current condition.
- Display future weather predictions for the selected region.
- Responsive and easy-to-use graphical interface using Tkinter.

## Problem Statement
Provide real-time weather information and predictions for different regions in Cameroon to help users stay updated on the weather conditions.

## Approach

1. **Data Fetching**: 
   - Used the wttr.in API to fetch current weather data and predictions based on the region selected by the user.
   - The app fetches weather data and displays it dynamically on the GUI.

2. **GUI Setup**:
   - Designed the GUI using Tkinter with dropdown menus, labels, buttons, and a weather icon display.
   - Weather data such as temperature, wind speed, pressure, and predictions are shown in the form of labels on the interface.

3. **Error Handling**:
   - Included error handling for API request failures and missing region input.

4. **Future Predictions**:
   - A feature to fetch and display weather predictions for the selected region.

## Installation and Setup

### Prerequisites
- Python 3.x
- Tkinter (typically included with Python)
- Pillow (for image processing)
- Requests (for HTTP requests)

### Install Dependencies

You can install the required libraries using `pip`:

```bash
pip install pillow requests
```

### Running the Code
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Run the application:
   ```bash
   python weather_app.py
   ```

## Usage
1. **Select a Region**: Choose a region from the dropdown list (e.g., Northwest, Littoral, etc.).
2. **Get Weather**: Click the "Get Weather" button to fetch and display the current weather data for the selected region.
3. **Get Predictions**: Click the "Get Predictions" button to fetch and display future weather predictions.

## Screenshot
![Weather App Screenshot](screenshots/weather_app_screenshot.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits
- Weather data provided by [wttr.in](https://wttr.in).
- Powered by Tkinter, Pillow, and Requests libraries.

---

Feel free to adjust any sections or add any additional information specific to your setup or repository.

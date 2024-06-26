# Weather Forecast Django Project

This is a Django project for creating a weather forecast application. Follow the instructions below to get started.

## Prerequisites

- Python 3.x installed on your system
- Pip package manager

## Installation

1. Clone the repository to your local machine:

  ```shell
  git clone https://github.com/ahabalikhan/weather-forecast-django.git
  ```

2. Navigate to the project directory:

  ```shell
  cd weather-forecast-django
  ```

3. Create a virtual environment:

  ```shell
  python -m venv venv
  ```

4. Activate the virtual environment:

  - For Windows:

    ```shell
    venv\Scripts\activate
    ```

  - For macOS/Linux:

    ```shell
    source venv/bin/activate
    ```

5. Install the project dependencies:

  ```shell
  pip install -r requirements.txt
  ```

6. Create a `.env` file in the project root directory and add the following environment variables:

  ```plaintext
  OPEN_WEATHER_API_KEY=your_weather_api_key
  ```

  Replace `your_weather_api_key` with your actual API key for accessing the weather forecast data.

## Usage

To start the Django development server, run the following command:

```shell
python manage.py runserver
```

You can now access the application by visiting `http://localhost:8000/map/` in your web browser.

The main API consumed in this project is `http://localhost:8000/weather/`

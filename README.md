python -m venv venv
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\activate     # On Windows

Install dependencies:

pip install -r requirements.txt

Get your OpenWeatherMap API key:

Visit https://openweathermap.org/ and sign up or log in.
Generate an API key from your account.
Replace "API_KEY" in main.py with your actual API key:


Run the FastAPI application:

uvicorn main:app --reload


Use http://127.0.0.1:8000/weather/{city} directly.
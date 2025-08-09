# Setup Instructions

1. Clone the repository or download the ZIP package.
2. Install Python 3.8+.
3. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Configure environment variables for your API tokens and URLs.
6. Run the FastAPI app:
   ```
   uvicorn api.main:app --reload
   ```
7. Access API documentation at http://localhost:8000/docs
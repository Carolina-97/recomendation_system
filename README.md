# Recommendation System

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

5. Access the services:
   - Generator: `http://localhost:8001/generate/`
   - Invoker: `http://localhost:8002/recommend/`

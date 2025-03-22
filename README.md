# Risk-Analysis-with-Langchain
A full stack system for risk analysis of companies across several years using Langchain framework

# Risk Analysis with Langchain

This project uses Langchain for risk analysis.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/risk-analysis-with-langchain.git
   cd risk-analysis-with-langchain

2. Create a virtual Environment and activate it
  ```sh
  python -m venv .venv
  .venv\Scripts\activate  # On Windows
  source .venv/bin/activate  # On macOS/Linux
  ```

3. Install Dependencies
  ```sh
  pip install -r requirements.txt
  ```

4. Create a .env file and add your API keys
```sh
echo "OPENAI_API_KEY=your-api-key" > .env
```

5. Run the application
```sh
docker-compose up --build
```
6. Stopping the container

```sh
docker-compose stop

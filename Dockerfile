# Use official Playwright image (browsers already installed)
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Set working directory
WORKDIR /app

# Copy requirements first (Docker caching optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy complete project
COPY . .

# Install Playwright browsers (safety step)
RUN playwright install

# Create folders for reports if not present
RUN mkdir -p reports/allure-results screenshots logs

# Run tests
CMD ["pytest", "-v", "--alluredir=reports/allure-results"]
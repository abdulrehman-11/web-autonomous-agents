# Web Autonomous Agents - Automated Testing with Playwright

This project contains automated test cases for the website [video-converter.com](https://video-converter.com/) using Playwright. The test suite includes both positive and negative use cases to validate video conversion functionality and ensure proper handling of edge cases.

---

## Features

- **Automated Test Cases**:
  - **Positive Test**: Upload an `.mp4` file smaller than 4GB and convert it to `.avi` format with the lowest HD quality.
  - **Negative Test 1**: Attempt to upload a YouTube video URL and verify the error handling.
  - **Negative Test 2**: Attempt to upload a file larger than 4GB and ensure the system responds with the appropriate error message.
  
- **Tools Used**:
  - [Playwright](https://playwright.dev/) for browser automation.
  - [Pytest](https://docs.pytest.org/) for test orchestration.

---

## Installation

### Prerequisites

1. Python 3.7 or higher.
2. Node.js for Playwright dependencies.
3. Playwright installed via Python.

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:abdulrehman-11/web-autonomous-agents.git
   cd web-autonomous-agents
   ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate 
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Install Playwright and its browsers:
    ```bash
    playwright install
    ```

# Usage
Running Tests
To run all test cases:
    ```bash
    pytest tests/
    ```
To run a specific test:
    ```bash
    pytest tests/test_negative_case_youtube.py
    ```
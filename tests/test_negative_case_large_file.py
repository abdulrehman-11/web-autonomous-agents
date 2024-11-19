import pytest
from playwright.sync_api import sync_playwright

def test_large_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the video converter site
        page.goto("https://video-converter.com/")

        # Upload a file larger than 4GB
        page.set_input_files("input[type='file']", "assets/large_video.mp4")

        # Validate error message
        error_message = page.text_content("#error-message")  # Adjust selector
        assert "File size exceeds the 4GB limit" in error_message

        browser.close()

import pytest
from playwright.sync_api import sync_playwright

def test_youtube_url_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the video converter site
        page.goto("https://video-converter.com/")

        # Attempt to upload a YouTube URL
        page.fill("#open_link", "https://www.youtube.com/watch?v=aWk2XZ_8IhA")  # Adjust selector
        page.click("#converter > a > div > div")  # Adjust selector

        # Validate error message
        error_message = page.text_content("#error-message")  # Adjust selector
        assert "Uploading URLs is not allowed" in error_message

        browser.close()

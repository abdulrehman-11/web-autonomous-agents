import pytest
from playwright.sync_api import sync_playwright

def test_positive_case():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True if you want headless mode
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the video converter site
        page.goto("https://video-converter.com/")

        # Upload a valid MP4 file
        page.set_input_files("input[type='file']", "assets/small_video.mp4")

        # Select AVI as the output format (Adjust selector as per the website)
        page.select_option("#output-format", "avi")

        # Select lowest HD quality (Adjust selector)
        page.select_option("#preset_dropdown", "low_hd")

        # Click the convert button
        page.click("#convert-button")

        # Wait for the conversion to complete
        page.wait_for_selector("#success-message")  # Adjust selector

        # Validate success message
        success_message = page.text_content("#success-message")
        assert "Conversion successful" in success_message

        browser.close()

# Spotlight Archive Downloader

## Overview

Spotlight Archive Downloader is a Python script designed to download images from a specified archive (e.g., Windows Spotlight). The script utilizes Playwright for web automation to navigate through the archive pages and fetch images along with associated metadata.

## Requirements

- Python (version 3.11)
- Playwright library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Spotlight-Archive-Downloader.git
    ```

2. Install the necessary dependencies:

    ```bash
    pip install playwright
    ```

3. Update the script with your preferred start and stop page numbers, file paths, etc., in the `Spotlight_Archive_Downloader.py` file.

## Usage

1. Run the Python script:

    ```bash
    python3 Spotlight_Archive_Downloader.py
    ```

2. The script will launch a browser instance, navigate through the specified pages of the archive, and download images to the specified directory.

## Configuration

- **start_page**: The starting page number to begin downloading images.
- **stop_page**: The last page number until which the script will download images. If set to `None`, it will download the entire set or update the current set.
- **json_file_path**: Path to the JSON file storing metadata information.

## Notes

- Ensure proper network connectivity for the script to access the archive.
- The script utilizes Playwright to interact with the archive site. Adjustments might be needed based on site changes or updates.

## License

The content in this repository is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

This means you are free to:
- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material.

Under the following terms:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You should not imply endorsement by the licensor.
- NonCommercial: You may not use the material for commercial purposes.

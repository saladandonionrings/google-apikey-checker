# GOOGLE API KEY CHECKER 🌐🔑

A simple yet powerful tool to verify the validity of Google API keys, specifically designed for Google Maps API.

## Features ✨

- Validates Google Maps API keys.
- Provides detailed response information for valid API keys, including formatted address and location coordinates.
- Identifies and informs about invalid or problematic API keys with clear messages.
- Simple command-line interface for ease of use.

## Requirements 📋

- Python 3.x
- `requests` library
- `termcolor` library

Ensure you have the above requirements installed. You can install the necessary libraries using pip:

```bash
pip install requests termcolor
```

## Installation 🚀

To use the GOOGLE API KEY CHECKER, follow these steps:

```bash
git clone https://github.com/saladandonionrings/google-apikey-checker.git
cd google-apikey-checker

python3 google-api-check.py <your_api_key>
```

## Output 📌

The script will provide one of the following outputs based on the validity of the API key:

- 🟢 For valid API keys: A success message with the formatted address and location coordinates.
- 🔴 For invalid API keys: An error message stating that the API key is invalid.
- 🟡 If the request does not return any results: A warning message.

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 🙏

- This script is for educational and testing purposes only. Always ensure you have permission to use and test API keys accordingly.
- Google Maps API is a trademark of Google Inc.

# Auto Download with Selenium

This project is a Python-based automation script using Selenium to interact with the [Veed.io](https://www.veed.io/) video editing platform. It automates the process of creating videos, exporting them, and downloading the final output. The script is designed to handle repetitive tasks efficiently, saving time and effort.

---

## Features

- **Automatic Login Detection:** Waits until the user is logged in before proceeding.
- **Dynamic Input Handling:** Reads a list of video subjects from a text file and processes each subject.
- **AI Video Generation:** Utilizes Veed.io's AI-powered video creation tool.
- **Export and Download:** Automatically publishes, exports, and downloads videos in MP4 format.
- **User-Agent and Bot Detection Evasion:** Configured to minimize bot detection by modifying browser properties.

---

## Installation

### Prerequisites
- Python 3.7+
- Google Chrome browser
- ChromeDriver

### Install Required Python Libraries

```bash
pip install selenium webdriver-manager
```

---

## Setup

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Prepare the Input File**
   Create a file named `listofvideos.txt` in the project directory. Add each video subject on a new line. Example:
   ```
   Video Subject 1
   Video Subject 2
   Video Subject 3
   ```

3. **Run the Script**
   ```bash
   python auto_download.py
   ```

---

## How It Works

1. **Initialization:**
   - Sets up the ChromeDriver with options to avoid detection.
   - Prepares browser preferences for file download and sets a custom user-agent.

2. **Login Detection:**
   - Waits for the user to log in to Veed.io.

3. **Video Creation:**
   - For each subject in `listofvideos.txt`, navigates to the video creation workspace.
   - Uses Veed.io's AI tools to generate videos based on the subject.

4. **Publishing and Exporting:**
   - Publishes the generated video.
   - Exports the video in MP4 format.

5. **Downloading:**
   - Automatically downloads the exported MP4 file to the `Videos` folder in the current directory.

---

## Code Structure

- **`auto_download.py`:** Main script containing all automation logic.
- **`listofvideos.txt`:** Input file containing video subjects to process.

---

## Key Functions

### `getlist()`
Reads and returns the list of video subjects from `listofvideos.txt`.

### `Auto_Download` Class
Handles all automation steps:
- **`__init__`:** Initializes the ChromeDriver with specified options.
- **`StartAndWait`:** Waits for login and processes the video subjects.
- **`ClickToXpath`:** Clicks an element located by its XPath.
- **`Create_Video`:** Automates the video creation, publishing, and downloading process.
- **`ext`:** Quits the browser session.

---

## Customization
- Update the Veed.io workspace ID in the `Create_Video` function if necessary.
- Modify browser options and preferences in the `__init__` method to suit your needs.

---

## Troubleshooting

### Common Issues

1. **Login Detection Fails:**
   Ensure the browser window is open and logged into Veed.io. The script waits for a specific URL pattern (`"workspaces"`) to verify login.

2. **Element Not Found Errors:**
   - Verify that the XPath selectors in the script match the current Veed.io DOM structure.
   - Update XPath selectors if Veed.io's website structure changes.

3. **Download Location Issues:**
   - Ensure the `Videos` folder exists in the project directory.
   - Check ChromeDriver permissions for file downloads.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [Veed.io](https://www.veed.io/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)



----------------


## Updates

### January 11, 2025

- Significant improvements have been made to the `ClickToXpath` function in the `Auto_Video_Creator.py` file.  
  - A retry mechanism has been added to handle cases where the target button is not immediately found.  
  - If the button is not located, the function will attempt to find and click it at regular intervals, improving reliability.  
  - This update has drastically enhanced the function's timing performance, making it nearly **5 times faster** in handling dynamic delays during the button loading process.


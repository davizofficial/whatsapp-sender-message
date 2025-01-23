# WhatsApp Message Sender Script

This repository contains a Python script to send automated WhatsApp messages to multiple recipients using the `pywhatkit` library. The script ensures smooth execution with controlled timing and provides customization options for messages and recipient lists.

## Features
- Send WhatsApp messages to multiple recipients with specified delays.
- Automatically calculates the next delivery time based on the current time.
- Closes the WhatsApp Web tab after sending messages to maintain a clean browsing experience.

## Prerequisites
1. **Python version**: Python 3.7 or higher.
2. **Required libraries**:
   - `pywhatkit`
   - `pyautogui`
   - `datetime` (built-in module)
   - `time` (built-in module)

Install the necessary libraries:
```bash
pip install pywhatkit pyautogui
```

## How to Use

### General Steps
1. **Ensure WhatsApp Web is active**: Open WhatsApp Web on your browser and ensure you're logged in.
2. **Install dependencies**:
   Run the following command to install the required Python libraries:
   ```bash
   pip install pywhatkit pyautogui
   ```
3. **Clone this repository**:
   ```bash
   git clone https://github.com/davizofficial/whatsapp-sender-message.git
   cd whatsapp-sender-message
   ```
4. **Edit the script**:
   - Add your recipient numbers in the `daftar_nomor` list using the international format (e.g., `+6281234567890`).
   - Customize the `pesan` variable with your desired message.
5. **Run the script**:
   ```bash
   python sendwa.py
   ```

---

### Step-by-Step Guide for Windows Users
1. Download and install Python from [python.org](https://www.python.org/) and add it to the system's PATH during installation.
2. Open the Command Prompt and install the required libraries:
   ```bash
   pip install pywhatkit pyautogui
   ```
3. Clone the repository using Git (install Git for Windows if necessary):
   ```bash
   git clone https://github.com/davizofficial/whatsapp-sender-message.git
   cd whatsapp-sender-message
   ```
4. Ensure WhatsApp Web is open in your browser and logged in.
5. Run the script:
   ```bash
   python sendwa.py
   ```

---

### Step-by-Step Guide for Linux Users
1. Install Python 3 and Git if not already installed:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```
2. Install the required Python libraries:
   ```bash
   pip install pywhatkit pyautogui
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/davizofficial/whatsapp-sender-message.git
   cd whatsapp-sender-message
   ```
4. Open WhatsApp Web in your browser and log in.
5. Run the script:
   ```bash
   python3 sendwa.py
   ```

---

## Script Overview
The script sends a WhatsApp message to each recipient in the list with a delay of 20 seconds between messages. Key components include:
- **Function `kirim_pesan`**:
  Sends a WhatsApp message to a specific number at a designated time and closes the WhatsApp Web tab after delivery.
- **Time Calculation**:
  Automatically schedules message-sending times starting 1 minute from the current time, with a 20-second delay for subsequent messages.

## Notes
- Ensure the numbers are registered on WhatsApp.
- This script includes delays to adhere to WhatsApp's anti-spam policies.
- Test the script with a small number of recipients before using it at scale.

## Disclaimer
This script is for educational and personal use only. The author is not responsible for any misuse or violations of WhatsApp's terms of service.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

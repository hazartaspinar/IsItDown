Already Down! - Server Availability Testing Tool

📌 Introduction

Already Down! is a powerful tool designed to continuously monitor the availability of a target server using multiple testing methods. This tool checks whether a server is down by performing:

HTTP Status Checks (Checks HTTP response codes)

ICMP Ping Tests (Checks network availability via ICMP)

TCP Connection Tests (Checks port connectivity)

If all three methods fail, the tool congratulates you for successfully bringing the server down! 🎉

🚀 Features

Live status updates using the Rich library

Continuous testing with real-time results

Interactive mode for ease of use

ASCII banner for aesthetics 😎

🛠️ Installation

To use Already Down!, ensure you have Python installed on your system. Then, follow these steps:

# Clone the repository
git clone https://github.com/yourusername/already-down.git
cd already-down

# Install required dependencies
pip install -r requirements.txt

▶️ Usage

Run the script in interactive mode:

python already_down.py

You will be prompted to enter a target URL and a TCP port. The tool will then continuously test the server's availability.

Example

Enter the target domain or IP (default: https://example.com): https://target.com
Enter the TCP port to check (default: 443): 80

⚡ Live Monitoring Example

The tool displays a live results table:

┌───────────────────┬──────────┬───────────────────┐
│       Test       │  Result  │      Details      │
├───────────────────┼──────────┼───────────────────┤
│   HTTP Test      │ Success  │ 200 OK            │
│   ICMP Ping Test │ Failed   │                   │
│   TCP Connection │ Failed   │                   │
└───────────────────┴──────────┴───────────────────┘

If all tests fail, the message "Target is already down! Congratulations! 🎉" will appear.

📜 License

This project is licensed under the MIT License. You are free to modify and distribute it.

🤝 Contributing

Pull requests are welcome! Feel free to submit improvements or report issues.

📧 Contact

For any inquiries or suggestions, contact me at your.email@example.com or open an issue on GitHub

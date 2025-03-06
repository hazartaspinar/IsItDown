# README içeriğini bir dosya olarak kaydetme
readme_content = """# Already Down! - Server Availability Testing Tool

## 📌 Introduction
**Already Down!** is a powerful tool designed to continuously monitor the availability of a target server using multiple testing methods. This tool checks whether a server is down by performing:

- **HTTP Status Checks** (Checks HTTP response codes)
- **ICMP Ping Tests** (Checks network availability via ICMP)
- **TCP Connection Tests** (Checks port connectivity)

If all three methods fail, the tool congratulates you for successfully bringing the server down! 🎉

## 🚀 Features
- Live status updates using the **Rich** library
- Continuous testing with real-time results
- Interactive mode for ease of use
- ASCII banner for aesthetics 😎

## 🛠️ Installation
To use **Already Down!**, ensure you have Python installed on your system. Then, follow these steps:

```sh
# Clone the repository
git clone https://github.com/yourusername/already-down.git
cd already-down

# Install required dependencies
pip install -r requirements.txt

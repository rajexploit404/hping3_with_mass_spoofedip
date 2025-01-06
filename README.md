# RAJTCP - SYN Flood Tool

RAJTCP is a SYN flood tool designed for educational purposes only. It allows for testing TCP SYN flood attacks using **hping3** with mass spoofed IP addresses.

### DISCLAIMER
**RAJTCP** is intended for educational use only. Do not use this tool to perform attacks on networks, servers, or any system that you do not own or have explicit permission to test. Unauthorized use is illegal and unethical. Please make sure to comply with all laws and regulations.

## Features
- Sends SYN flood packets using **hping3**.
- Supports spoofing IP addresses for each packet.
- Multi-threaded approach to speed up the attack.

## Dependencies
To run this tool, you need to install the following dependencies:
- **Python 3.x**: This script is written in Python 3.
- **hping3**: A network tool used for crafting and sending custom packets.
  - You can install it using the command:  
    `sudo apt-get install hping3` (on Debian-based Linux systems).
- **Linux** (or a system with equivalent network capabilities): Required for sending raw packets and using **hping3**.

## Usage

1. Clone this repository or download the `main.py` script.
2. Ensure that you have installed the required dependencies.
3. Prepare a file containing a list of spoofed IP addresses. Each line should contain a single IP address.
4. Run the script using the following command:

   ```bash
   sudo python3 main.py
   ```

5. When prompted, enter the following:
   - **Target IP**: The IP address of the target server.
   - **Target port**: The port to target with the SYN flood.
   - **Spoofed IP list file**: Path to the file containing spoofed IP addresses (one per line).

6. The tool will start flooding the target with SYN packets from spoofed IP addresses.

### Example:
```bash
┌──(root㉿rajsec)-[~/hping3_with_mass_spoofedip]
└─# python3 main.py

██████╗  █████╗      ████████╗ ██████╗██████╗  ██████╗
██╔══██╗██╔══██╗     ╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗
██║  ██║███████║        ██║   ██║     ██████╔╝██║   ██║
██║  ██║██╔══██║        ██║   ██║     ██╔═══╝ ██║   ██║
██████╔╝██║  ██║        ██║   ╚██████╗██║     ╚██████╔╝
╚═════╝ ╚═╝  ╚═╝        ╚═╝    ╚═════╝╚═╝      ╚═════╝ 
                  SYN Flood Tool - RAJTCP
    
Enter target IP: 1.1.1.1
Enter target port: 12
Enter spoofed IP list file: spoof.txt
```

### How it works:
1. **RAJTCP** reads a list of spoofed IP addresses from the file.
2. The script generates SYN packets and floods the target server using **hping3**.
3. The **--flood** option ensures a continuous stream of SYN packets.
4. The **-S** option sends SYN packets to the target.
5. The **-a** option is used to spoof the source IP address (i.e., the list of spoofed IPs you provide).
6. The tool uses multi-threading to speed up the attack process.

### Stopping the Attack:
You can stop the attack by pressing **CTRL+C** (or **CTRL+Z**) during execution. The program will cleanly terminate all running processes.

## Important Notes:
- **RAJTCP** should only be used in a controlled environment where you have explicit permission to perform testing.
- **hping3** is a powerful tool and can be used for legitimate network testing, but it can also be misused for attacks. Use responsibly.
- This tool **does not** bypass firewalls or other security measures. It is designed to demonstrate how SYN flood attacks work and for educational purposes.

---

### Credits:
- **hping3**: Tool for crafting and sending network packets.
---



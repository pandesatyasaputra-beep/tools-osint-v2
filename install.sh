#!/bin/bash
# =====================================
#  🔍 OSINT TOOL INSTALLER
#  Compatible: Kali Linux & Termux
# =====================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}====================================="
echo -e "   🔍 OSINT TOOL INSTALLER"
echo -e "=====================================${NC}"

# Detect platform
if [ -d "/data/data/com.termux" ]; then
    echo -e "${GREEN}[+] Detected: Termux (Android)${NC}"
    echo -e "${YELLOW}[+] Updating packages...${NC}"
    pkg update -y
    echo -e "${YELLOW}[+] Installing Python and tools...${NC}"
    pkg install -y python python-pip git
else
    echo -e "${GREEN}[+] Detected: Linux Distribution${NC}"
    echo -e "${YELLOW}[+] Updating packages...${NC}"
    sudo apt update -y
    echo -e "${YELLOW}[+] Installing Python and tools...${NC}"
    sudo apt install -y python3 python3-pip git
fi

echo -e "${YELLOW}[+] Installing Python modules...${NC}"
pip install --upgrade pip
pip install requests phonenumbers colorama

# whois package - try python-whois on Debian/Kali, or pip
echo -e "${YELLOW}[+] Installing whois module...${NC}"
if [ -d "/data/data/com.termux" ]; then
    pip install python-whois
else
    # Try apt first (Debian/Kali has python3-whois)
    sudo apt install -y python3-whois 2>/dev/null || pip install python-whois
fi

echo ""
echo -e "${CYAN}====================================="
echo -e "   ✅ INSTALLATION COMPLETE!"
echo -e "=====================================${NC}"
echo ""
echo -e "${GREEN}[+] To run the tool:${NC}"
echo -e "    python3 osint_tool.py"
echo ""
echo -e "${RED}[!] Legal Disclaimer:${NC}"
echo -e "    This tool is for educational and"
echo -e "    authorized testing purposes only."
echo -e "${CYAN}=====================================${NC}"

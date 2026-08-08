#!/usr/bin/env python3
"""
=====================================
      🔍 OSINT TOOL v1.1 🔍
=====================================
  Open Source Intelligence Tool
  Compatible: Kali Linux & Termux
=====================================
"""

import os
import sys
import re
import socket
import subprocess
import platform
from datetime import datetime

# =====================================
#  COLORAMA - IMPORT AT TOP LEVEL
#  (agar Fore tersedia di seluruh file)
# =====================================
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA_OK = True
except ImportError:
    # Fallback jika colorama belum terinstall
    class _Dummy:
        def __getattr__(self, name):
            return ''
    Fore = _Dummy()
    Style = _Dummy()
    COLORAMA_OK = False

# =====================================
#  AUTO-INSTALL DEPENDENCIES
# =====================================
def install_dependencies():
    """Check and install required libraries automatically"""
    global requests, phonenumbers, carrier, geocoder, timezone, whois_module

    required = {
        'requests': 'requests',
        'phonenumbers': 'phonenumbers',
        'colorama': 'colorama',
        'whois': 'python-whois',
    }

    for module, package in required.items():
        try:
            __import__(module)
            print(f"{Fore.GREEN}[✔] {module} already installed")
        except ImportError:
            print(f"{Fore.YELLOW}[!] Installing {package}...")
            try:
                result = subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', package],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    print(f"{Fore.GREEN}[✔] {package} installed successfully")
                else:
                    print(f"{Fore.RED}[✘] Failed to install {package}: {result.stderr[-200:]}")
            except Exception as e:
                print(f"{Fore.RED}[✘] Error installing {package}: {e}")

    # Import setelah install
    import requests
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
    import whois as whois_module
    return True

# =====================================
#  ART & BANNER
# =====================================
BANNER = r"""
    ____  _____ _____ ___ _____ 
   / __ \|  _  |_   _|_ _|_   _|
  / / _` | | | | | |  | |  | |  
 | | (_| | |_| | | |  | |  | |  
  \ \__,_\___/  |_| |___| |_|  
   \____/                      
    OSINT TOOL - Kali Linux & Termux
    Open Source Intelligence Tool
"""

def clear_screen():
    """Clear terminal screen (cross-platform)"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_banner():
    """Display the banner"""
    print(f"{Fore.CYAN}{BANNER}")
    print(f"{Fore.GREEN}[System] : {platform.system()} {platform.machine()}")
    print(f"{Fore.GREEN}[Python] : {sys.version.split()[0]}")
    print(f"{Fore.GREEN}[Time]   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.YELLOW}===============================================")

# =====================================
#  MODULE 1: PHONE NUMBER LOOKUP
# =====================================
def phone_lookup():
    """Phone number information lookup"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      📱 PHONE NUMBER LOOKUP")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    number = input(f"{Fore.YELLOW}[?] Enter phone number (with country code, e.g. +628123456789): ").strip()

    try:
        parsed = phonenumbers.parse(number, None)

        print(f"\n{Fore.GREEN}[+] Phone Number    : {parsed.national_number}")
        print(f"{Fore.GREEN}[+] Country Code     : +{parsed.country_code}")
        print(f"{Fore.GREEN}[+] Country          : {geocoder.description_for_number(parsed, 'en')}")
        print(f"{Fore.GREEN}[+] Carrier          : {carrier.name_for_number(parsed, 'en')}")
        print(f"{Fore.GREEN}[+] Timezone         : {timezone.time_zones_for_number(parsed)}")
        print(f"{Fore.GREEN}[+] Valid number     : {phonenumbers.is_valid_number(parsed)}")
        print(f"{Fore.GREEN}[+] Possible number  : {phonenumbers.is_possible_number(parsed)}")
        print(f"{Fore.GREEN}[+] Number type      : {phonenumbers.number_type(parsed)}")

        if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE:
            print(f"{Fore.MAGENTA}[★] This appears to be a MOBILE number")
        elif phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f"{Fore.MAGENTA}[★] This appears to be a LANDLINE number")

    except phonenumbers.NumberParseException:
        print(f"{Fore.RED}[✘] Invalid phone number format!")
    except Exception as e:
        print(f"{Fore.RED}[✘] Error: {e}")

# =====================================
#  MODULE 2: IP ADDRESS LOOKUP
# =====================================
def ip_lookup():
    """IP address information lookup"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      🌐 IP ADDRESS LOOKUP")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    ip = input(f"{Fore.YELLOW}[?] Enter IP address (or 'me' for your IP): ").strip()

    try:
        if ip.lower() == 'me':
            response = requests.get('https://api.ipify.org', timeout=10)
            ip = response.text
            print(f"{Fore.GREEN}[+] Your Public IP: {ip}")
        else:
            socket.inet_aton(ip)

        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=15)
        data = response.json()

        if data.get('status') == 'success':
            print(f"\n{Fore.GREEN}[+] IP Address      : {data['query']}")
            print(f"{Fore.GREEN}[+] Country         : {data.get('country', 'N/A')}")
            print(f"{Fore.GREEN}[+] Region          : {data.get('regionName', 'N/A')}")
            print(f"{Fore.GREEN}[+] City            : {data.get('city', 'N/A')}")
            print(f"{Fore.GREEN}[+] ZIP             : {data.get('zip', 'N/A')}")
            print(f"{Fore.GREEN}[+] Latitude        : {data.get('lat', 'N/A')}")
            print(f"{Fore.GREEN}[+] Longitude       : {data.get('lon', 'N/A')}")
            print(f"{Fore.GREEN}[+] ISP             : {data.get('isp', 'N/A')}")
            print(f"{Fore.GREEN}[+] Organization    : {data.get('org', 'N/A')}")
            print(f"{Fore.GREEN}[+] AS Number       : {data.get('as', 'N/A')}")
            print(f"{Fore.GREEN}[+] Timezone        : {data.get('timezone', 'N/A')}")
        else:
            print(f"{Fore.RED}[✘] Could not retrieve IP information")

    except socket.error:
        print(f"{Fore.RED}[✘] Invalid IP address format!")
    except Exception as e:
        print(f"{Fore.RED}[✘] Error: {e}")

# =====================================
#  MODULE 3: DOMAIN/WHOIS LOOKUP
# =====================================
def domain_lookup():
    """Domain information lookup"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      🌍 DOMAIN / WHOIS LOOKUP")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    domain = input(f"{Fore.YELLOW}[?] Enter domain name (e.g. example.com): ").strip()

    try:
        print(f"\n{Fore.BLUE}[*] Resolving DNS...")
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Fore.GREEN}[+] IP Address      : {ip}")
        except socket.gaierror:
            print(f"{Fore.RED}[✘] Domain could not be resolved")

        print(f"{Fore.BLUE}[*] Querying WHOIS server...")
        w = whois_module.whois(domain)

        print(f"\n{Fore.GREEN}[+] Domain Name     : {w.domain_name}")
        print(f"{Fore.GREEN}[+] Registrar       : {w.registrar}")
        print(f"{Fore.GREEN}[+] Creation Date   : {w.creation_date}")
        print(f"{Fore.GREEN}[+] Expiration Date : {w.expiration_date}")
        print(f"{Fore.GREEN}[+] Updated Date    : {w.updated_date}")
        print(f"{Fore.GREEN}[+] Name Servers    : {w.name_servers}")
        print(f"{Fore.GREEN}[+] Status          : {w.status}")
        print(f"{Fore.GREEN}[+] Organization    : {w.org}")
        print(f"{Fore.GREEN}[+] Country         : {w.country}")

        if w.emails:
            print(f"{Fore.GREEN}[+] Emails          : {w.emails}")

    except Exception as e:
        print(f"{Fore.RED}[✘] Error: {e}")

# =====================================
#  MODULE 4: USERNAME SEARCH
# =====================================
def username_search():
    """Search username across social media platforms"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      👤 USERNAME SEARCH")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    username = input(f"{Fore.YELLOW}[?] Enter username: ").strip()

    platforms = {
        'Instagram': f'https://www.instagram.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Facebook': f'https://www.facebook.com/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}',
        'YouTube': f'https://www.youtube.com/@{username}',
        'GitHub': f'https://github.com/{username}',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'Telegram': f'https://t.me/{username}',
        'Discord': f'https://discord.com/users/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'Pinterest': f'https://www.pinterest.com/{username}',
        'Snapchat': f'https://www.snapchat.com/add/{username}',
        'Twitch': f'https://www.twitch.tv/{username}',
        'Steam': f'https://steamcommunity.com/id/{username}',
        'Patreon': f'https://www.patreon.com/{username}',
        'Medium': f'https://medium.com/@{username}',
        'Dev.to': f'https://dev.to/{username}',
        'Keybase': f'https://keybase.io/{username}',
        'Vimeo': f'https://vimeo.com/{username}',
        'SoundCloud': f'https://soundcloud.com/{username}',
        'Flickr': f'https://www.flickr.com/people/{username}',
        'Behance': f'https://www.behance.net/{username}',
        'Dribbble': f'https://dribbble.com/{username}',
        'VK': f'https://vk.com/{username}',
        'Tumblr': f'https://{username}.tumblr.com',
        'WordPress': f'https://{username}.wordpress.com',
        'About.me': f'https://about.me/{username}',
        'Gravatar': f'https://en.gravatar.com/{username}',
        'Replit': f'https://replit.com/@{username}',
        'HackerNews': f'https://news.ycombinator.com/user?id={username}',
    }

    print(f"\n{Fore.YELLOW}[*] Searching for '{username}' on {len(platforms)} platforms...")
    print(f"{Fore.YELLOW}[*] This may take a moment...\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    found = []
    not_found = []

    for platform_name, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=8, allow_redirects=True)

            if response.status_code == 200:
                page_text_lower = response.text.lower()
                not_found_phrases = [
                    "page not found", "doesn't exist", "not found",
                    "this page isn't available", "user not found",
                    "couldn't find this page", "page doesn't exist"
                ]

                is_not_found = any(phrase in page_text_lower for phrase in not_found_phrases)

                if not is_not_found:
                    found.append((platform_name, url))
                    print(f"{Fore.GREEN}[✔] {platform_name:<15} → FOUND! {url}")
                else:
                    not_found.append(platform_name)
            else:
                not_found.append(platform_name)
        except requests.exceptions.Timeout:
            not_found.append(platform_name)
        except Exception:
            not_found.append(platform_name)

    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}          SEARCH RESULTS")
    print(f"{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.GREEN}[✔] Found on {len(found)} platforms")
    print(f"{Fore.RED}[✘] Not found on {len(not_found)} platforms")

    if found:
        print(f"\n{Fore.MAGENTA}[★] Profile links found:")
        for platform_name, url in found:
            print(f"{Fore.CYAN}   → {platform_name}: {url}")

# =====================================
#  MODULE 5: EMAIL VALIDATION & RECON
# =====================================
def email_lookup():
    """Email validation and basic recon"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      📧 EMAIL VALIDATION & RECON")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    email = input(f"{Fore.YELLOW}[?] Enter email address: ").strip()

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(email_pattern, email):
        print(f"{Fore.RED}[✘] Invalid email format!")
        return

    print(f"\n{Fore.GREEN}[+] Email Address   : {email}")

    domain = email.split('@')[1]
    print(f"{Fore.GREEN}[+] Domain          : {domain}")

    disposable_domains = [
        'mailinator.com', 'temp-mail.org', 'guerrillamail.com',
        '10minutemail.com', 'yopmail.com', 'throwawaymail.com',
        'tempmail.com', 'fakeinbox.com', 'mintemail.com',
        'sharklasers.com', 'guerrillamail.info', 'maildrop.cc'
    ]

    if domain.lower() in disposable_domains:
        print(f"{Fore.RED}[⚠] WARNING: This looks like a DISPOSABLE email domain!")
    else:
        print(f"{Fore.GREEN}[✔] Domain appears to be a legitimate provider")

    print(f"\n{Fore.BLUE}[*] Checking MX records for {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}[+] Domain resolves to: {ip}")
        print(f"{Fore.GREEN}[+] MX records found - email domain is valid")
    except socket.gaierror:
        print(f"{Fore.RED}[✘] Domain does not resolve - email may be invalid")

    print(f"\n{Fore.BLUE}[*] Checking breach databases...")
    print(f"{Fore.YELLOW}[!] Note: Full breach check requires API key")

    try:
        headers = {'User-Agent': 'OSINT-Tool'}
        response = requests.get(f'https://api.github.com/users/{email.split("@")[0]}',
                              headers=headers, timeout=10)
        print(f"{Fore.GREEN}[+] GitHub username check: {email.split('@')[0]}")
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Could not check breach databases")

# =====================================
#  MODULE 6: DNS ENUMERATION
# =====================================
def dns_enum():
    """DNS enumeration for a domain"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      🔎 DNS ENUMERATION")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    domain = input(f"{Fore.YELLOW}[?] Enter domain name: ").strip()

    subdomains = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1',
        'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig',
        'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin',
        'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old',
        'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta',
        'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki', 'web',
        'media', 'email', 'images', 'img', 'www1', 'intranet', 'portal',
        'video', 'sip', 'dns2', 'api', 'cdn', 'app', 'staging', 'test',
        'vps', 'login', 'host', 'help', 'tools', 'chat', 'backup', 'office'
    ]

    print(f"\n{Fore.GREEN}[*] Domain: {domain}")
    print(f"{Fore.YELLOW}[*] Enumerating {len(subdomains)} common subdomains...\n")

    found_subdomains = []

    for sub in subdomains:
        full_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            print(f"{Fore.GREEN}[✔] {full_domain:<30} → {ip}")
            found_subdomains.append((full_domain, ip))
        except (socket.gaierror, socket.herror):
            pass

    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.GREEN}[✔] Found {len(found_subdomains)} active subdomains")

    if found_subdomains:
        print(f"\n{Fore.MAGENTA}[★] Active subdomains:")
        for sub, ip in found_subdomains:
            print(f"{Fore.CYAN}   → {sub} [{ip}]")

# =====================================
#  MODULE 7: PORT SCANNER (BASIC)
# =====================================
def port_scan():
    """Basic port scanner"""
    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.CYAN}      🚪 PORT SCANNER")
    print(f"{Fore.CYAN}═══════════════════════════════════════")

    target = input(f"{Fore.YELLOW}[?] Enter target IP or domain: ").strip()

    try:
        ip = socket.gethostbyname(target)
        print(f"{Fore.GREEN}[+] Target: {target} ({ip})")
    except socket.gaierror:
        print(f"{Fore.RED}[✘] Could not resolve target!")
        return

    common_ports = {
        21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
        80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'RPC', 139: 'NetBIOS',
        143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
        1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5900: 'VNC', 8080: 'HTTP-Proxy'
    }

    print(f"{Fore.YELLOW}[*] Scanning {len(common_ports)} common ports...\n")

    open_ports = []

    for port, service in common_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{Fore.GREEN}[✔] Port {port:<5} ({service:<10}) → OPEN")
                open_ports.append((port, service))
            sock.close()
        except Exception:
            pass

    print(f"\n{Fore.CYAN}═══════════════════════════════════════")
    print(f"{Fore.GREEN}[✔] Scan complete: {len(open_ports)} open ports found")

    if open_ports:
        print(f"\n{Fore.MAGENTA}[★] Open ports:")
        for port, service in open_ports:
            print(f"{Fore.CYAN}   → Port {port}: {service}")

# =====================================
#  MAIN MENU
# =====================================
def main_menu():
    """Display the main menu"""
    while True:
        clear_screen()
        print_banner()

        print(f"\n{Fore.CYAN}╔══════════════════════════════════════╗")
        print(f"{Fore.CYAN}║        📋 MAIN MENU                 ║")
        print(f"{Fore.CYAN}╠══════════════════════════════════════╣")
        print(f"{Fore.CYAN}║                                      ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[1]{Fore.CYAN} 📱 Phone Lookup              ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[2]{Fore.CYAN} 🌐 IP Address Lookup         ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[3]{Fore.CYAN} 🌍 Domain / Whois Lookup      ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[4]{Fore.CYAN} 👤 Username Search           ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[5]{Fore.CYAN} 📧 Email Recon               ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[6]{Fore.CYAN} 🔎 DNS Enumeration            ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[7]{Fore.CYAN} 🚪 Port Scanner              ║")
        print(f"{Fore.CYAN}║  {Fore.WHITE}[0]{Fore.CYAN} 🚪 Exit                       ║")
        print(f"{Fore.CYAN}║                                      ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════╝")

        try:
            choice = input(f"\n{Fore.YELLOW}[?] Select option [0-7]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{Fore.RED}[!] Exiting...")
            sys.exit(0)

        if choice == '1':
            phone_lookup()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            domain_lookup()
        elif choice == '4':
            username_search()
        elif choice == '5':
            email_lookup()
        elif choice == '6':
            dns_enum()
        elif choice == '7':
            port_scan()
        elif choice == '0':
            print(f"\n{Fore.RED}[!] Exiting...")
            print(f"{Fore.GREEN}[✓] Goodbye! Stay safe!")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}[✘] Invalid choice! Please try again.")

        try:
            input(f"\n{Fore.YELLOW}[↩] Press Enter to continue...")
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)

# =====================================
#  MAIN ENTRY POINT
# =====================================
if __name__ == '__main__':
    try:
        print(f"{Fore.CYAN}[*] Checking & installing dependencies...")
        install_dependencies()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Interrupted... Exiting")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[✘] Error: {e}")
        sys.exit(1)

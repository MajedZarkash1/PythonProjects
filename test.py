def chatbot(user_input):
    responses = {
        # IT & Cybersecurity (Expanded)
        "what is python": "Python is a popular programming language for web, AI, and data science!",
        "what is an api": "API stands for Application Programming Interface. It lets apps talk to each other!",
        "what is cloud computing": "Cloud computing means storing and accessing data over the internet instead of a local computer.",
        "what is ethical hacking": "Ethical hacking is using hacking skills to find security weaknesses and fix them!",
        "what is artificial intelligence": "AI is technology that allows machines to learn and make decisions!",
        "what is a database": "A database is a structured way to store and manage data!",
        "what is frontend development": "Frontend is what users see on a website! HTML, CSS, and JavaScript make it happen.",
        "what is backend development": "Backend is the server side of a website! It handles logic, databases, and APIs.",
        "what is a full-stack developer": "A full-stack developer works on both frontend and backend!",
        "what is machine learning": "Machine learning is a type of AI that helps computers learn from data!",

        # Expanded IT & Cybersecurity
        "what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.",
        "what is malware": "Malware is any software designed to harm a computer or network, like viruses or ransomware.",
        "what is a firewall": "A firewall is a security system that monitors and controls incoming and outgoing network traffic.",
        "what is phishing": "Phishing is when attackers try to trick people into revealing sensitive information, like passwords.",
        "what is a vpn": "A VPN (Virtual Private Network) creates a secure connection over the internet, protecting your privacy.",
        "what is encryption": "Encryption is the process of converting information into a code to prevent unauthorized access.",
        "what is two-factor authentication": "Two-factor authentication (2FA) adds an extra layer of security by requiring two forms of identification.",
        "what is a ddos attack": "A DDoS (Distributed Denial of Service) attack is when multiple computers overwhelm a server, making it unavailable.",
        "what is a hacker": "A hacker is someone who gains unauthorized access to systems or data, often for malicious purposes.",
        "what is ransomware": "Ransomware is a type of malware that locks your files and demands payment to unlock them.",
        "what is a trojan horse": "A Trojan horse is a type of malware that appears as a legitimate program but secretly harms your system.",
        "what is penetration testing": "Penetration testing (ethical hacking) involves simulating attacks to find vulnerabilities in systems.",
        "what is the dark web": "The dark web is part of the internet that's not indexed by search engines and is often used for illegal activities.",
        "what is an ip address": "An IP address is a unique identifier for a device on a network, like a phone or computer.",
        "what is a botnet": "A botnet is a network of infected computers controlled by a hacker to perform malicious tasks.",
        "what is social engineering": "Social engineering is manipulating people into giving up confidential information or access to systems.",
        "what is a security breach": "A security breach is an incident where unauthorized access is gained to systems or data.",
        "what is encryption key": "An encryption key is used to encode and decode data, ensuring that only authorized users can access it.",
        "what is a vulnerability": "A vulnerability is a weakness in a system that can be exploited by an attacker.",
        "what is a rootkit": "A rootkit is a type of malware that hides itself in a system, allowing attackers to maintain control without detection.",
        "what is a data breach": "A data breach is when sensitive, confidential, or protected information is accessed or disclosed without permission.",
        "what is a password manager": "A password manager securely stores and organizes your passwords, helping you avoid weak or repeated passwords.",
        "what is a bot": "A bot is an automated program designed to perform repetitive tasks, like web scraping or responding to users.",
        "what is a vpn kill switch": "A VPN kill switch cuts your internet connection if the VPN connection is lost, protecting your privacy.",
        "what is endpoint security": "Endpoint security protects devices like computers, phones, and tablets from cyber threats.",
        "what is a security token": "A security token is a physical device or software-based tool used for secure authentication, like two-factor authentication.",
        "what is a proxy server": "A proxy server acts as an intermediary between your device and the internet, helping to secure or anonymize your traffic.",
        "what is a honeypot": "A honeypot is a decoy system set up to attract hackers and study their methods without compromising real data.",
        "what is an exploit": "An exploit is a piece of code or method used to take advantage of a vulnerability in a system.",
        "what is a bug bounty": "A bug bounty is a program where companies reward individuals who find and report vulnerabilities in their systems.",
        "what is zero-day exploit": "A zero-day exploit is an attack that targets a vulnerability before the vendor has released a fix for it.",
        "what is a security patch": "A security patch is an update that fixes vulnerabilities in software or hardware to prevent attacks.",
        "what is a bot attack": "A bot attack occurs when malicious bots flood a server or website, often causing it to crash or become unresponsive.",
        "what is a keylogger": "A keylogger is software that records keystrokes, often used to steal personal information like passwords.",
        "what is a trojan virus": "A Trojan virus is a type of malware that disguises itself as legitimate software but performs harmful actions.",
        "what is a cyber attack": "A cyber attack is any deliberate action taken to damage or disrupt a computer system or network.",
        "what is a bug": "A bug is an error or flaw in software that causes it to behave unexpectedly or incorrectly.",
        "what is code injection": "Code injection is a vulnerability that allows an attacker to insert malicious code into a program.",
        "what is a script kiddie": "A script kiddie is an unskilled hacker who uses pre-written tools and scripts to attack systems.",
        "what is a cipher": "A cipher is an algorithm used for encryption and decryption of data to keep it secure.",
        "what is an exploit kit": "An exploit kit is a collection of tools that allows attackers to exploit vulnerabilities in software.",
        "what is threat intelligence": "Threat intelligence involves collecting and analyzing information to predict and prevent cyber threats.",
        "what is a botnet attack": "A botnet attack is when multiple compromised devices are used to launch a coordinated cyber attack, often DDoS.",
        
        # Additional IT & Cybersecurity Terms
        "what is cryptojacking": "Cryptojacking is when hackers secretly use your computer's power to mine cryptocurrency without your consent.",
        "what is a backdoor": "A backdoor is a hidden entry point into a system, often created by malware for remote control by an attacker.",
        "what is a man-in-the-middle attack": "A man-in-the-middle (MITM) attack occurs when an attacker intercepts and manipulates communication between two parties.",
        "what is a patch management": "Patch management is the process of updating software to fix security vulnerabilities and bugs.",
        "what is osint": "OSINT (Open Source Intelligence) is the process of collecting publicly available data for security analysis.",
        "what is a ransomware attack": "A ransomware attack locks your files and demands a ransom to release them, often affecting businesses and individuals.",
        "what is a privilege escalation": "Privilege escalation is when an attacker gains higher levels of access to a system than intended, often to execute malicious tasks.",
        "what is a sandbox": "A sandbox is an isolated environment used to test suspicious programs or code without affecting the main system.",
        "what is a whitelist": "A whitelist is a list of trusted entities or addresses that are allowed access to a system, network, or resource.",
        "what is a black hat hacker": "A black hat hacker is a malicious hacker who violates security for personal gain or to cause harm.",
        "what is a white hat hacker": "A white hat hacker is an ethical hacker who helps organizations identify and fix vulnerabilities.",
        "what is a gray hat hacker": "A gray hat hacker is someone who finds vulnerabilities but doesn't have permission, yet reports them for potential rewards.",
    }

    return responses.get(user_input.lower(), "Sorry, I don't have an answer for that.")

while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break
    print("Bot:", chatbot(user_text))

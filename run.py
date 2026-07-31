#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import time
import secrets

def print_step(message):
    print(f"\n[*] {message}")

def print_error(message):
    print(f"[!] ERROR: {message}")
    sys.exit(1)

def print_success(message):
    print(f"[+] {message}")

def check_command(cmd):
    return shutil.which(cmd) is not None

def generate_secret_key():
    secret_file = ".ctfd_secret_key"
    if not os.path.exists(secret_file):
        print_step("Generating secure .ctfd_secret_key...")
        with open(secret_file, "w") as f:
            f.write(secrets.token_hex(32))
        print_success("Secret key generated successfully.")
    else:
        print_step(".ctfd_secret_key already exists. Skipping generation.")

def check_docker():
    print_step("Checking for Docker and Docker Compose...")
    
    if not check_command("docker"):
        print_error("Docker is not installed or not in your PATH.")
        if sys.platform == "win32":
            print("Please download and install Docker Desktop for Windows: https://docs.docker.com/desktop/install/windows/")
        elif sys.platform == "darwin":
            print("Please download and install Docker Desktop for Mac: https://docs.docker.com/desktop/install/mac-install/")
        else:
            print("Please install Docker: curl -fsSL https://get.docker.com | sh")
        sys.exit(1)
        
    # Check if 'docker compose' (v2) or 'docker-compose' (v1) is available
    compose_cmd = None
    try:
        # Check docker compose (V2)
        subprocess.run(["docker", "compose", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        compose_cmd = ["docker", "compose"]
    except (subprocess.CalledProcessError, FileNotFoundError):
        if check_command("docker-compose"):
            compose_cmd = ["docker-compose"]
        else:
            print_error("Docker Compose is not installed.")
            print("Please ensure Docker Compose is installed and available in your PATH.")
            sys.exit(1)
            
    print_success(f"Found Docker and Compose: {' '.join(compose_cmd)}")
    return compose_cmd

def start_platform(compose_cmd):
    print_step("Starting Operation Black Vault...")
    
    try:
        # Run docker compose up -d --build
        cmd = compose_cmd + ["up", "-d", "--build"]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print_success("Containers started successfully in the background.")
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to start containers. Error code: {e.returncode}")
    except KeyboardInterrupt:
        print("\n[!] Setup interrupted by user.")
        sys.exit(1)

def main():
    print("="*50)
    print(" Operation Black Vault - Universal Setup Script ")
    print("="*50)
    
    # Ensure we are in the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 1. Generate secret key if missing
    generate_secret_key()
    
    # 2. Check for docker dependencies
    compose_cmd = check_docker()
    
    # 3. Start the platform
    start_platform(compose_cmd)
    
    # 4. Provide access info
    print("\n" + "="*50)
    print_success("Operation Black Vault is now launching!")
    print("It may take 1-2 minutes for the database and web server to fully boot up.")
    print("\nAccess the platform at:")
    print("  Local Access: http://localhost:8000")
    print("  Network Access: http://<YOUR_IP_ADDRESS>:8000")
    print("\nTo stop the platform, run:")
    print(f"  {' '.join(compose_cmd)} down")
    print("="*50)

if __name__ == "__main__":
    main()

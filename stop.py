#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil

def print_step(message):
    print(f"\n[*] {message}")

def print_error(message):
    print(f"[!] ERROR: {message}")
    sys.exit(1)

def print_success(message):
    print(f"[+] {message}")

def check_command(cmd):
    return shutil.which(cmd) is not None

def check_docker():
    print_step("Checking for Docker and Docker Compose...")
    
    if not check_command("docker"):
        print_error("Docker is not installed or not in your PATH.")
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
            sys.exit(1)
            
    print_success(f"Found Docker and Compose: {' '.join(compose_cmd)}")
    return compose_cmd

def stop_platform(compose_cmd):
    print_step("Stopping Operation Black Vault...")
    
    try:
        # Run docker compose down
        cmd = compose_cmd + ["down"]
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print_success("Containers stopped and removed successfully.")
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to stop containers. Error code: {e.returncode}")
    except KeyboardInterrupt:
        print("\n[!] Shutdown interrupted by user.")
        sys.exit(1)

def main():
    print("="*50)
    print(" Operation Black Vault - Universal Shutdown Script ")
    print("="*50)
    
    # Ensure we are in the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 1. Check for docker dependencies
    compose_cmd = check_docker()
    
    # 2. Stop the platform
    stop_platform(compose_cmd)
    
    print("\n" + "="*50)
    print_success("Operation Black Vault has been safely shut down.")
    print("="*50)

if __name__ == "__main__":
    main()

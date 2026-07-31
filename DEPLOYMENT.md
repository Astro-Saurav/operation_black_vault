# Operation Black Vault: Deployment Guide

This project is fully containerized using Docker and Docker Compose. Because all customizations (including SCSS, assets, database structure, and the Operation Black Vault plugin) are embedded directly within this source code, deployment is as simple as cloning the repository and bringing up the Docker containers.

## Prerequisites
- A cloud virtual machine (EC2 on AWS or a Virtual Machine on Azure)
- Ubuntu 22.04 LTS (recommended)
- Docker & Docker Compose installed on the VM
- A public IP address configured with your cloud provider

---

## Deployment on AWS (Amazon Web Services)

1. **Launch an EC2 Instance:**
   - Go to the AWS EC2 Dashboard.
   - Click **Launch Instance**.
   - Choose **Ubuntu Server 22.04 LTS** as the AMI.
   - Choose an Instance Type (e.g., `t3.medium` or larger is recommended for adequate memory).
   - Configure your Security Group to allow inbound traffic on **HTTP (Port 80)**, **HTTPS (Port 443)**, and **SSH (Port 22)** from anywhere.
   - Launch the instance and SSH into it.

2. **Clone the Repository:**
   (Ubuntu 22.04 comes with Git pre-installed. If not, run `sudo apt update && sudo apt install git`).
   ```bash
   git clone https://github.com/Astro-Saurav/operation_black_vault.git
   cd operation_black_vault
   ```

3. **Deploy the Platform:**
   ```bash
   python3 run.py
   ```
   The `run.py` script automatically verifies dependencies, generates a secure `.ctfd_secret_key`, and brings up the Docker containers. You can stop the platform cleanly at any time by running `python3 stop.py`.

4. **Access the Platform:**
   Find your EC2 instance's **Public IPv4 Address** or **Public IPv4 DNS** in the AWS console and visit it in your browser (`http://<YOUR_AWS_IP>`).

---

## Deployment on Microsoft Azure

1. **Create a Virtual Machine:**
   - Go to the Azure Portal and search for **Virtual Machines**.
   - Click **Create > Azure virtual machine**.
   - Select the **Ubuntu Server 22.04 LTS** image.
   - Choose a size (e.g., `Standard_B2s`).
   - Under **Inbound port rules**, allow **SSH (22)**, **HTTP (80)**, and **HTTPS (443)**.
   - Click **Review + Create** and launch the VM. Once running, SSH into it.

2. **Clone the Repository:**
   (Ubuntu 22.04 comes with Git pre-installed. If not, run `sudo apt update && sudo apt install git`).
   ```bash
   git clone https://github.com/Astro-Saurav/operation_black_vault.git
   cd operation_black_vault
   ```

3. **Deploy the Platform:**
   ```bash
   python3 run.py
   ```
   The `run.py` script automatically verifies dependencies, generates a secure `.ctfd_secret_key`, and brings up the Docker containers. You can stop the platform cleanly at any time by running `python3 stop.py`.

4. **Access the Platform:**
   Find your VM's **Public IP address** in the Azure portal and visit it in your browser (`http://<YOUR_AZURE_IP>`).

---

## Important Production Notes
* **Data Persistence**: The platform utilizes local Docker volumes (`.data/`) to store MySQL data, Redis caches, and uploaded files. This ensures your data persists even if the containers restart.
* **Secret Key**: Before deploying to a wide audience, open `.ctfd_secret_key` and ensure it is randomly generated and kept secure.
* **HTTPS/SSL**: For production, it is highly recommended to place a reverse proxy (like NGINX or Caddy) or a Cloud Load Balancer in front of the platform to handle SSL/HTTPS termination.

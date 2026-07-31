# Operation Black Vault

**Operation Black Vault** is a highly customized, immersive Capture The Flag (CTF) platform built on top of the robust [CTFd](https://github.com/CTFd/CTFd) framework.

Designed for immersive cybersecurity training and competitive operations, this platform features a completely custom, responsive, and dynamic UI. It transforms the standard CTF experience into a realistic, cyberpunk-inspired intelligence operation center.

## Features
- **Tactical Cyberpunk UI**: Fully custom SCSS styling featuring glassmorphism, dynamic animations, and curated background art.
- **Redesigned Dashboards**: Re-skinned Active Operations (challenges), Intel Rankings (scoreboards), and Dossiers (profiles) to fit an intelligence agency aesthetic.
- **Dockerized Deployment**: Fully containerized out-of-the-box for rapid and reproducible deployments on any cloud provider.
- **Powered by CTFd**: Leverages the proven stability, rich plugin ecosystem, and deep administrative controls of the core CTFd engine.

## Quick Start (Deployment)

This repository comes with automated setup scripts that make deploying the customized containerized environment completely frictionless across Linux, macOS, and Windows.

```bash
git clone https://github.com/Astro-Saurav/operation_black_vault.git
cd operation_black_vault
python3 run.py
```

The script will automatically check for dependencies, generate a secure `.ctfd_secret_key`, and launch all Docker containers in the background.

To cleanly shut down the platform at any time, run:
```bash
python3 stop.py
```

For detailed production deployment instructions (AWS EC2 / Microsoft Azure), please refer to our comprehensive [DEPLOYMENT.md](DEPLOYMENT.md) guide.

---

## Acknowledgements and Credits

This project is a heavily customized fork of **[CTFd](https://github.com/CTFd/CTFd)**. 

All core backend functionality, database architecture, and administrative tooling are provided by the excellent work of the CTFd team. We extend our full credit and immense gratitude to them for providing such a powerful open-source framework that made this tactical reskin possible.

- **CTFd Website**: [https://ctfd.io/](https://ctfd.io/)
- **CTFd Repository**: [https://github.com/CTFd/CTFd](https://github.com/CTFd/CTFd)

## License
Since this project is based on CTFd, it respects and inherits the original open-source licensing. Please refer to the [LICENSE](LICENSE) file for more details.

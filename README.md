<p align="center">
  <img src="./image/header.svg" alt="IP Binary Class Detector">
</p>

# IP Binary Class Detector

A simple Python CLI tool that validates IPv4 addresses, converts each octet into its 8-bit binary representation, and identifies the corresponding IP address class.

<p align="center">
  <img src="./image/work.svg" alt="How IP Binary Class Detector works">
</p>

## Features

* IPv4 address validation
* Convert IPv4 octets to 8-bit binary
* Detect IPv4 address classes
* Handle invalid IP addresses
* Interactive command-line interface

## Requirements

* Python 3.x
* No external packages required

The project uses Python's built-in `ipaddress` module.

## Usage

Run the program with:

```bash
python ipv4_validator.py
```

Enter an IPv4 address when prompted. The program will validate the address, display each octet in binary, and determine its IP class.

## Project Structure

```text
IP-Binary-Class-Detector/
├── ipv4_validator.py
├── README.md
└── image/
    ├── header.svg
    └── work.svg
```

## Technologies

* Python
* IPv4
* `ipaddress` module


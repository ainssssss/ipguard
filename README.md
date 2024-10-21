# IPGuard 

## IP retriever tool

This Project is a Collaboration between cybersecurity students at ENTI - UB (read license). 

This Python script performs IP information lookups, such as geolocation coordinates, ISP, city, country, and more using the ipinfo.io API.

## Features

- Retrieve detailed information about a user: IP, browser (user-agent), geo-coordinates.
- IP address information extraction from a custom IP.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ainssssss/ipguard.git
    ```

2. Navigate to the project directory:
    ```sh
    cd ipguard
    ```

2. Install the required packages:
    ```sh
    pip3 install -r requirements.txt --no-cache-dir; yes yes | python3 manage.py collectstatic
    ```

## Usage

To run the script and query information about an IP address, use the following command:
  ```sh
  python manage.py runserver
  ```

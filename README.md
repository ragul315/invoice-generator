# Invoice Generator

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
  - [Cloning the Repository](#cloning-the-repository)
  - [Installing Dependencies](#installing-dependencies)
  - [Database Configuration](#database-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

Invoice Generator is a comprehensive Python-based application designed to manage and streamline invoice generation, user authentication, and related functionalities. Leveraging a MySQL database backend, the system offers an intuitive interface for users to create, view, and manage invoices efficiently.

## Features

- **User Authentication**: Secure login mechanism for authorized access.
- **Dashboard Interface**: User-friendly dashboard post-login, presenting various functionalities.
- **Invoice Generation**: Dynamic creation and management of invoices with detailed itemization.
- **Invoice Viewing**: Instant access to invoice details via an ID-based search mechanism.
- **User Management**: Administrative capabilities for user addition, modification, and access control.

## Prerequisites

Ensure you have the following prerequisites installed and configured on your system:

- Python 3.x
- MySQL Server
- Required Python packages (`tkinter`, `mysql.connector`, `subprocess`, `docxtpl`, `docx2pdf`, `win32api`)

## Installation and Setup

### Cloning the Repository

1. Clone the Invoice Generator repository to your local machine:
   ```bash
   git clone https://github.com/ragul0420/invoice-generator.git
   ```

### Installing Dependencies

Navigate to the project directory and install the necessary Python packages:

```bash
cd invoice-generator
pip install -r requirements.txt
```

### Installing Dependencies

Navigate to the project directory and install the necessary Python packages:

```bash
cd invoice-generator
pip install -r requirements.txt
```

### Database Configuration

Configure the MySQL database by executing the SQL commands located in the sql commands.sql file. Ensure you update the database connection parameters in the respective Python files (login_page.py, view_invoice.py, etc.) to match your MySQL configuration.

## Usage

Launch the application by executing the login page script:

```bash
python login_page.py
```

## Contributing

Contributions, enhancements, and feedback are encouraged! Please review the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. Refer to the LICENSE file for detailed licensing information.

## Acknowledgements

Special thanks to the following technologies and resources that contributed to the development and success of this project:

- Python
- MySQL
- Tkinter
- GitHub

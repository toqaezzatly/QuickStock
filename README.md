# Quick Stock - Inventory Management System


## Overview

Quick Stock is a simple, web-based inventory management system designed for small businesses. It allows users to track their product inventory, manage products (add, edit, delete), and handle user authentication with basic login and registration functionalities.

This project is built using:

*   **Python** as the primary language.
*   **Flask** as the web framework.
*   **SQLite** for database management.
*   **HTML, CSS** for user interface.

## Features

*   **User Authentication:** Secure user registration and login with password hashing.
*   **Product Management:**
    *   Add new products to the inventory.
    *   View all products in a table.
    *   Edit existing product details.
    *   Delete products from the inventory.
*   **Basic Inventory Tracking:**  Display products with their name, price, and quantity.
*   **Theme switching:** Basic implementation to change the overall theme of the application.
*   **Responsive Design:** The application is designed to be usable on different screen sizes.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.7 or higher**
*   **pip** (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/toqaezzatly/QuickStock
    cd quick_stock
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Linux/macOS
    # venv\Scripts\activate on Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install Flask requests cryptography
    ```

### Running the Application

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

2.  **Access the application:** Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1.  **Register or Login:** You'll be prompted to register a new user or log in with existing credentials.
2.  **View Inventory:** Once logged in, you'll see the main inventory page.
3.  **Manage Products:** Use the "Add Product," "Edit," and "Delete" features to manage your inventory.

## Project Structure
*   **`app.py`:** Contains the main Flask application code.
*   **`models.py`:** Defines the data models (Product, Inventory).
*   **`auth.py`:** Handles user authentication and security.
*   **`database.py`:** Contains database connection and query logic.
*   **`templates/`:** Directory for HTML templates.
*   **`static/`:** Directory for static files (CSS).
*   **`README.md`:** Provides project overview and usage information.

## Technologies Used

*   **Python:** Core programming language.
*   **Flask:** Web framework for the backend.
*   **SQLite:** Database for storing data.
*   **HTML/CSS:** Frontend development.
*   **Git:** Version control.

## Contributing

Contributions are always welcome! If you would like to contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes with clear commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

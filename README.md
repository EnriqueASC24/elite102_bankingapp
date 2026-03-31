# Python SQLite Project

This project is a simple Python application that interacts with an SQLite database. It serves as a demonstration of how to set up a Python project with SQLite and includes basic functionality for database operations.

## Setup Instructions
1. **Create a Codespace:**
   - Navigate to the repository on GitHub.
   - Click the **Code** button and select **Codespaces**.
   - Click **Create codespace on main** to start a new Codespace.
   - You can run the Codespace directly in your browser or open it in VS Code by connecting to the Codespace.

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   You can start the application by running:
   ```
   python initialize_db.py
   ```

4. **Run the application:**
   You can start the application by running:
   ```
   python main.py
   ```

## Usage

- The application initializes a connection to the SQLite database and allows for basic CRUD operations.
- Modify the `src/database/db_setup.py` file to customize the database schema and initial data.

## Development

This project is set up to be used with a development container. You can open it in a containerized environment by using the `.devcontainer` configuration.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Flask Calculator

A simple and interactive web-based calculator built using Python's Flask framework. The calculator allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) between two numbers. The application features an intuitive user interface and dynamic result display.

---

## Features

- **Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Dynamic Result Display**: Displays results directly on the same page after calculation.
- **Error Handling**: Provides appropriate error messages for invalid inputs (e.g., non-numeric values, division by zero).
- **Responsive Design**: Styled with CSS for a simple and user-friendly interface.

---

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS

---

## Installation and Usage

### Prerequisites

- Python 3.x installed on your system.
- Flask library installed. You can install it using:

```bash
pip install flask
```

### Steps to Run the Application

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Run the Flask Application**:

   ```bash
   python app.py
   ```

3. **Access the Application**:
   Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

4. **Perform Calculations**:

   - Enter two numbers.
   - Select the desired operation (Addition, Subtraction, Multiplication, Division).
   - Click the **Calculate** button to view the result.

---

## Project Structure

```
.
├── app.py                  # Flask backend code
├── templates
      └── index.html        # Frontend HTML file

```

## Error Handling

- **Invalid Inputs**: Displays an error message when non-numeric values are entered.
- **Division by Zero**: Provides an appropriate error message when trying to divide by zero.

---

## Future Improvements

- Add advanced mathematical operations (e.g., exponents, square roots).
- Integrate JavaScript for real-time calculations without page reloads.
- Enhance UI/UX with more styling and animations.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgments

- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Inspiration from web-based calculators.

---

Feel free to contribute to this project by submitting issues or pull requests!



# RECEIPT GENERATOR
#### Video Demo:  <https://youtu.be/cI9Yy-spuvY>
#### Description:

The Receipt Generator is a simple command-line application written in Python. It allows users to input product information, such as product name, quantity, and unit price, to generate a receipt for a fictional restaurant. The generated receipt is saved as both a text file (`receipt.txt`) and a PDF file (`billGenerated.pdf`).

## Table of Contents
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [How to Run Tests](#how-to-run-tests)

## Project Structure

### `project.py` (Main Script)
- **Dependencies:**
  - `fpdf`: A library for creating PDF files in Python.
- **Functions:**
  - **`main():`** Entry point of the program. Calls `generate_receipt()` to start the receipt generation process.
  - **`generate_receipt():`** Manages the receipt generation process by collecting product information, writing to a text file, calculating the total sum, and creating a PDF receipt.
  - **`get_product_info():`** Collects product information from the user, such as name, quantity, and price.
  - **`write_billing_info(file_name, product_name, product_quantity, product_price, index):`** Writes billing information to a text file, including product details and calculated totals.
  - **`create_pdf(file_content):`** Creates a PDF file from the billing information stored in the text file.

### `test_project.py` (Unit Tests)
- **Dependencies:**
  - `pytest`: A testing framework for Python.
  - `unittest.mock.patch`: Used for mocking user input during tests.
- **Test Cases:**
  - **`test_generate_receipt():`** Tests the main receipt generation process, mocking user input.
  - **`test_write_billing_info(tmp_path):`** Tests the function that writes billing information to a text file.
  - **`test_create_pdf(tmp_path):`** Tests the function responsible for creating a PDF file from a given text file.
  - **`test_get_product_info(capsys):`** Tests the function that collects product information from the user.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running: `pip install fpdf2`
3. Run the main script: `python project.py`
4. Follow the prompts to input product information. To finish and generate the receipt, enter 'q' when prompted for the product name.
5. The generated receipt will be saved as both `receipt.txt` and `billGenerated.pdf`.

## How to Run Tests

1. Install the required test dependencies by running: `pip install pytest`
2. Run the tests using the following command: `pytest test_project.py`

**Note:** The project assumes a Linux/Mac environment. Adjust file paths accordingly if using Windows.


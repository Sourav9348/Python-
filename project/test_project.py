import pytest
from unittest.mock import patch
from project import generate_receipt, create_pdf, write_billing_info, get_product_info


def test_generate_receipt():
    with patch('builtins.input', side_effect=['Product1', '2', '10', 'Product2', '3', '15', 'q']):
        generate_receipt()


def test_write_billing_info(tmp_path):
    file_name = tmp_path / "test_receipt.txt"
    product_name = "TestProduct"
    product_quantity = 2
    product_price = 10
    index = 1

    write_billing_info(file_name, product_name, product_quantity, product_price, index)

    with open(file_name, "r") as file:
        content = file.read()
        assert f"{index}. Product Name = {product_name}" in content
        assert f"Quantity   = {product_quantity}" in content
        assert f"Price   = {product_price}" in content
        assert f"billed: {product_price} x {product_quantity} = Rs. {float(product_price) * product_quantity}" in content


def test_create_pdf(tmp_path):
    file_content = ["Line 1", "Line 2", "Line 3"]
    file_name = tmp_path / "test_receipt.txt"
    with open(file_name, "w") as file:
        file.write("\n".join(file_content))


def test_get_product_info(capsys):
    with patch('builtins.input', side_effect=['TestProduct', '2', '10']):
        product_name, product_quantity, product_price = get_product_info()
        assert product_name == 'TestProduct'
        assert product_quantity == 2
        assert product_price == '10'


if __name__ == "__main__":
    pytest.main()

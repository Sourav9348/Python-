from fpdf import FPDF
from fpdf.enums import XPos, YPos

def main():
    generate_receipt()


def get_product_info():
    product_name = input("Enter the product name (Press q to print the final bill): \n")

    if product_name == "q":
        return None, None, None

    product_quantity = int(input("Enter the product quantity : \n"))
    product_price = input("Enter the unit price : \n")
    return product_name, product_quantity, product_price


def write_billing_info(file_name, product_name, product_quantity, product_price, index):
    billing = f"{index}. Product Name = {product_name}\n   Price   = {product_price}\n   Quantity   = {product_quantity}\n   billed: {product_price} x {product_quantity} = Rs. {float(product_price) * product_quantity}"
    with open(file_name, "a") as file:
        file.write(billing + "\n")
    print(billing)


def create_pdf(file_content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=15)

    for line in file_content:
        pdf.cell(200, 10, text=line, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
    pdf.output("billGenerated.pdf")


def generate_receipt():
    filename = "receipt.txt"

    with open(filename, "w") as f:
        f.write("********************************  Sourav's Restaurant  *********************************\n\n")

    total_sum = 0
    index = 1

    while True:
        product_name, product_quantity, product_price = get_product_info()

        if product_name is None:
            break

        total_sum += float(product_price) * product_quantity
        write_billing_info(filename, product_name, product_quantity, product_price, index)
        index += 1

    print(f"Order total so far Rs. {total_sum}")

    with open(filename, "a") as f:
        thanq = f"\n\n!!! Your bill total is only Rs. {total_sum}. Thanks for shopping with us !!!\n\n"
        f.write(thanq)
        print(thanq)

    with open(filename, "r") as f:
        file_content = f.readlines()

    create_pdf(file_content)



if __name__ == "__main__":
    main()


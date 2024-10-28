# Creating the PDF for AP Computer Science Principles sample questions
from fpdf import FPDF

# Create PDF instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title font
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'AP Computer Science Principles - Sample Questions', ln=True, align='C')

# Add some space
pdf.ln(10)

# Set normal font
pdf.set_font('Arial', '', 12)

# Question 1
pdf.multi_cell(0, 10, '1. Variables and Data Types\n'
                      'Question: Write a Python program that takes an integer input from the user and prints whether '
                      'the number is even or odd.\n')

# Question 2
pdf.multi_cell(0, 10, '2. Conditionals and Loops\n'
                      'Question: Create a Python program that prints the sum of all even numbers between 1 and 100.\n')

# Question 3
pdf.multi_cell(0, 10, '3. Functions\n'
                      'Question: Define a Python function is_prime(n) that returns True if the given number n is prime '
                      'and False otherwise.\n')

# Question 4
pdf.multi_cell(0, 10, '4. Lists and Loops\n'
                      'Question: Write a Python program that takes a list of integers and returns the largest number in the list.\n')

# Question 5
pdf.multi_cell(0, 10, '5. Dictionaries\n'
                      'Question: Create a Python dictionary to store information about a book: title, author, publication year, and genre. '
                      'Write a program that allows the user to input this information and then prints it.\n')

# Question 6
pdf.multi_cell(0, 10, '6. Algorithms\n'
                      'Question: Implement a Python program to perform a binary search on a sorted list of integers.\n')

# Question 7
pdf.multi_cell(0, 10, '7. File Handling\n'
                      'Question: Write a Python program that reads a file called data.txt, counts the number of lines, and prints the result.\n')

# Question 8
pdf.multi_cell(0, 10, '8. APIs and JSON\n'
                      'Question: Use Python\'s requests and json libraries to fetch and display data from a public API (e.g., weather data or cryptocurrency prices).\n')

# Question 9
pdf.multi_cell(0, 10, '9. Data Visualization\n'
                      'Question: Use Python\'s matplotlib library to plot a bar chart of student scores in a class.\n')

# Question 10
pdf.multi_cell(0, 10, '10. Simulations\n'
                      'Question: Create a Python simulation that models a coin toss experiment. The program should simulate flipping a coin 1000 times and print the number of heads and tails.\n')

# Save the PDF to a file
pdf_output_path = "AP_CS_Principles_Sample_Questions.pdf"
pdf.output(pdf_output_path)



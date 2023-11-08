import fpdf
import openai
from PIL import Image

# Set up your OpenAI API key
openai.api_key = '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'


# Function to generate cover letter using OpenAI
def generate_cover_letter(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Function to create the PDF
def create_pdf(cv_data, cover_letter, image_path):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add the image
    if image_path:
        try:
            Image.open(image_path)  # Check if the image is valid
            pdf.image(image_path, x=10, y=8, w=33)
        except IOError:
            print("Image file is not valid")

    # Add the CV data
    pdf.ln(40)  # Move 40 down
    for line in cv_data:
        pdf.cell(200, 10, txt=line, ln=True)

    # Add the cover letter
    pdf.add_page()
    pdf.multi_cell(0, 10, cover_letter)

    # Save the PDF to a file
    pdf.output("your_cv.pdf")


# Example usage
cv_information = ["Name: John Doe", "Email: john.doe@example.com", "..."]
cover_letter_prompt = "Write a cover letter for a software engineer position at a tech company."
cover_letter_text = generate_cover_letter(cover_letter_prompt)
create_pdf(cv_information, cover_letter_text, "path_to_image.jpg")

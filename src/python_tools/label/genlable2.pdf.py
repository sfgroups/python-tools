from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def generate_labels(pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=A4)

    label_width = 3.37 * inch  # Credit card width in inches
    label_height = 2.12 * inch  # Credit card height in inches
    margin = 0.25 * inch  # Margin between labels

    start_x = margin
    start_y = A4[1] - margin - label_height

    for _ in range(6):
        c.rect(start_x, start_y, label_width, label_height)
        start_x += label_width + margin

        if start_x + label_width > A4[0]:
            start_x = margin
            start_y -= label_height + margin
            if start_y < margin:
                c.showPage()
                start_x = margin
                start_y = A4[1] - margin - label_height

    c.save()


if __name__ == "__main__":
    generate_labels("credit_card_labels.pdf")

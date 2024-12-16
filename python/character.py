from colorama import Fore, Style, init
from PIL import Image, ImageDraw, ImageFont

init(autoreset=True)

def generate_table():
    header = (
        f"┌───────────┬──────────┬─────────┬────────────┬──────────┐\n"
        f"│ {'Decimal':^9} │ {'Binary':^8} │ {'Octal':^7} │ {'Hexadecimal':^10}│ {'ASCII':^8}│\n"
        f"├───────────┼──────────┼─────────┼────────────┼──────────┤\n"
    )

    rows = []
    for i in range(256):
        binary = bin(i)[2:].zfill(8)
        octal = oct(i)[2:].zfill(3)
        hexa = hex(i)[2:].upper().zfill(2)
        char = chr(i) if 32 <= i <= 126 else ''
        row = (
            f"│ {i:^9} │ {binary:^8} │ {octal:^7} │ {hexa:^10} │ {char:^8} │"
        )
        rows.append(row)

    footer = "└───────────┴──────────┴─────────┴────────────┴──────────┘"
    return header, rows, footer

def save_and_split_image(text, rows, output_file="table.png"):
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    font_size = 12

    font = ImageFont.truetype(font_path, font_size)
    lines = text.split("\n")

    max_line_width = max([font.getbbox(line)[2] for line in lines])
    line_height = font.getbbox("A")[3]

    image_width = max_line_width + 20
    header_height = line_height * 3
    row_height = line_height
    num_splits = 4
    rows_per_split = len(rows) // num_splits
    crop_height = header_height + (rows_per_split * row_height)

    img = Image.new("RGB", (image_width, crop_height), "white")

    draw = ImageDraw.Draw(img)
    y_offset = 10
    for line in text.split("\n")[:3]:
        draw.text((10, y_offset), line, font=font, fill="black")
        y_offset += line_height

    img.save(output_file)
    print(f"Table saved as {output_file}")

    cropped_images = []
    for i in range(num_splits):
        start_row = i * rows_per_split
        end_row = (i + 1) * rows_per_split

        section_lines = text.split("\n")[:3]
        section_lines += rows[start_row:end_row]
        section_text = "\n".join(section_lines)

        section_height = header_height + len(section_lines) * row_height
        section_img = Image.new("RGB", (image_width, section_height), "white")
        draw = ImageDraw.Draw(section_img)

        y_offset = 10
        for line in section_lines:
            draw.text((10, y_offset), line, font=font, fill="black")
            y_offset += line_height

        cropped_images.append(section_img)

    combined_width = image_width * num_splits
    combined_height = cropped_images[0].height
    combined_img = Image.new("RGB", (combined_width, combined_height), "white")

    for i, cropped in enumerate(cropped_images):
        combined_img.paste(cropped, (i * image_width, 0))

    combined_output_file = "table_combined.png"
    combined_img.save(combined_output_file)
    print(f"Combined image saved as {combined_output_file}")

header, rows, footer = generate_table()
save_and_split_image(header, rows)

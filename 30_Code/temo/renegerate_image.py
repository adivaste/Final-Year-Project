from PIL import Image, ImageDraw, ImageFont

def generate_image(username="newuser"):
    
    # Create a new image with a white background
    width, height = 500, 300
    background_color = (255, 255, 255)  # RGB values for white
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Set the font and size
    font_size = 30
    font = ImageFont.truetype("arial.ttf", font_size)  # You can replace "arial.ttf" with the path to your font file

    # Set the text color
    text_color = (0, 0, 0)  # RGB values for black

    # Position to place the text
    text_position = (width // 4, height // 2)

    # Add text to the image
    text = "This is random text"
    draw.text(text_position, text, font=font, fill=text_color)

    # Save or display the image
    image.save(f"{username}.png")
    return text

# generate_image("adi")
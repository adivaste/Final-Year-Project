from PIL import Image, ImageDraw, ImageFont
import random

words = [
    "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "bright", "blue", "sky", "beautiful", "sunny", "day",
    "happy", "cat", "runs", "through", "green", "grass", "under", "big", "yellow", "ball", "flies", "high", "red",
    "balloon", "chases", "clouds", "tiny", "butterfly", "lands", "on", "flower", "near", "river", "sparkling", "water",
    "shines", "in", "moonlight", "stars", "twinkle", "above", "quiet", "forest", "full", "life", "during", "night",
    "soft", "breeze", "whispers", "stories", "among", "trees", "wild", "animals", "rest", "peacefully", "while",
    "crickets", "sing", "their", "songs", "distant", "owl", "hoots", "echoes", "throughout", "dark", "mountains",
    "stand", "tall", "against", "silhouetted", "horizon", "early", "morning", "brings", "fresh", "beginnings",
    "dewdrops", "glisten", "every", "leaf", "bird", "chirps", "melodious", "tune", "world", "awakens", "new", "light",
    "fills", "air", "with", "warmth", "hope"
]

def generate_random_sentence(word_list, num_words=4):
    return ' '.join(random.choices(word_list, k=num_words))

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
    text = generate_random_sentence(words)
    draw.text(text_position, text, font=font, fill=text_color)

    # Save or display the image
    image.save(f"{username}.png")
    return text

# generate_image("adi")
from PIL import Image, ImageFilter
import io


def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """

    image = Image.open(file)
    image = image.filter(eval(f"ImageFilter.{filter.upper()}"))

    file = io.BytesIO()
    image.save(file, "JPEG")
    file.seek(0)

    return file

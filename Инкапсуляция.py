import os
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """
    Класс для сжатия изображений и их обработки в директориях.
    """
    supported_formats = ('.jpg', '.jpeg', '.png')

    def __init__(self, quality: int):
        """
        Инициализирует объект с заданным качеством сжатия.
        """
        self.__quality = quality
        register_heif_opener()

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")

    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)
                    
    @property
    def quality(self) -> int:
        """Геттер для получения качества сжатия."""
        return self.__quality

    @quality.setter
    def quality(self, value: int) -> None:
        """Сеттер для установки качества сжатия."""
        if not (0 <= value <= 100):
            raise ValueError("Качество должно быть в диапазоне 0-100.")
        self.__quality = value
        
from PIL import Image
import os

def resize_images(input_folder, output_folder, size=(640, 640)):
    if not os.path.exists(output_folder):
        print(f"Output folder {output_folder} does not exist. Creating it.")
        os.makedirs(output_folder)
    else:
        print(f"Output folder {output_folder} already exists.")
    
    print(f"Reading images from {input_folder}...")
    for filename in os.listdir(input_folder):
        print(f"Processing file: {filename}")
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            try:
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)
                img_resized = img.resize(size, Image.LANCZOS)
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)
                print(f"Resized and saved {filename} to {output_folder}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
        else:
            print(f"Skipping file {filename} as it does not match the supported image formats.")

# 使用示例
def main():
    input_folder = 'C:/Users/rainbow/Desktop/image2'
    output_folder = 'C:/Users/rainbow/Desktop/output'
    resize_images(input_folder, output_folder)
    
if __name__ == "__main__":
    print("resize is starting......")
    main()
    print("resize over!")
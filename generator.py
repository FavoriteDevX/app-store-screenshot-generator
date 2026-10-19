import os
import sys
from PIL import Image, ImageDraw, ImageFont

class AppStoreScreenshotGenerator:
    def __init__(self):
        # Target Apple App Store Device Target Dimensions Matrix
        self.target_devices = {
            "iPhone_6.7_Inch": (1290, 2796),
            "iPhone_6.5_Inch": (1242, 2688),
            "iPhone_5.5_Inch": (1242, 2208),
            "iPad_Pro_12.9_Inch": (2048, 2732)
        }

    def generate_canvas(self, raw_screenshot_path, title_text, output_dir="AppStore_Output"):
        if not os.path.exists(raw_screenshot_path):
            print(f"❌ Error: Raw screenshot asset missing at path: {raw_screenshot_path}")
            return

        os.makedirs(output_dir, exist_ok=True)
        print(f"🎨 Initializing App Store Asset Generation Engine for text: '{title_text}'...")

        try:
            raw_img = Image.open(raw_screenshot_path)
        except Exception as e:
            print(f"❌ Core Image Decryption Failure: {str(e)}")
            return

        for device_name, dimensions in self.target_devices.items():
            width, height = dimensions
            print(f"⚙️ Structuring Canvas Framework ──► {device_name} ({width}x{height})")

            # 1. Create Linear Gradient Background Matrix
            base_canvas = Image.new("RGBA", (width, height), "#0f172a")
            draw = ImageDraw.Draw(base_canvas)
            
            # Simple soft vertical color distribution overlay gradient logic
            for y in range(height):
                color_ratio = y / height
                r = int(15 + (30 - 15) * color_ratio)
                g = int(23 + (41 - 23) * color_ratio)
                b = int(42 + (59 - 42) * color_ratio)
                draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

            # 2. Render Text Layers Safely (Fallback to default system fonts context)
            text_drawer = ImageDraw.Draw(base_canvas)
            text_y_position = int(height * 0.08)
            
            # Use simple drawing box as default cross-platform layout
            text_drawer.text(
                (width // 2, text_y_position), 
                title_text.upper(), 
                fill="#f8fafc", 
                anchor="mm",
                align="center"
            )

            # 3. Scale and Embed Raw User Screenshot Component
            target_screenshot_width = int(width * 0.85)
            aspect_ratio = raw_img.height / raw_img.width
            target_screenshot_height = int(target_screenshot_width * aspect_ratio)
            
            scaled_screenshot = raw_img.resize(
                (target_screenshot_width, target_screenshot_height), 
                Image.Resampling.LANCZOS
            )

            # Center horizontal alignment, anchor onto bottom frame boundaries
            screenshot_x_position = (width - target_screenshot_width) // 2
            screenshot_y_position = height - target_screenshot_height - int(height * 0.05)

            base_canvas.paste(
                scaled_screenshot, 
                (screenshot_x_position, screenshot_y_position), 
                scaled_screenshot.convert("RGBA") if scaled_screenshot.mode != "RGBA" else scaled_screenshot
            )

            # Save finalized deployment file
            final_path = os.path.join(output_dir, f"{device_name}_final.png")
            base_canvas.save(final_path, "PNG")
            print(f"✅ Generated App Store File: {final_path}")

if __name__ == "__main__":
    # Create a dummy image for quick pipeline validation if none provided
    dummy_input = "mock_screenshot.png"
    if not os.path.exists(dummy_input):
        img = Image.new("RGBA", (800, 1600), "#1e293b")
        d = ImageDraw.Draw(img)
        d.text((400, 800), "App Mockup View", fill="#38bdf8", anchor="mm")
        img.save(dummy_input)

    generator = AppStoreScreenshotGenerator()
    target_title = sys.argv[1] if len(sys.argv) > 1 else "Manage Tasks\nWith Zero Friction"
    generator.generate_canvas(dummy_input, target_title)

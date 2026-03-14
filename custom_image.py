from PIL import Image
import sys

class DeferredImage:
    def __init__(self, default_color=(0, 0, 0, 0)):
        self.pixels = {}  # (x, y): (r, g, b, a)
        self.default_color = default_color

    def set_pixel(self, x, y, rgba):
        if not isinstance(rgba, tuple) or len(rgba) != 4:
            raise ValueError("Pixel data must be a 4-tuple (r, g, b, a)")
        self.pixels[(x, y)] = rgba

    def export(self, path):
        if not self.pixels:
            print("没有任何像素被设置。")
            return

        xs, ys = zip(*self.pixels.keys())
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        print(f"即将导出图片，尺寸为：{width}x{height}")
        '''
        confirm = input("继续导出？(y/n): ").strip().lower()
        if confirm != 'y':
            print("已取消导出。")
            return
    '''
        image = Image.new("RGBA", (width, height), self.default_color)

        for (x, y), color in self.pixels.items():
            px = x - min_x
            py = y - min_y
            image.putpixel((px, py), color)

        image.save(path)
        print(f"已保存图片至 {path}")


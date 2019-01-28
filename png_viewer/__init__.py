import imageio
import matplotlib.pyplot as plt
import sys
from glob import glob
from pathlib import Path
import click


@click.command()
@click.argument('filename')
def png_view(filename):
    PngViewer(filename)


class PngViewer:
    def __init__(self, filename):
        filepath = Path(filename)
        self.files = sorted(glob(str(filepath.parent) + '/*.png'))
        filename = str(filepath)
        for i in range(len(self.files)):
            if filename in self.files[i]:
                break
        self.ind = i

        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.fig.canvas.mpl_connect('key_press_event', self.press)
        raw = imageio.imread(filename, 'PNG-FI')
        self.im = self.ax.imshow(raw / raw.max())
        plt.show()

    def press(self, event):
        sys.stdout.flush()
        if event.key == 'z' or event.key == 'left':
            self.ind -= 1
        elif event.key == 'x' or event.key == 'right':
            self.ind += 1
        else:
            print(f'{event.key} has no functionality yet.')
        filename = self.files[self.ind]
        print(filename)
        raw = imageio.imread(filename, 'PNG-FI')
        self.im.set_data(raw / raw.max())
        self.fig.canvas.draw()
        self.fig.canvas.set_window_title(filename)
        plt.tight_layout()

# Passepartout - Python script for adding borders around images

## Dependencies
* [Pillow](https://pypi.org/project/Pillow/)
* [argparse](https://pypi.org/project/argparse/)
`pip install Pillow argparse`

## Usage
Download and run `passepartout.py` with desired arguments. An image with borders will be created in the same destination as the original, but with an added "\_p" before the file extension. ex: image.jpg -> image\_p.jpg

* `--border` takes an int and "p"(pixels) or "%"(percentage of width). ex: 5p, 10%.
* `--color` takes "white", "black", or a hex code. ex: 4A412A.
* `--weighted` takes "y" or "n", and adds a thicker lower border.

Example input: `python3 passepartout.py --image path/to/image --border 2% --color EFEBDD --weighted y`

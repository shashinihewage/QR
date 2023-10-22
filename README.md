# QR Code Generator

Easily generate QR codes with a simple Python script.

## Features

- Generates QR codes from any text or URL input.
- Customizable box size and border for the QR code.
- Option to modify the QR code's color.

## Requirements

- Python
- qrcode library

## Installation

1. Clone this repository:

```
git clone https://github.com/your_username/your_repo_name.git
```

2. Install the required library:

```
pip install qrcode
```

## Usage

1. Modify the `feature.add_data("https://github.com/shashinihewage")` line in the script with the data or link you want to encode into the QR code.

2. Run the script:

```
python path_to_qrcode_generator_script.py
```

3. The QR code will be saved as `qr.png` in the current directory.

## Customization

- To change the size of the boxes making up the QR code, modify the `box_size` parameter.
- To change the border thickness of the QR code, modify the `border` parameter.
- To change the colors of the QR code, adjust the `fill` and `back_color` parameters in the `feature.make_image` method.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


---

![qr](https://github.com/shashinihewage/QR/assets/87617294/200d455b-9196-4629-8870-5d80539adc25)

Remember to adjust the URLs and paths according to your actual GitHub repository and file paths.

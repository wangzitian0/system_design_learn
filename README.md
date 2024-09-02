# system_design_learn
# Install the stack
## Install the package
mac
```bash
brew install ffmpeg cairo pango
```
linux
```bash
sudo apt update
sudo apt install ffmpeg sox cairo pango python3-pip
```
## python-env
```bash
python3 -m venv manim-env
source manim-env/bin/activate  # Linux/macOS
.\manim-env\Scripts\activate   # Windows
```

## install requirement
```bash
pip install manim
```

## render video
```bash
manim -pql example.py HelloWorld
```
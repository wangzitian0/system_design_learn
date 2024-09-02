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
test only
```bash
manim -pql playground/helloworld.py HelloWorld
```
my build.sh
```bash
# quick preview
./build.sh quick playground/helloworld.py
# std preview
./build.sh std playground/helloworld.py
# release: to release/playground/helloworld-1634567890.mov
./build.sh release playground/helloworld.py
```

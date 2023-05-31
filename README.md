# Directory-Visualizer
A Python Class that takes a directory as input, and prints out the structure in an easy to read format

Idea was taken from the way the [wiiu.hacks.guide](https://wiiu.hacks.guide) website displays their SD-Card layout(s).

## Usage

```python
root_dir = './Shine'
dir = DirectoryPrinter(root_dir)
dir.print_dir()
```

## Sample output

```text
📂 Shine:
 ┣  📂 Classes:
 ┣   ┣ 📜 Commands.py
 ┣   ┣ 📜 ErrorWindow.py
 ┣   ┣ 📜 Errors.py
 ┣   ┣ 📜 InfoWindow.py
 ┣   ┣ 📜 Memory.py
 ┣   ┣ 📜 Verification.py
 ┣   ┣  📂 __pycache__:
 ┣   ┣   ┣ 📜 Commands.cpython-310.pyc
 ┣   ┣   ┣ 📜 Commands.cpython-311.pyc
 ┣   ┣   ┣ 📜 ErrorWindow.cpython-310.pyc
 ┣   ┣   ┣ 📜 ErrorWindow.cpython-311.pyc
 ┣   ┣   ┣ 📜 Errors.cpython-310.pyc
 ┣   ┣   ┣ 📜 Errors.cpython-311.pyc
 ┣   ┣   ┣ 📜 InfoWindow.cpython-310.pyc
 ┣   ┣   ┣ 📜 InfoWindow.cpython-311.pyc
 ┣   ┣   ┣ 📜 Memory.cpython-310.pyc
 ┣   ┣   ┣ 📜 Memory.cpython-311.pyc
 ┣   ┣   ┣ 📜 Verification.cpython-310.pyc
 ┣   ┣   ┣ 📜 Verification.cpython-311.pyc
 ┣   ┣   ┣ 📜 uGecko.cpython-310.pyc
 ┣   ┣   ┗ 📜 uGecko.cpython-311.pyc
 ┣   ┗ 📜 uGecko.py
 ┣ 📜 ShineClientSender.py
 ┣ 📜 ShineClientSender.spec
 ┣  📂 build:
 ┣      📂 ShineClientSender:
 ┣       ┣ 📜 Analysis-00.toc
 ┣       ┣ 📜 EXE-00.toc
 ┣       ┣ 📜 PKG-00.toc
 ┣       ┣ 📜 PYZ-00.pyz
 ┣       ┣ 📜 PYZ-00.toc
 ┣       ┣ 📜 ShineClientSender.exe.manifest
 ┣       ┣ 📜 ShineClientSender.pkg
 ┣       ┣ 📜 base_library.zip
 ┣       ┣  📂 localpycs:
 ┣       ┣   ┣ 📜 pyimod01_archive.pyc
 ┣       ┣   ┣ 📜 pyimod02_importers.pyc
 ┣       ┣   ┣ 📜 pyimod03_ctypes.pyc
 ┣       ┣   ┣ 📜 pyimod04_pywin32.pyc
 ┣       ┣   ┗ 📜 struct.pyc
 ┣       ┣ 📜 warn-ShineClientSender.txt
 ┣       ┗ 📜 xref-ShineClientSender.html
    📂 dist:
     ┗ 📜 ShineClientSender.exe
```

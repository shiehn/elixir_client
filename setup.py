from setuptools import setup, find_packages
import subprocess


def is_ffmpeg_installed():
    try:
        subprocess.run(
            ["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return True
    except FileNotFoundError:
        return False


ffmpeg_warning_msg = """
Warning: FFmpeg is not installed on your system, which is required for some functionalities of this package.
Please install FFmpeg using the following instructions:

- For macOS:
  Install FFmpeg using Homebrew: `brew install ffmpeg`

- For Linux (Debian/Ubuntu):
  Install FFmpeg using apt: `sudo apt-get install ffmpeg`

After installing, ensure that FFmpeg is in your PATH.
"""

if not is_ffmpeg_installed():
    print(ffmpeg_warning_msg)

setup(
    name="runes-client",
    version="0.9.4",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "websockets",
        "nest-asyncio",
        "sentry-sdk",
        "pydub",
        "librosa",
        "pytest-asyncio",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "runes-client=runes_client.core:main",
        ],
    },
    # Additional metadata about your package
    author="Steve Hiehn",
    author_email="stevehiehn@gmail.com",
    description="Runes client enables remote execution of python code triggered from a Crucible Plugin on the Signals & Sorcery platform.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://signalsandsorcery.app",
)

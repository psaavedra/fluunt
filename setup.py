from setuptools import setup, find_packages

version = "0.1.0"

long_description = ""
try:
    long_description=file('README').read()
except Exception:
    pass

license = ""
try:
    license=file('MIT_License.txt').read()
except Exception:
    pass


setup(
    name = 'fluunt',
    version = version,
    description = 'Video stream server (HLS, HTTP, HTTP-FLV, time-shift, image server)',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/fluunt',
    packages = find_packages(),
    package_data={
    },
    zip_safe=False,
    install_requires=[
        "paste",
    ],
    scripts=[
        "tools/fluunt-server",
        "tools/fluunt-cleaner",
        "tools/fluunt-recorder",
        "tools/fluunt-image-server",
        "tools/fluunt-watchdog",
    ],
    data_files=[
        ('share/doc/fluunt', [
            'doc/fluunt-server.cfg',
            'doc/fluunt-cleaner.cfg',
            'doc/fluunt-recorder.cfg',
            'README',
            'AUTHORS',
                ])
    ],
    download_url= 'https://github.com/psaavedra/fluunt/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "python stream pvr live h264 mpegts flv hls images",
)

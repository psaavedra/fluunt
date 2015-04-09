from setuptools import setup, find_packages

version = "1.0.0"

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
    author_email = 'saavedra.pablo@gmail.com',
    url = 'http://github.com/psaavedra/fluunt',
    packages = find_packages(),
    package_data={
    },
    zip_safe=False,
    install_requires=[
        "paste >=1.7.5.1",
        "requests >=2.3.0",
        "bottle >=0.11.5"
    ],
    scripts=[
        "tools/fluunt-server",
        "tools/fluunt-cleaner",
        "tools/fluunt-recorder",
        "tools/fluunt-image-server",
        "tools/fluunt-watchdog",
    ],
    data_files=[
        ('/usr/share/doc/fluunt', [
            'README',
            'AUTHORS',
                ]),
        ('/etc/supervisor/conf.d/', [
            'cfg/supervisor/fluunt.conf',
                ]),
        ('/etc/supervisor/conf.d/', [
            'cfg/supervisor/fluunt-image-server.conf',
                ]),
        ('/etc/logrotate.d/', [
            'cfg/logrotate/fluunt',
                ]),
        ('/etc/cron.d/', [
            'cfg/crond/fluunt',
                ])

    ],
    download_url= 'https://github.com/psaavedra/fluunt/zipball/master',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "python stream pvr live h264 mpegts flv hls images convert",
)

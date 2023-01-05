import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="tktimepicker",
    version=1.0,
    author="Jack Horvath",
    author_email="jmhorvath65@gmail.com",
    description="An altered version of tktimepicker to work with Reddcat.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bluejay65/tkTimePicker",
    packages=setuptools.find_packages(where='src'),
    license='MIT License',
    install_requires=['tk'],
    keywords='tkinter tktimepicker',
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

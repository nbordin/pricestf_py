import setuptools


with open("./README.md") as f:
    README = f.read()

setuptools.setup(
    author="Nicolò Bordin",
    author_email="nicolofbordin@gmail.com",
    name="pricestf_py",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    description="pricestf_py is a library to get Team Fortress 2 items' prices from prices.tf API.",
    version="0.1.2",
    url="https://github.com/nbordin/pricestf_py",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["requests"],
)

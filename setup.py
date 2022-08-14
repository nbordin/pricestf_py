import setuptools


setuptools.setup(
    author="Nicolò Bordin",
    author_email="nicolofbordin@gmail.com",
    name="pricestf_py",
    license="MIT",
    description="Python API for prices.tf website.",
    version="0.1.0",
    url="https://github.com/nbordin/pricestf_py",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["requests"],
)

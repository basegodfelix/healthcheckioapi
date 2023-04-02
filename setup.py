import setuptools

setuptools.setup(
    name="HealthCheckIOAPI",
    version="1.0.0",
    author="Felix Hernandez",
    description="Simple Python Tooling to interact with Healthcheck.io projects.",
    packages=["healthcheckio"],
    install_requires=["requests"]
)
# coding: utf-8

"""
    FIX Gateway Commander API

    # FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                         # noqa: E501

    OpenAPI spec version: 0.1
    Contact: dmtsyganov@devexperts.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="FIX Gateway Commander API",
    author_email="dmtsyganov@devexperts.com",
    url="",
    keywords=["Swagger", "FIX Gateway Commander API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    # FIX Gateway Commander API REST API to get status and to send control commands to FIX Gateway.  Configuration API allows to view and update FIX Gateway session configuration.                         # noqa: E501
    """
)

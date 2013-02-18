from setuptools import setup

setup(
    name="django-globetrotter",
    version="0.0.1",
    description="Extra i18n + l10n tools for Django",
    long_description="Extra i18n + l10n tools for Django",
    keywords="django, i18n, l10n",
    author="Jared Morse <jarcoal@gmail.com>",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/django-globetrotter",
    license="BSD",
    packages=["globetrotter"],
    zip_safe=False,
    install_requires=['pytz'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)

extinfo
======================
|LANGUAGE| |VERSION| |LICENSE| |MAINTAINED| |STYLE|

.. |LICENSE| image:: https://img.shields.io/badge/license-Apache%202.0-informational
   :target: https://www.apache.org/licenses/LICENSE-2.0.txt
.. |MAINTAINED| image:: https://img.shields.io/maintenance/yes/2022?logoColor=informational
.. |VERSION| image:: https://img.shields.io/pypi/v/extinfo
   :target: https://pypi.org/project/extinfo
.. |STYLE| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |LANGUAGE| image:: https://img.shields.io/pypi/pyversions/extinfo

Given a file extension, extinfo will scrape web sources for information about
what type of file is usually named with that extension.

If you want to know what's in an actual file you have on disk, you should use
the file command or another tool that leverages libmagic.

Installation
------------

.. code-block :: console

    pip3 install extinfo

Usage
-----

.. code-block :: console

    $ extinfo jpeg | fmt
    From https://fileinfo.com/extension/jpeg

    # JPEG Image

    A JPEG file is an image saved in a compressed graphic format standardized
    by the Joint Photographic Experts Group (JPEG). It supports up to 24-bit
    color and is compressed using lossy compression, which may noticeably
    reduce the image quality if high amounts of compression are used. JPEG
    files are commonly used for storing digital photos and web graphics.


    # What is a JPEG file?

    JPEG file open in Microsoft Windows Photos

    In the early 1980s, no technology existed that allowed users to easily
    compress and share digital images with one another. In 1982, the JPEG
    workgroup began designing a compression standard that could be used to
    reduce image files' size, making them easier to share, while retaining
    as much of their quality as possible.

    In 1992, the workgroup created the JPEG file format. JPEG files are images
    created using a lossy compression algorithm, which actually destroys some
    data contained within the original image file. However, this data loss is
    mostly unnoticeable to the human eye. Because the JPEG standard continues
    to allows users to produce sharable, high-quality image files, and because
    it is so embedded within technologies used to create and share images,
    it is still the most common image compression standard in use today.

    NOTE: A JPEG file also contains metadata that describes the contents of
    its file, such as the color space, color profile, and image dimension
    information. Image files saved in the JPEG format are more commonly
    appended with the .JPG extension than the JPEG extension.

============
Development
============

To install development dependencies, you will need `poetry <https://docs.pipenv.org/en/latest/>`_
and `pre-commit <https://pre-commit.com/>`_.

.. code-block :: console

    pre-commit install --install-hooks
    poetry install && poetry shell

`direnv <https://direnv.net/>`_ is optional, but recommended for convenience.

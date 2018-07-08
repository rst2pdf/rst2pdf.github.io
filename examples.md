---
title: rst2pdf: Examples
---

# rst2pdf Examples

Here are a few examples of the kinds of things that rst2pdf can do, along with the source and style files so that you can use them as starting points for your own projects.  You are very welcome to suggest additional examples by opening an issue on [our source repo](https://github.com/rst2pdf/rst2pdf.github.io) and to add your own examples - follow the `CONTRIBUTING.md` file for more information.

## Basic Document

A simple document with some headings and the basic rst2pdf styling.

<img src="../examples/document1/document1-thumbnail.png" />

* **PDF:** [document1.pdf](../examples/document1/document1.pdf)
* **Content**: [document1.rst](../examples/document1/document1.rst)
* **Style**: (no style applied)
* **Command:** rst2pdf document1.rst

## Document with Simple Styling

The same basic document with some styles added.

<img src="../examples/document1/document1-simple-thumbnail.png" />

* **PDF:** [document1-simple.pdf](../examples/document1/document1-simple.pdf)
* **Content**: [document1.rst](../examples/document1/document1.rst)
* **Style**: [simple.style](../examples/document1/simple.style)
* **Command:** rst2pdf --stylesheets=simple.style document1.rst document1-simple.pdf


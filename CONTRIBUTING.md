# Contributing

Please feel free to add to or edit this website, we love input!

## TL;DR

Please fork, branch and open a pull request.

## More Detailed Instructions

To send changes to this repository, first create your own fork of the project.

Then, create a branch on your fork - name your branch after the feature or fix it will include.

Make changes, and commit them to your new branch.  Then open a pull request, and tell us what you have changed and why.

That's it - but if you have questions, feel free to open an issue to start a discussion or ask for help!

## Adding Examples

To add an example to our examples page, create a new directory for your example inside `/examples`, add the `.rst` source code and any style information needed.

Generate a PDF so we others can see what you made without needing to compile it!

If you have imagemagick installed, generate the thumbnail for your example using a command like: `convert document1.pdf[0] -resize 20% document1-thumbnail.png`.  If you don't have imagemagic or have no idea what this means, don't worry, we can add this when we review the pull request.

Add a new section to the `examples.rst` file with a title, a thumbnail, and links to the ReStructured Text source, style file and resulting PDF.  Also include the command to generate the output shown.

Now open a pull request - see examples above.  You can always open an issue to get some help or advice!

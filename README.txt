IdiotScript

This is a python port of https://github.com/mooshmoosh/IdiotScript

Three sentence description
Like mooshmoosh, I also have great difficulty remembering how to use
regular expressions. However, python is my choice of language. Now
it's even easier for everyone to use and extend IdiotScript!

The main goal of this port to python is to provide more control over
how the pointer is moved when various operations are carried out. I
would highly recommend reading over the readme file in mooshmoosh's
repository before progressing any further.

This version differs from mooshmoosh's version in a few key ways.

First off, this is designed to be used as a library rather than a
monolithic script. This means each component is pluggable. An example
script is provided in the repository for reference.

There are more instructions in the standard instruction set, and some
of them behave slightly differently. The main additions are the 'search
up till' and 'copy till with' instructions. 'search up till' allows you
to search for a particular string of text, but not move the pointer
past that text. Similarly, 'copy till with' allows you to copy
everything up to AND including the search term.

The other big change is how branching works. This version of
IdiotScript introduces proper if/elseif/else branching with 'if you
find', 'or if you find' and 'otherwise'. Also, if/elseif statements do
not move the pointer.

Of course, the great thing about everything in this version being
pluggable is that you can throw out the built-in instructions and use
your own instruction set. If you want if/elseif statements that move
the pointer, you can do just that.

Finally, there's a small hack in place to allow you to represent
newline characters in your scripts. Instances of '\n' will be
converted to actual newline characters when the script is parsed.

This software is released into the public domain without any warranty.

# truss-take-home (with stdin)
I was not able to do it within the 4 hour window, but I was curious and kept going so I submit this branch as a talking point. I wanted to use csv.reader() but that would only accept file objects and list objects (iterable things). This made it difficult to pivot to using stdin, because I had to figure out a way to read from stdin, encode it without failing or replacing characters, and then create some sort of iterable from it. Ideally, I could turn stdin buffer into a file object.

At last, I found the function, sys.stdin.fileno(), that allowed me to the stdin buffer's fileno (file descriptor number) as the path destination for open(). I don't fully understand this, but it's good to know!

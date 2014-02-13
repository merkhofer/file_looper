File Looper
===========

The file looper is a simple utility to serve up the next line of a file. It creates a generator that goes through the entire file, start from (then ending immediately before) any arbitrary offset.

One use is to loop through x times, or start somewhere other than the beginning. But since it's using File.seek() to make sure it's at the right offset before returning any lines, this is not particularly efficient.

I made this because I had the idea to have multiple generators independently reading the same file line-by-line in a larger program.

That's probably not something you should actually need to do. But I wanted to once, in the words of Cal Naughton Junior, [because I like to party.](http://www.youtube.com/watch?v=SS_OVZtVa4E)


Sample use:
````
fl = FileLooper(open('../12.txt', 'r'), num_loops=3)
print fl.return_line()
for l in fl.line():
    print l
fl.add_loop()
print fl.return_line()
````

# squishJpg
A python script to reduce the dimensions of a folder of .jpg files. 

# Problem: 

I had to send an image of every page of my passport to the person helping me with an immigration matter. However, I had grabbed them all using my phone and the file sizes were unreasonably large.

I quickly realized that the Python library, Pillow, would be the fastest way of doing this. Resizing them all by hand in GIMP? No thanks. 

My issue? I'm not a Python dev. And I didn't feel like spending my afternoon learning to do this myself.

# My solution

A simple ChatGPT prompt:

> I need you to write me a Python 3 script. The requirements are as follows:
> 1. the script will run from the project's root directory
> 2. It will import all the .jpg files from a /working directory
> 3. It will use the Python Library "Pillow" to reduce each jpg to 20% of its original dimensions
> 4. The resized files should be a written to a /output directory

ChatGPT's code can me found in this projects' squishJpg.py file. 

It worked perfectly.

# License

I claim no ownership over this code. I didn't write it and who the hell knows where ChatGPT stole it from :D

Do what you want as far as I'm concerned.

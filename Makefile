all: picmaker.py
		python picmaker.py
		magick convert image.ppm image.png
		imdisplay image.png
clean:
		rm *.ppm
		rm *.png

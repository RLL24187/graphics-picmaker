all: picmaker.py
		python picmaker.py
		convert image.ppm image.png
		display image.png
clean:
		rm *.ppm
		rm *.png

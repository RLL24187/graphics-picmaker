all: picmaker.py
		python picmaker.py
		convert image.ppm image.png
		echo image.png
clean:
		rm *.ppm
		rm *.png

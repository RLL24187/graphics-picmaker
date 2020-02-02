all: picmaker.py
		python picmaker.py
		echo image.png
clean:
		rm *.ppm
		rm *.png

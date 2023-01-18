all: builder.py
	python3 $<

clean:
	rm -rf *.o *.so _qd.c __pycache__

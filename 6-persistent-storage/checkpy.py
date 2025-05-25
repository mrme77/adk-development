import os

if 'VIRTUAL_ENV' in os.environ:
       print("Running inside a virtual environment.")
else:
       print("Not running inside a virtual environment.")


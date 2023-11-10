# wcsim2npz_custom
This code converts WCSim generated root files into npz numpy files easily handled with python/numpy. For more details, https://numpy.org/doc/stable/reference/generated/numpy.load.html

## Requirements
 - numpy
 - root compiled with python

Make sure you define the WCSIMBUILD variable pointing to the foder containing the compiled WCSim library `libWCSimRoot.so` 

```
export WCSIMBUILD=/path/to/your/WCSim/build/directory
```


## Usage
```
python event_dump.py /path/to/your/wcsim/root/files*.root
```

The code will produce a `.npz` file of numpy arrays with the same name and in the same location as the input root files, but with the different extension.

## Reading npz files
The program `plot_npz.py` has a first simple attempt that takes a .npz file as input and loops over its variables.
```
python plot_npz.py /path/to/your/wcsim/root/file.npz
```

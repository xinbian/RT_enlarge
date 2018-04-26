#this file extract some datasets from one HDF5 file to another
#the application:1 HDF5 file run out of digits 2 want to change the domain ratio


#!/bin/bash

inFile="tests_single_new.h5"
outFile="temp.h5"
inTime="001000"
outTime="001000"


h5copy -p -i $inFile  -o $outFile -s /Fields/Prho/$inTime -d /Fields/Prho/$outTime
h5copy -p -i $inFile  -o $outFile -s /Fields/PPress/$inTime -d /Fields/PPress/$outTime
h5copy -p -i $inFile  -o $outFile -s /Fields/PVy/$inTime -d /Fields/PVy/$outTime
h5copy -p -i $inFile  -o $outFile -s /Fields/PVz/$inTime -d /Fields/PVz/$outTime



#this part just copying to another file, keeping same time stamp
#the apploication: hdf5 file is too large, extract some for post processing

inFile="tests_single_new.h5"
outFile="temp.h5"

for step in '020000' '030000' '040000' '050000'; do
	
	for var in 'Prho' 'PVx' 'PVy' 'PVz' 'PPress'; do 

		h5copy -p -i $inFile -o $outFile -s /Fields/$var/$step -d /Fields/$var/$step

		echo "copying $var variable, $step step"

	done


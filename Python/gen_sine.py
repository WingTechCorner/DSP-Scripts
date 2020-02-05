#!/usr/bin/env python

# Simple python script to generat a sine wave of a specific hz and a specific duration

import os,sys,math,argparse,csv

parser = argparse.ArgumentParser(description='Generate Sinewave.')
parser.add_argument('--hertz', dest='hertz', action='store', type=float, default=220.00, help='Frequency in hertz as a float value(default:220hz)')
parser.add_argument('--sample-rate', dest='sample_rate', action='store', type=float, default=44100.00, help='Sample rate as a float value(default:44100)')
parser.add_argument('--amplitude', dest='amplitude', action='store', type=float, default=1.00, help='Amplitude of values as float.(default:1.0)')
parser.add_argument('--duration', dest='duration', action='store', type=float, default=1.00, help='Duration of sample, in seconds.(default:1.0)')
parser.add_argument('--csv', dest='csv', action='store_true', default=False, help='Output in comma separated format.(Default:False)')
args = parser.parse_args()

# Setup variables
twopi = 2.00 * math.pi

# Steps per full circle
rad_step = float( twopi ) / float(args.sample_rate)

# Duration
rad_stop = float(args.duration) * twopi

# Starting point
rad_pos=0.00

# Ending point
index = 0
while (rad_pos <= rad_stop):
    if ( args.csv ):
        if ( ( rad_pos + rad_step ) > rad_stop ):
            print( math.sin( rad_pos * float(args.hertz) ))
        else:
            print( math.sin( rad_pos * float(args.hertz) ), ",")
    else:
        print( math.sin( rad_pos * float(args.hertz) ))
    rad_pos = rad_pos + rad_step

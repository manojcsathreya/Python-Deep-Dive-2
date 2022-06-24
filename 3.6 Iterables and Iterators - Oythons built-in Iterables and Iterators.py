'''
PYTHONS BUILT-IN ITERABLES AND ITERATORS

Python provides many functions that return iterables or iterators

Additionally, the iterators perform lazy evaluation

You should always be aware of whether you are dealing with an iterable or an iterator

why?    if an object is an iterable (but not an iterator) you can iterate over it many times
        if an object is an iterator you can iterate over it only once
------------------------------------------------------------------------------------------
range(10) →iterable

zip(l1, l2) →iterator

enumerate(l1) →iterator

open('cars.csv') →iterator

dictionary .keys() →iterable

dictionary .values() →iterable

dictionary .items() →iterable

'''
# =============================================================================
# Python's Built-In Iterables and Iterators
# Python has a lot of built-in functions that return iterators or iterables.
# 
# Let's look at the simple range function first:
# =============================================================================

r_10 = range(10)
#Now, r_10 is an iterable:

'__iter__' in dir(r_10)
#True
#But it is not an iterator:

'__next__' in dir(r_10)
# =============================================================================
# False
# However, we can request an iterator by calling the __iter__ method, or simply using the iter() function:
# =============================================================================

r_10_iter = iter(r_10)
#And of course this is now an iterator:

'__iter__' in dir(r_10_iter)
#True
'__next__' in dir(r_10_iter)
#True
#Most built-in iterables in Python use lazy evaluation (including the range) function - i.e. when we execute range(10) Python does no pre-compute a "list" of all the elements in the range. Instead it uses lazy evluation and the iterator computes and returns elements one at a time.

#This is why when we print a range object we do not actually see the contents of the range - they don't exist yet!

#Instead, we need to iterate through the iterator and put it into something like a list:

[num for num in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#The zip function on the other hand returns an iterator:

z = zip([1, 2, 3], 'abc')
z
# =============================================================================
# <zip at 0x28b01b684c8>
# It is an iterator:
# =============================================================================

print('__iter__' in dir(z))
print('__next__' in dir(z))
# =============================================================================
# True
# True
# Just like range() though, it also uses lazy evaluation, so we need to iterate through the iterator and make a list for example in order to see the contents:
# =============================================================================

list(z)
# =============================================================================
# [(1, 'a'), (2, 'b'), (3, 'c')]
# Even reading a file line by line is done using lazy evaluation:
# =============================================================================

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))
# =============================================================================
# <class '_io.TextIOWrapper'>
# True
# True
# =============================================================================
#As you can see, the open() function returns an iterator (of type TextIOWrapper), and we can read lines from the file one by one using the next() function, or calling the __next__() method. The class also implements a readline() method we can use to get the next row:

with open('cars.csv') as f:
    print(next(f))
    print(f.__next__())
    print(f.readline())
# =============================================================================
# Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
# 
# STRING;DOUBLE;INT;DOUBLE;DOUBLE;DOUBLE;DOUBLE;INT;CAT
# 
# Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US
# 
# Of course we can just iterate over all the lines using a for loop as well:
# =============================================================================

with open('cars.csv') as f:
    for row in f:
        print(row, end='')
        '''
Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
STRING;DOUBLE;INT;DOUBLE;DOUBLE;DOUBLE;DOUBLE;INT;CAT
Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US
Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US
Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US
AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US
Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US
Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US
Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US
Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US
Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US
AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US
Citroen DS-21 Pallas;0;4;133.0;115.0;3090.;17.5;70;Europe
Chevrolet Chevelle Concours (sw);0;8;350.0;165.0;4142.;11.5;70;US
Ford Torino (sw);0;8;351.0;153.0;4034.;11.0;70;US
Plymouth Satellite (sw);0;8;383.0;175.0;4166.;10.5;70;US
AMC Rebel SST (sw);0;8;360.0;175.0;3850.;11.0;70;US
Dodge Challenger SE;15.0;8;383.0;170.0;3563.;10.0;70;US
Plymouth 'Cuda 340;14.0;8;340.0;160.0;3609.;8.0;70;US
Ford Mustang Boss 302;0;8;302.0;140.0;3353.;8.0;70;US
Chevrolet Monte Carlo;15.0;8;400.0;150.0;3761.;9.5;70;US
Buick Estate Wagon (sw);14.0;8;455.0;225.0;3086.;10.0;70;US
Toyota Corolla Mark ii;24.0;4;113.0;95.00;2372.;15.0;70;Japan
Plymouth Duster;22.0;6;198.0;95.00;2833.;15.5;70;US
AMC Hornet;18.0;6;199.0;97.00;2774.;15.5;70;US
Ford Maverick;21.0;6;200.0;85.00;2587.;16.0;70;US
Datsun PL510;27.0;4;97.00;88.00;2130.;14.5;70;Japan
Volkswagen 1131 Deluxe Sedan;26.0;4;97.00;46.00;1835.;20.5;70;Europe
Peugeot 504;25.0;4;110.0;87.00;2672.;17.5;70;Europe
Audi 100 LS;24.0;4;107.0;90.00;2430.;14.5;70;Europe
Saab 99e;25.0;4;104.0;95.00;2375.;17.5;70;Europe
BMW 2002;26.0;4;121.0;113.0;2234.;12.5;70;Europe
AMC Gremlin;21.0;6;199.0;90.00;2648.;15.0;70;US
Ford F250;10.0;8;360.0;215.0;4615.;14.0;70;US
Chevy C20;10.0;8;307.0;200.0;4376.;15.0;70;US
Dodge D200;11.0;8;318.0;210.0;4382.;13.5;70;US
Hi 1200D;9.0;8;304.0;193.0;4732.;18.5;70;US
Datsun PL510;27.0;4;97.00;88.00;2130.;14.5;71;Japan
Chevrolet Vega 2300;28.0;4;140.0;90.00;2264.;15.5;71;US
Toyota Corolla;25.0;4;113.0;95.00;2228.;14.0;71;Japan
Ford Pinto;25.0;4;98.00;0;2046.;19.0;71;US
Volkswagen Super Beetle 117;0;4;97.00;48.00;1978.;20.0;71;Europe
AMC Gremlin;19.0;6;232.0;100.0;2634.;13.0;71;US
Plymouth Satellite Custom;16.0;6;225.0;105.0;3439.;15.5;71;US
Chevrolet Chevelle Malibu;17.0;6;250.0;100.0;3329.;15.5;71;US
Ford Torino 500;19.0;6;250.0;88.00;3302.;15.5;71;US
AMC Matador;18.0;6;232.0;100.0;3288.;15.5;71;US
Chevrolet Impala;14.0;8;350.0;165.0;4209.;12.0;71;US
Pontiac Catalina Brougham;14.0;8;400.0;175.0;4464.;11.5;71;US
Ford Galaxie 500;14.0;8;351.0;153.0;4154.;13.5;71;US
Plymouth Fury iii;14.0;8;318.0;150.0;4096.;13.0;71;US
Dodge Monaco (sw);12.0;8;383.0;180.0;4955.;11.5;71;US
Ford Country Squire (sw);13.0;8;400.0;170.0;4746.;12.0;71;US
Pontiac Safari (sw);13.0;8;400.0;175.0;5140.;12.0;71;US
AMC Hornet Sportabout (sw);18.0;6;258.0;110.0;2962.;13.5;71;US
Chevrolet Vega (sw);22.0;4;140.0;72.00;2408.;19.0;71;US
Pontiac Firebird;19.0;6;250.0;100.0;3282.;15.0;71;US
Ford Mustang;18.0;6;250.0;88.00;3139.;14.5;71;US
Mercury Capri 2000;23.0;4;122.0;86.00;2220.;14.0;71;US
Opel 1900;28.0;4;116.0;90.00;2123.;14.0;71;Europe
Peugeot 304;30.0;4;79.00;70.00;2074.;19.5;71;Europe
Fiat 124B;30.0;4;88.00;76.00;2065.;14.5;71;Europe
Toyota Corolla 1200;31.0;4;71.00;65.00;1773.;19.0;71;Japan
Datsun 1200;35.0;4;72.00;69.00;1613.;18.0;71;Japan
Volkswagen Model 111;27.0;4;97.00;60.00;1834.;19.0;71;Europe
Plymouth Cricket;26.0;4;91.00;70.00;1955.;20.5;71;US
Toyota Corolla Hardtop;24.0;4;113.0;95.00;2278.;15.5;72;Japan
Dodge Colt Hardtop;25.0;4;97.50;80.00;2126.;17.0;72;US
Volkswagen Type 3;23.0;4;97.00;54.00;2254.;23.5;72;Europe
Chevrolet Vega;20.0;4;140.0;90.00;2408.;19.5;72;US
Ford Pinto Runabout;21.0;4;122.0;86.00;2226.;16.5;72;US
Chevrolet Impala;13.0;8;350.0;165.0;4274.;12.0;72;US
Pontiac Catalina;14.0;8;400.0;175.0;4385.;12.0;72;US
Plymouth Fury III;15.0;8;318.0;150.0;4135.;13.5;72;US
Ford Galaxie 500;14.0;8;351.0;153.0;4129.;13.0;72;US
AMC Ambassador SST;17.0;8;304.0;150.0;3672.;11.5;72;US
Mercury Marquis;11.0;8;429.0;208.0;4633.;11.0;72;US
Buick LeSabre Custom;13.0;8;350.0;155.0;4502.;13.5;72;US
Oldsmobile Delta 88 Royale;12.0;8;350.0;160.0;4456.;13.5;72;US
Chrysler Newport Royal;13.0;8;400.0;190.0;4422.;12.5;72;US
Mazda RX2 Coupe;19.0;3;70.00;97.00;2330.;13.5;72;Japan
AMC Matador (sw);15.0;8;304.0;150.0;3892.;12.5;72;US
Chevrolet Chevelle Concours (sw);13.0;8;307.0;130.0;4098.;14.0;72;US
Ford Gran Torino (sw);13.0;8;302.0;140.0;4294.;16.0;72;US
Plymouth Satellite Custom (sw);14.0;8;318.0;150.0;4077.;14.0;72;US
Volvo 145e (sw);18.0;4;121.0;112.0;2933.;14.5;72;Europe
Volkswagen 411 (sw);22.0;4;121.0;76.00;2511.;18.0;72;Europe
Peugeot 504 (sw);21.0;4;120.0;87.00;2979.;19.5;72;Europe
Renault 12 (sw);26.0;4;96.00;69.00;2189.;18.0;72;Europe
Ford Pinto (sw);22.0;4;122.0;86.00;2395.;16.0;72;US
Datsun 510 (sw);28.0;4;97.00;92.00;2288.;17.0;72;Japan
Toyota Corolla Mark II (sw);23.0;4;120.0;97.00;2506.;14.5;72;Japan
Dodge Colt (sw);28.0;4;98.00;80.00;2164.;15.0;72;US
Toyota Corolla 1600 (sw);27.0;4;97.00;88.00;2100.;16.5;72;Japan
Buick Century 350;13.0;8;350.0;175.0;4100.;13.0;73;US
AMC Matador;14.0;8;304.0;150.0;3672.;11.5;73;US
Chevrolet Malibu;13.0;8;350.0;145.0;3988.;13.0;73;US
Ford Gran Torino;14.0;8;302.0;137.0;4042.;14.5;73;US
Dodge Coronet Custom;15.0;8;318.0;150.0;3777.;12.5;73;US
Mercury Marquis Brougham;12.0;8;429.0;198.0;4952.;11.5;73;US
Chevrolet Caprice Classic;13.0;8;400.0;150.0;4464.;12.0;73;US
Ford LTD;13.0;8;351.0;158.0;4363.;13.0;73;US
Plymouth Fury Gran Sedan;14.0;8;318.0;150.0;4237.;14.5;73;US
Chrysler New Yorker Brougham;13.0;8;440.0;215.0;4735.;11.0;73;US
Buick Electra 225 Custom;12.0;8;455.0;225.0;4951.;11.0;73;US
AMC Ambassador Brougham;13.0;8;360.0;175.0;3821.;11.0;73;US
Plymouth Valiant;18.0;6;225.0;105.0;3121.;16.5;73;US
Chevrolet Nova Custom;16.0;6;250.0;100.0;3278.;18.0;73;US
AMC Hornet;18.0;6;232.0;100.0;2945.;16.0;73;US
Ford Maverick;18.0;6;250.0;88.00;3021.;16.5;73;US
Plymouth Duster;23.0;6;198.0;95.00;2904.;16.0;73;US
Volkswagen Super Beetle;26.0;4;97.00;46.00;1950.;21.0;73;Europe
Chevrolet Impala;11.0;8;400.0;150.0;4997.;14.0;73;US
Ford Country;12.0;8;400.0;167.0;4906.;12.5;73;US
Plymouth Custom Suburb;13.0;8;360.0;170.0;4654.;13.0;73;US
Oldsmobile Vista Cruiser;12.0;8;350.0;180.0;4499.;12.5;73;US
AMC Gremlin;18.0;6;232.0;100.0;2789.;15.0;73;US
Toyota Camry;20.0;4;97.00;88.00;2279.;19.0;73;Japan
Chevrolet Vega;21.0;4;140.0;72.00;2401.;19.5;73;US
Datsun 610;22.0;4;108.0;94.00;2379.;16.5;73;Japan
Mazda RX3;18.0;3;70.00;90.00;2124.;13.5;73;Japan
Ford Pinto;19.0;4;122.0;85.00;2310.;18.5;73;US
Mercury Capri v6;21.0;6;155.0;107.0;2472.;14.0;73;US
Fiat 124 Sport Coupe;26.0;4;98.00;90.00;2265.;15.5;73;Europe
Chevrolet Monte Carlo S;15.0;8;350.0;145.0;4082.;13.0;73;US
Pontiac Grand Prix;16.0;8;400.0;230.0;4278.;9.50;73;US
Fiat 128;29.0;4;68.00;49.00;1867.;19.5;73;Europe
Opel Manta;24.0;4;116.0;75.00;2158.;15.5;73;Europe
Audi 100LS;20.0;4;114.0;91.00;2582.;14.0;73;Europe
Volvo 144ea;19.0;4;121.0;112.0;2868.;15.5;73;Europe
Dodge Dart Custom;15.0;8;318.0;150.0;3399.;11.0;73;US
Saab 99le;24.0;4;121.0;110.0;2660.;14.0;73;Europe
Toyota Mark II;20.0;6;156.0;122.0;2807.;13.5;73;Japan
Oldsmobile Omega;11.0;8;350.0;180.0;3664.;11.0;73;US
Plymouth Duster;20.0;6;198.0;95.00;3102.;16.5;74;US
Ford Maverick;21.0;6;200.0;0;2875.;17.0;74;US
AMC Hornet;19.0;6;232.0;100.0;2901.;16.0;74;US
Chevrolet Nova;15.0;6;250.0;100.0;3336.;17.0;74;US
Datsun B210;31.0;4;79.00;67.00;1950.;19.0;74;Japan
Ford Pinto;26.0;4;122.0;80.00;2451.;16.5;74;US
Toyota Corolla 1200;32.0;4;71.00;65.00;1836.;21.0;74;Japan
Chevrolet Vega;25.0;4;140.0;75.00;2542.;17.0;74;US
Chevrolet Chevelle Malibu Classic;16.0;6;250.0;100.0;3781.;17.0;74;US
AMC Matador;16.0;6;258.0;110.0;3632.;18.0;74;US
Plymouth Satellite Sebring;18.0;6;225.0;105.0;3613.;16.5;74;US
Ford Gran Torino;16.0;8;302.0;140.0;4141.;14.0;74;US
Buick Century Luxus (sw);13.0;8;350.0;150.0;4699.;14.5;74;US
Dodge Coronet Custom (sw);14.0;8;318.0;150.0;4457.;13.5;74;US
Ford Gran Torino (sw);14.0;8;302.0;140.0;4638.;16.0;74;US
AMC Matador (sw);14.0;8;304.0;150.0;4257.;15.5;74;US
Audi Fox;29.0;4;98.00;83.00;2219.;16.5;74;Europe
Volkswagen Dasher;26.0;4;79.00;67.00;1963.;15.5;74;Europe
Opel Manta;26.0;4;97.00;78.00;2300.;14.5;74;Europe
Toyota Corolla;31.0;4;76.00;52.00;1649.;16.5;74;Japan
Datsun 710;32.0;4;83.00;61.00;2003.;19.0;74;Japan
Dodge Colt;28.0;4;90.00;75.00;2125.;14.5;74;US
Fiat 128;24.0;4;90.00;75.00;2108.;15.5;74;Europe
Fiat 124 TC;26.0;4;116.0;75.00;2246.;14.0;74;Europe
Honda Civic;24.0;4;120.0;97.00;2489.;15.0;74;Japan
Subaru;26.0;4;108.0;93.00;2391.;15.5;74;Japan
Fiat x1.9;31.0;4;79.00;67.00;2000.;16.0;74;Europe
Plymouth Valiant Custom;19.0;6;225.0;95.00;3264.;16.0;75;US
Chevrolet Nova;18.0;6;250.0;105.0;3459.;16.0;75;US
Mercury Monarch;15.0;6;250.0;72.00;3432.;21.0;75;US
Ford Maverick;15.0;6;250.0;72.00;3158.;19.5;75;US
Pontiac Catalina;16.0;8;400.0;170.0;4668.;11.5;75;US
Chevrolet Bel Air;15.0;8;350.0;145.0;4440.;14.0;75;US
Plymouth Grand Fury;16.0;8;318.0;150.0;4498.;14.5;75;US
Ford LTD;14.0;8;351.0;148.0;4657.;13.5;75;US
Buick Century;17.0;6;231.0;110.0;3907.;21.0;75;US
Chevrolete Chevelle Malibu;16.0;6;250.0;105.0;3897.;18.5;75;US
AMC Matador;15.0;6;258.0;110.0;3730.;19.0;75;US
Plymouth Fury;18.0;6;225.0;95.00;3785.;19.0;75;US
Buick Skyhawk;21.0;6;231.0;110.0;3039.;15.0;75;US
Chevrolet Monza 2+2;20.0;8;262.0;110.0;3221.;13.5;75;US
Ford Mustang II;13.0;8;302.0;129.0;3169.;12.0;75;US
Toyota Corolla;29.0;4;97.00;75.00;2171.;16.0;75;Japan
Ford Pinto;23.0;4;140.0;83.00;2639.;17.0;75;US
AMC Gremlin;20.0;6;232.0;100.0;2914.;16.0;75;US
Pontiac Astro;23.0;4;140.0;78.00;2592.;18.5;75;US
Toyota Corolla;24.0;4;134.0;96.00;2702.;13.5;75;Japan
Volkswagen Dasher;25.0;4;90.00;71.00;2223.;16.5;75;Europe
Datsun 710;24.0;4;119.0;97.00;2545.;17.0;75;Japan
Ford Pinto;18.0;6;171.0;97.00;2984.;14.5;75;US
Volkswagen Rabbit;29.0;4;90.00;70.00;1937.;14.0;75;Europe
AMC Pacer;19.0;6;232.0;90.00;3211.;17.0;75;US
Audi 100LS;23.0;4;115.0;95.00;2694.;15.0;75;Europe
Peugeot 504;23.0;4;120.0;88.00;2957.;17.0;75;Europe
Volvo 244DL;22.0;4;121.0;98.00;2945.;14.5;75;Europe
Saab 99LE;25.0;4;121.0;115.0;2671.;13.5;75;Europe
Honda Civic CVCC;33.0;4;91.00;53.00;1795.;17.5;75;Japan
Fiat 131;28.0;4;107.0;86.00;2464.;15.5;76;Europe
Opel 1900;25.0;4;116.0;81.00;2220.;16.9;76;Europe
Capri ii;25.0;4;140.0;92.00;2572.;14.9;76;US
Dodge Colt;26.0;4;98.00;79.00;2255.;17.7;76;US
Renault 12tl;27.0;4;101.0;83.00;2202.;15.3;76;Europe
Chevrolet Chevelle Malibu Classic;17.5;8;305.0;140.0;4215.;13.0;76;US
Dodge Coronet Brougham;16.0;8;318.0;150.0;4190.;13.0;76;US
AMC Matador;15.5;8;304.0;120.0;3962.;13.9;76;US
Ford Gran Torino;14.5;8;351.0;152.0;4215.;12.8;76;US
Plymouth Valiant;22.0;6;225.0;100.0;3233.;15.4;76;US
Chevrolet Nova;22.0;6;250.0;105.0;3353.;14.5;76;US
Ford Maverick;24.0;6;200.0;81.00;3012.;17.6;76;US
AMC Hornet;22.5;6;232.0;90.00;3085.;17.6;76;US
Chevrolet Chevette;29.0;4;85.00;52.00;2035.;22.2;76;US
Chevrolet Woody;24.5;4;98.00;60.00;2164.;22.1;76;US
Volkswagen Rabbit;29.0;4;90.00;70.00;1937.;14.2;76;Europe
Honda Civic;33.0;4;91.00;53.00;1795.;17.4;76;Japan
Dodge Aspen SE;20.0;6;225.0;100.0;3651.;17.7;76;US
Ford Grenada ghia;18.0;6;250.0;78.00;3574.;21.0;76;US
Pontiac Ventura SJ;18.5;6;250.0;110.0;3645.;16.2;76;US
AMC Pacer d/l;17.5;6;258.0;95.00;3193.;17.8;76;US
Volkswagen Rabbit;29.5;4;97.00;71.00;1825.;12.2;76;Europe
Datsun B-210;32.0;4;85.00;70.00;1990.;17.0;76;Japan
Toyota Corolla;28.0;4;97.00;75.00;2155.;16.4;76;Japan
Ford Pinto;26.5;4;140.0;72.00;2565.;13.6;76;US
Volvo 245;20.0;4;130.0;102.0;3150.;15.7;76;Europe
Plymouth Volare Premier v8;13.0;8;318.0;150.0;3940.;13.2;76;US
Peugeot 504;19.0;4;120.0;88.00;3270.;21.9;76;Europe
Toyota Mark II;19.0;6;156.0;108.0;2930.;15.5;76;Japan
Mercedes-Benz 280s;16.5;6;168.0;120.0;3820.;16.7;76;Europe
Cadillac Seville;16.5;8;350.0;180.0;4380.;12.1;76;US
Chevrolet C10;13.0;8;350.0;145.0;4055.;12.0;76;US
Ford F108;13.0;8;302.0;130.0;3870.;15.0;76;US
Dodge D100;13.0;8;318.0;150.0;3755.;14.0;76;US
Honda Accord CVCC;31.5;4;98.00;68.00;2045.;18.5;77;Japan
Buick Opel Isuzu Deluxe;30.0;4;111.0;80.00;2155.;14.8;77;US
Renault 5 GTL;36.0;4;79.00;58.00;1825.;18.6;77;Europe
Plymouth Arrow GS;25.5;4;122.0;96.00;2300.;15.5;77;US
Datsun F-10 Hatchback;33.5;4;85.00;70.00;1945.;16.8;77;Japan
Chevrolet Caprice Classic;17.5;8;305.0;145.0;3880.;12.5;77;US
Oldsmobile Cutlass Supreme;17.0;8;260.0;110.0;4060.;19.0;77;US
Dodge Monaco Brougham;15.5;8;318.0;145.0;4140.;13.7;77;US
Mercury Cougar Brougham;15.0;8;302.0;130.0;4295.;14.9;77;US
Chevrolet Concours;17.5;6;250.0;110.0;3520.;16.4;77;US
Buick Skylark;20.5;6;231.0;105.0;3425.;16.9;77;US
Plymouth Volare Custom;19.0;6;225.0;100.0;3630.;17.7;77;US
Ford Grenada;18.5;6;250.0;98.00;3525.;19.0;77;US
Pontiac Grand Prix LJ;16.0;8;400.0;180.0;4220.;11.1;77;US
Chevrolet Monte Carlo Landau;15.5;8;350.0;170.0;4165.;11.4;77;US
Chrysler Cordoba;15.5;8;400.0;190.0;4325.;12.2;77;US
Ford Thunderbird;16.0;8;351.0;149.0;4335.;14.5;77;US
Volkswagen Rabbit Custom;29.0;4;97.00;78.00;1940.;14.5;77;Europe
Pontiac Sunbird Coupe;24.5;4;151.0;88.00;2740.;16.0;77;US
Toyota Corolla Liftback;26.0;4;97.00;75.00;2265.;18.2;77;Japan
Ford Mustang II 2+2;25.5;4;140.0;89.00;2755.;15.8;77;US
Chevrolet Chevette;30.5;4;98.00;63.00;2051.;17.0;77;US
Dodge Colt m/m;33.5;4;98.00;83.00;2075.;15.9;77;US
Subaru DL;30.0;4;97.00;67.00;1985.;16.4;77;Japan
Volkswagen Dasher;30.5;4;97.00;78.00;2190.;14.1;77;Europe
Datsun 810;22.0;6;146.0;97.00;2815.;14.5;77;Japan
BMW 320i;21.5;4;121.0;110.0;2600.;12.8;77;Europe
Mazda RX-4;21.5;3;80.00;110.0;2720.;13.5;77;Japan
Volkswagen Rabbit Custom Diesel;43.1;4;90.00;48.00;1985.;21.5;78;Europe
Ford Fiesta;36.1;4;98.00;66.00;1800.;14.4;78;US
Mazda GLC Deluxe;32.8;4;78.00;52.00;1985.;19.4;78;Japan
Datsun B210 GX;39.4;4;85.00;70.00;2070.;18.6;78;Japan
Honda Civic CVCC;36.1;4;91.00;60.00;1800.;16.4;78;Japan
Oldsmobile Cutlass Salon Brougham;19.9;8;260.0;110.0;3365.;15.5;78;US
Dodge Diplomat;19.4;8;318.0;140.0;3735.;13.2;78;US
Mercury Monarch ghia;20.2;8;302.0;139.0;3570.;12.8;78;US
Pontiac Phoenix LJ;19.2;6;231.0;105.0;3535.;19.2;78;US
Chevrolet Malibu;20.5;6;200.0;95.00;3155.;18.2;78;US
Ford Fairmont (auto);20.2;6;200.0;85.00;2965.;15.8;78;US
Ford Fairmont (man);25.1;4;140.0;88.00;2720.;15.4;78;US
Plymouth Volare;20.5;6;225.0;100.0;3430.;17.2;78;US
AMC Concord;19.4;6;232.0;90.00;3210.;17.2;78;US
Buick Century Special;20.6;6;231.0;105.0;3380.;15.8;78;US
Mercury Zephyr;20.8;6;200.0;85.00;3070.;16.7;78;US
Dodge Aspen;18.6;6;225.0;110.0;3620.;18.7;78;US
AMC Concord d/l;18.1;6;258.0;120.0;3410.;15.1;78;US
Chevrolet Monte Carlo Landau;19.2;8;305.0;145.0;3425.;13.2;78;US
Buick Regal Sport Coupe (turbo);17.7;6;231.0;165.0;3445.;13.4;78;US
Ford Futura;18.1;8;302.0;139.0;3205.;11.2;78;US
Dodge Magnum XE;17.5;8;318.0;140.0;4080.;13.7;78;US
Chevrolet Chevette;30.0;4;98.00;68.00;2155.;16.5;78;US
Toyota Corolla;27.5;4;134.0;95.00;2560.;14.2;78;Japan
Datsun 510;27.2;4;119.0;97.00;2300.;14.7;78;Japan
Dodge Omni;30.9;4;105.0;75.00;2230.;14.5;78;US
Toyota Celica GT Liftback;21.1;4;134.0;95.00;2515.;14.8;78;Japan
Plymouth Sapporo;23.2;4;156.0;105.0;2745.;16.7;78;US
Oldsmobile Starfire SX;23.8;4;151.0;85.00;2855.;17.6;78;US
Datsun 200-SX;23.9;4;119.0;97.00;2405.;14.9;78;Japan
Audi 5000;20.3;5;131.0;103.0;2830.;15.9;78;Europe
Volvo 264gl;17.0;6;163.0;125.0;3140.;13.6;78;Europe
Saab 99gle;21.6;4;121.0;115.0;2795.;15.7;78;Europe
Peugeot 604sl;16.2;6;163.0;133.0;3410.;15.8;78;Europe
Volkswagen Scirocco;31.5;4;89.00;71.00;1990.;14.9;78;Europe
Honda Accord LX;29.5;4;98.00;68.00;2135.;16.6;78;Japan
Pontiac Lemans V6;21.5;6;231.0;115.0;3245.;15.4;79;US
Mercury Zephyr 6;19.8;6;200.0;85.00;2990.;18.2;79;US
Ford Fairmont 4;22.3;4;140.0;88.00;2890.;17.3;79;US
AMC Concord DL 6;20.2;6;232.0;90.00;3265.;18.2;79;US
Dodge Aspen 6;20.6;6;225.0;110.0;3360.;16.6;79;US
Chevrolet Caprice Classic;17.0;8;305.0;130.0;3840.;15.4;79;US
Ford LTD Landau;17.6;8;302.0;129.0;3725.;13.4;79;US
Mercury Grand Marquis;16.5;8;351.0;138.0;3955.;13.2;79;US
Dodge St. Regis;18.2;8;318.0;135.0;3830.;15.2;79;US
Buick Estate Wagon (sw);16.9;8;350.0;155.0;4360.;14.9;79;US
Ford Country Squire (sw);15.5;8;351.0;142.0;4054.;14.3;79;US
Chevrolet Malibu Classic (sw);19.2;8;267.0;125.0;3605.;15.0;79;US
Chrysler Lebaron Town @ Country (sw);18.5;8;360.0;150.0;3940.;13.0;79;US
Volkswagen Rabbit Custom;31.9;4;89.00;71.00;1925.;14.0;79;Europe
Mazda GLC Deluxe;34.1;4;86.00;65.00;1975.;15.2;79;Japan
Dodge Colt Hatchback Custom;35.7;4;98.00;80.00;1915.;14.4;79;US
AMC Spirit DL;27.4;4;121.0;80.00;2670.;15.0;79;US
Mercedes Benz 300d;25.4;5;183.0;77.00;3530.;20.1;79;Europe
Cadillac Eldorado;23.0;8;350.0;125.0;3900.;17.4;79;US
Peugeot 504;27.2;4;141.0;71.00;3190.;24.8;79;Europe
Oldsmobile Cutlass Salon Brougham;23.9;8;260.0;90.00;3420.;22.2;79;US
Plymouth Horizon;34.2;4;105.0;70.00;2200.;13.2;79;US
Plymouth Horizon TC3;34.5;4;105.0;70.00;2150.;14.9;79;US
Datsun 210;31.8;4;85.00;65.00;2020.;19.2;79;Japan
Fiat Strada Custom;37.3;4;91.00;69.00;2130.;14.7;79;Europe
Buick Skylark Limited;28.4;4;151.0;90.00;2670.;16.0;79;US
Chevrolet Citation;28.8;6;173.0;115.0;2595.;11.3;79;US
Oldsmobile Omega Brougham;26.8;6;173.0;115.0;2700.;12.9;79;US
Pontiac Phoenix;33.5;4;151.0;90.00;2556.;13.2;79;US
Volkswagen Rabbit;41.5;4;98.00;76.00;2144.;14.7;80;Europe
Toyota Corolla Tercel;38.1;4;89.00;60.00;1968.;18.8;80;Japan
Chevrolet Chevette;32.1;4;98.00;70.00;2120.;15.5;80;US
Datsun 310;37.2;4;86.00;65.00;2019.;16.4;80;Japan
Chevrolet Citation;28.0;4;151.0;90.00;2678.;16.5;80;US
Ford Fairmont;26.4;4;140.0;88.00;2870.;18.1;80;US
AMC Concord;24.3;4;151.0;90.00;3003.;20.1;80;US
Dodge Aspen;19.1;6;225.0;90.00;3381.;18.7;80;US
Audi 4000;34.3;4;97.00;78.00;2188.;15.8;80;Europe
Toyota Corolla Liftback;29.8;4;134.0;90.00;2711.;15.5;80;Japan
Mazda 626;31.3;4;120.0;75.00;2542.;17.5;80;Japan
Datsun 510 Hatchback;37.0;4;119.0;92.00;2434.;15.0;80;Japan
Toyota Corolla;32.2;4;108.0;75.00;2265.;15.2;80;Japan
Mazda GLC;46.6;4;86.00;65.00;2110.;17.9;80;Japan
Dodge Colt;27.9;4;156.0;105.0;2800.;14.4;80;US
Datsun 210;40.8;4;85.00;65.00;2110.;19.2;80;Japan
Volkswagen Rabbit C (Diesel);44.3;4;90.00;48.00;2085.;21.7;80;Europe
Volkswagen Dasher (diesel);43.4;4;90.00;48.00;2335.;23.7;80;Europe
Audi 5000s (diesel);36.4;5;121.0;67.00;2950.;19.9;80;Europe
Mercedes-Benz 240d;30.0;4;146.0;67.00;3250.;21.8;80;Europe
Honda Civic 1500 gl;44.6;4;91.00;67.00;1850.;13.8;80;Japan
Renault Lecar Deluxe;40.9;4;85.00;0;1835.;17.3;80;Europe
Subaru DL;33.8;4;97.00;67.00;2145.;18.0;80;Japan
Volkswagen Rabbit;29.8;4;89.00;62.00;1845.;15.3;80;Europe
Datsun 280-ZX;32.7;6;168.0;132.0;2910.;11.4;80;Japan
Mazda RX-7 GS;23.7;3;70.00;100.0;2420.;12.5;80;Japan
Triumph TR7 Coupe;35.0;4;122.0;88.00;2500.;15.1;80;Europe
Ford Mustang Cobra;23.6;4;140.0;0;2905.;14.3;80;US
Honda Accord;32.4;4;107.0;72.00;2290.;17.0;80;Japan
Plymouth Reliant;27.2;4;135.0;84.00;2490.;15.7;81;US
Buick Skylark;26.6;4;151.0;84.00;2635.;16.4;81;US
Dodge Aries Wagon (sw);25.8;4;156.0;92.00;2620.;14.4;81;US
Chevrolet Citation;23.5;6;173.0;110.0;2725.;12.6;81;US
Plymouth Reliant;30.0;4;135.0;84.00;2385.;12.9;81;US
Toyota Starlet;39.1;4;79.00;58.00;1755.;16.9;81;Japan
Plymouth Champ;39.0;4;86.00;64.00;1875.;16.4;81;US
Honda Civic 1300;35.1;4;81.00;60.00;1760.;16.1;81;Japan
Subaru;32.3;4;97.00;67.00;2065.;17.8;81;Japan
Datsun 210 MPG;37.0;4;85.00;65.00;1975.;19.4;81;Japan
Toyota Tercel;37.7;4;89.00;62.00;2050.;17.3;81;Japan
Mazda GLC 4;34.1;4;91.00;68.00;1985.;16.0;81;Japan
Plymouth Horizon 4;34.7;4;105.0;63.00;2215.;14.9;81;US
Ford Escort 4W;34.4;4;98.00;65.00;2045.;16.2;81;US
Ford Escort 2H;29.9;4;98.00;65.00;2380.;20.7;81;US
Volkswagen Jetta;33.0;4;105.0;74.00;2190.;14.2;81;Europe
Renault 18i;34.5;4;100.0;0;2320.;15.8;81;Europe
Honda Prelude;33.7;4;107.0;75.00;2210.;14.4;81;Japan
Toyota Corolla;32.4;4;108.0;75.00;2350.;16.8;81;Japan
Datsun 200SX;32.9;4;119.0;100.0;2615.;14.8;81;Japan
Mazda 626;31.6;4;120.0;74.00;2635.;18.3;81;Japan
Peugeot 505s Turbo Diesel;28.1;4;141.0;80.00;3230.;20.4;81;Europe
Saab 900s;0;4;121.0;110.0;2800.;15.4;81;Europe
Volvo Diesel;30.7;6;145.0;76.00;3160.;19.6;81;Europe
Toyota Cressida;25.4;6;168.0;116.0;2900.;12.6;81;Japan
Datsun 810 Maxima;24.2;6;146.0;120.0;2930.;13.8;81;Japan
Buick Century;22.4;6;231.0;110.0;3415.;15.8;81;US
Oldsmobile Cutlass LS;26.6;8;350.0;105.0;3725.;19.0;81;US
Ford Grenada gl;20.2;6;200.0;88.00;3060.;17.1;81;US
Chrysler Lebaron Salon;17.6;6;225.0;85.00;3465.;16.6;81;US
Chevrolet Cavalier;28.0;4;112.0;88.00;2605.;19.6;82;US
Chevrolet Cavalier Wagon;27.0;4;112.0;88.00;2640.;18.6;82;US
Chevrolet Cavalier 2-door;34.0;4;112.0;88.00;2395.;18.0;82;US
Pontiac J2000 SE Hatchback;31.0;4;112.0;85.00;2575.;16.2;82;US
Dodge Aries SE;29.0;4;135.0;84.00;2525.;16.0;82;US
Pontiac Phoenix;27.0;4;151.0;90.00;2735.;18.0;82;US
Ford Fairmont Futura;24.0;4;140.0;92.00;2865.;16.4;82;US
AMC Concord DL;23.0;4;151.0;0;3035.;20.5;82;US
Volkswagen Rabbit l;36.0;4;105.0;74.00;1980.;15.3;82;Europe
Mazda GLC Custom l;37.0;4;91.00;68.00;2025.;18.2;82;Japan
Mazda GLC Custom;31.0;4;91.00;68.00;1970.;17.6;82;Japan
Plymouth Horizon Miser;38.0;4;105.0;63.00;2125.;14.7;82;US
Mercury Lynx l;36.0;4;98.00;70.00;2125.;17.3;82;US
Nissan Stanza XE;36.0;4;120.0;88.00;2160.;14.5;82;Japan
Honda Accord;36.0;4;107.0;75.00;2205.;14.5;82;Japan
Toyota Corolla;34.0;4;108.0;70.00;2245;16.9;82;Japan
Honda Civic;38.0;4;91.00;67.00;1965.;15.0;82;Japan
Honda Civic (auto);32.0;4;91.00;67.00;1965.;15.7;82;Japan
Datsun 310 GX;38.0;4;91.00;67.00;1995.;16.2;82;Japan
Buick Century Limited;25.0;6;181.0;110.0;2945.;16.4;82;US
Oldsmobile Cutlass Ciera (diesel);38.0;6;262.0;85.00;3015.;17.0;82;US
Chrysler Lebaron Medallion;26.0;4;156.0;92.00;2585.;14.5;82;US
Ford Grenada l;22.0;6;232.0;112.0;2835;14.7;82;US
Toyota Celica GT;32.0;4;144.0;96.00;2665.;13.9;82;Japan
Dodge Charger 2.2;36.0;4;135.0;84.00;2370.;13.0;82;US
Chevrolet Camaro;27.0;4;151.0;90.00;2950.;17.3;82;US
Ford Mustang GL;27.0;4;140.0;86.00;2790.;15.6;82;US
Volkswagen Pickup;44.0;4;97.00;52.00;2130.;24.6;82;Europe
Dodge Rampage;32.0;4;135.0;84.00;2295.;11.6;82;US
Ford Ranger;28.0;4;120.0;79.00;2625.;18.6;82;US
Chevy S-10;31.0;4;119.0;82.00;2720.;19.4;82;US
The TextIOWrapper class also provides a method readlines() that will read the entire file and return a list containing all the rows:
'''
with open('cars.csv') as f:
    l = f.readlines()
l
'''
['Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin\n',
 'STRING;DOUBLE;INT;DOUBLE;DOUBLE;DOUBLE;DOUBLE;INT;CAT\n',
 'Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US\n',
 'Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US\n',
 'Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US\n',
 'AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US\n',
 'Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US\n',
 'Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US\n',
 'Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US\n',
 'Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US\n',
 'Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US\n',
 'AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US\n',
 'Citroen DS-21 Pallas;0;4;133.0;115.0;3090.;17.5;70;Europe\n',
 'Chevrolet Chevelle Concours (sw);0;8;350.0;165.0;4142.;11.5;70;US\n',
 'Ford Torino (sw);0;8;351.0;153.0;4034.;11.0;70;US\n',
 'Plymouth Satellite (sw);0;8;383.0;175.0;4166.;10.5;70;US\n',
 'AMC Rebel SST (sw);0;8;360.0;175.0;3850.;11.0;70;US\n',
 'Dodge Challenger SE;15.0;8;383.0;170.0;3563.;10.0;70;US\n',
 "Plymouth 'Cuda 340;14.0;8;340.0;160.0;3609.;8.0;70;US\n",
 'Ford Mustang Boss 302;0;8;302.0;140.0;3353.;8.0;70;US\n',
 'Chevrolet Monte Carlo;15.0;8;400.0;150.0;3761.;9.5;70;US\n',
 'Buick Estate Wagon (sw);14.0;8;455.0;225.0;3086.;10.0;70;US\n',
 'Toyota Corolla Mark ii;24.0;4;113.0;95.00;2372.;15.0;70;Japan\n',
 'Plymouth Duster;22.0;6;198.0;95.00;2833.;15.5;70;US\n',
 'AMC Hornet;18.0;6;199.0;97.00;2774.;15.5;70;US\n',
 'Ford Maverick;21.0;6;200.0;85.00;2587.;16.0;70;US\n',
 'Datsun PL510;27.0;4;97.00;88.00;2130.;14.5;70;Japan\n',
 'Volkswagen 1131 Deluxe Sedan;26.0;4;97.00;46.00;1835.;20.5;70;Europe\n',
 'Peugeot 504;25.0;4;110.0;87.00;2672.;17.5;70;Europe\n',
 'Audi 100 LS;24.0;4;107.0;90.00;2430.;14.5;70;Europe\n',
 'Saab 99e;25.0;4;104.0;95.00;2375.;17.5;70;Europe\n',
 'BMW 2002;26.0;4;121.0;113.0;2234.;12.5;70;Europe\n',
 'AMC Gremlin;21.0;6;199.0;90.00;2648.;15.0;70;US\n',
 'Ford F250;10.0;8;360.0;215.0;4615.;14.0;70;US\n',
 'Chevy C20;10.0;8;307.0;200.0;4376.;15.0;70;US\n',
 'Dodge D200;11.0;8;318.0;210.0;4382.;13.5;70;US\n',
 'Hi 1200D;9.0;8;304.0;193.0;4732.;18.5;70;US\n',
 'Datsun PL510;27.0;4;97.00;88.00;2130.;14.5;71;Japan\n',
 'Chevrolet Vega 2300;28.0;4;140.0;90.00;2264.;15.5;71;US\n',
 'Toyota Corolla;25.0;4;113.0;95.00;2228.;14.0;71;Japan\n',
 'Ford Pinto;25.0;4;98.00;0;2046.;19.0;71;US\n',
 'Volkswagen Super Beetle 117;0;4;97.00;48.00;1978.;20.0;71;Europe\n',
 'AMC Gremlin;19.0;6;232.0;100.0;2634.;13.0;71;US\n',
 'Plymouth Satellite Custom;16.0;6;225.0;105.0;3439.;15.5;71;US\n',
 'Chevrolet Chevelle Malibu;17.0;6;250.0;100.0;3329.;15.5;71;US\n',
 'Ford Torino 500;19.0;6;250.0;88.00;3302.;15.5;71;US\n',
 'AMC Matador;18.0;6;232.0;100.0;3288.;15.5;71;US\n',
 'Chevrolet Impala;14.0;8;350.0;165.0;4209.;12.0;71;US\n',
 'Pontiac Catalina Brougham;14.0;8;400.0;175.0;4464.;11.5;71;US\n',
 'Ford Galaxie 500;14.0;8;351.0;153.0;4154.;13.5;71;US\n',
 'Plymouth Fury iii;14.0;8;318.0;150.0;4096.;13.0;71;US\n',
 'Dodge Monaco (sw);12.0;8;383.0;180.0;4955.;11.5;71;US\n',
 'Ford Country Squire (sw);13.0;8;400.0;170.0;4746.;12.0;71;US\n',
 'Pontiac Safari (sw);13.0;8;400.0;175.0;5140.;12.0;71;US\n',
 'AMC Hornet Sportabout (sw);18.0;6;258.0;110.0;2962.;13.5;71;US\n',
 'Chevrolet Vega (sw);22.0;4;140.0;72.00;2408.;19.0;71;US\n',
 'Pontiac Firebird;19.0;6;250.0;100.0;3282.;15.0;71;US\n',
 'Ford Mustang;18.0;6;250.0;88.00;3139.;14.5;71;US\n',
 'Mercury Capri 2000;23.0;4;122.0;86.00;2220.;14.0;71;US\n',
 'Opel 1900;28.0;4;116.0;90.00;2123.;14.0;71;Europe\n',
 'Peugeot 304;30.0;4;79.00;70.00;2074.;19.5;71;Europe\n',
 'Fiat 124B;30.0;4;88.00;76.00;2065.;14.5;71;Europe\n',
 'Toyota Corolla 1200;31.0;4;71.00;65.00;1773.;19.0;71;Japan\n',
 'Datsun 1200;35.0;4;72.00;69.00;1613.;18.0;71;Japan\n',
 'Volkswagen Model 111;27.0;4;97.00;60.00;1834.;19.0;71;Europe\n',
 'Plymouth Cricket;26.0;4;91.00;70.00;1955.;20.5;71;US\n',
 'Toyota Corolla Hardtop;24.0;4;113.0;95.00;2278.;15.5;72;Japan\n',
 'Dodge Colt Hardtop;25.0;4;97.50;80.00;2126.;17.0;72;US\n',
 'Volkswagen Type 3;23.0;4;97.00;54.00;2254.;23.5;72;Europe\n',
 'Chevrolet Vega;20.0;4;140.0;90.00;2408.;19.5;72;US\n',
 'Ford Pinto Runabout;21.0;4;122.0;86.00;2226.;16.5;72;US\n',
 'Chevrolet Impala;13.0;8;350.0;165.0;4274.;12.0;72;US\n',
 'Pontiac Catalina;14.0;8;400.0;175.0;4385.;12.0;72;US\n',
 'Plymouth Fury III;15.0;8;318.0;150.0;4135.;13.5;72;US\n',
 'Ford Galaxie 500;14.0;8;351.0;153.0;4129.;13.0;72;US\n',
 'AMC Ambassador SST;17.0;8;304.0;150.0;3672.;11.5;72;US\n',
 'Mercury Marquis;11.0;8;429.0;208.0;4633.;11.0;72;US\n',
 'Buick LeSabre Custom;13.0;8;350.0;155.0;4502.;13.5;72;US\n',
 'Oldsmobile Delta 88 Royale;12.0;8;350.0;160.0;4456.;13.5;72;US\n',
 'Chrysler Newport Royal;13.0;8;400.0;190.0;4422.;12.5;72;US\n',
 'Mazda RX2 Coupe;19.0;3;70.00;97.00;2330.;13.5;72;Japan\n',
 'AMC Matador (sw);15.0;8;304.0;150.0;3892.;12.5;72;US\n',
 'Chevrolet Chevelle Concours (sw);13.0;8;307.0;130.0;4098.;14.0;72;US\n',
 'Ford Gran Torino (sw);13.0;8;302.0;140.0;4294.;16.0;72;US\n',
 'Plymouth Satellite Custom (sw);14.0;8;318.0;150.0;4077.;14.0;72;US\n',
 'Volvo 145e (sw);18.0;4;121.0;112.0;2933.;14.5;72;Europe\n',
 'Volkswagen 411 (sw);22.0;4;121.0;76.00;2511.;18.0;72;Europe\n',
 'Peugeot 504 (sw);21.0;4;120.0;87.00;2979.;19.5;72;Europe\n',
 'Renault 12 (sw);26.0;4;96.00;69.00;2189.;18.0;72;Europe\n',
 'Ford Pinto (sw);22.0;4;122.0;86.00;2395.;16.0;72;US\n',
 'Datsun 510 (sw);28.0;4;97.00;92.00;2288.;17.0;72;Japan\n',
 'Toyota Corolla Mark II (sw);23.0;4;120.0;97.00;2506.;14.5;72;Japan\n',
 'Dodge Colt (sw);28.0;4;98.00;80.00;2164.;15.0;72;US\n',
 'Toyota Corolla 1600 (sw);27.0;4;97.00;88.00;2100.;16.5;72;Japan\n',
 'Buick Century 350;13.0;8;350.0;175.0;4100.;13.0;73;US\n',
 'AMC Matador;14.0;8;304.0;150.0;3672.;11.5;73;US\n',
 'Chevrolet Malibu;13.0;8;350.0;145.0;3988.;13.0;73;US\n',
 'Ford Gran Torino;14.0;8;302.0;137.0;4042.;14.5;73;US\n',
 'Dodge Coronet Custom;15.0;8;318.0;150.0;3777.;12.5;73;US\n',
 'Mercury Marquis Brougham;12.0;8;429.0;198.0;4952.;11.5;73;US\n',
 'Chevrolet Caprice Classic;13.0;8;400.0;150.0;4464.;12.0;73;US\n',
 'Ford LTD;13.0;8;351.0;158.0;4363.;13.0;73;US\n',
 'Plymouth Fury Gran Sedan;14.0;8;318.0;150.0;4237.;14.5;73;US\n',
 'Chrysler New Yorker Brougham;13.0;8;440.0;215.0;4735.;11.0;73;US\n',
 'Buick Electra 225 Custom;12.0;8;455.0;225.0;4951.;11.0;73;US\n',
 'AMC Ambassador Brougham;13.0;8;360.0;175.0;3821.;11.0;73;US\n',
 'Plymouth Valiant;18.0;6;225.0;105.0;3121.;16.5;73;US\n',
 'Chevrolet Nova Custom;16.0;6;250.0;100.0;3278.;18.0;73;US\n',
 'AMC Hornet;18.0;6;232.0;100.0;2945.;16.0;73;US\n',
 'Ford Maverick;18.0;6;250.0;88.00;3021.;16.5;73;US\n',
 'Plymouth Duster;23.0;6;198.0;95.00;2904.;16.0;73;US\n',
 'Volkswagen Super Beetle;26.0;4;97.00;46.00;1950.;21.0;73;Europe\n',
 'Chevrolet Impala;11.0;8;400.0;150.0;4997.;14.0;73;US\n',
 'Ford Country;12.0;8;400.0;167.0;4906.;12.5;73;US\n',
 'Plymouth Custom Suburb;13.0;8;360.0;170.0;4654.;13.0;73;US\n',
 'Oldsmobile Vista Cruiser;12.0;8;350.0;180.0;4499.;12.5;73;US\n',
 'AMC Gremlin;18.0;6;232.0;100.0;2789.;15.0;73;US\n',
 'Toyota Camry;20.0;4;97.00;88.00;2279.;19.0;73;Japan\n',
 'Chevrolet Vega;21.0;4;140.0;72.00;2401.;19.5;73;US\n',
 'Datsun 610;22.0;4;108.0;94.00;2379.;16.5;73;Japan\n',
 'Mazda RX3;18.0;3;70.00;90.00;2124.;13.5;73;Japan\n',
 'Ford Pinto;19.0;4;122.0;85.00;2310.;18.5;73;US\n',
 'Mercury Capri v6;21.0;6;155.0;107.0;2472.;14.0;73;US\n',
 'Fiat 124 Sport Coupe;26.0;4;98.00;90.00;2265.;15.5;73;Europe\n',
 'Chevrolet Monte Carlo S;15.0;8;350.0;145.0;4082.;13.0;73;US\n',
 'Pontiac Grand Prix;16.0;8;400.0;230.0;4278.;9.50;73;US\n',
 'Fiat 128;29.0;4;68.00;49.00;1867.;19.5;73;Europe\n',
 'Opel Manta;24.0;4;116.0;75.00;2158.;15.5;73;Europe\n',
 'Audi 100LS;20.0;4;114.0;91.00;2582.;14.0;73;Europe\n',
 'Volvo 144ea;19.0;4;121.0;112.0;2868.;15.5;73;Europe\n',
 'Dodge Dart Custom;15.0;8;318.0;150.0;3399.;11.0;73;US\n',
 'Saab 99le;24.0;4;121.0;110.0;2660.;14.0;73;Europe\n',
 'Toyota Mark II;20.0;6;156.0;122.0;2807.;13.5;73;Japan\n',
 'Oldsmobile Omega;11.0;8;350.0;180.0;3664.;11.0;73;US\n',
 'Plymouth Duster;20.0;6;198.0;95.00;3102.;16.5;74;US\n',
 'Ford Maverick;21.0;6;200.0;0;2875.;17.0;74;US\n',
 'AMC Hornet;19.0;6;232.0;100.0;2901.;16.0;74;US\n',
 'Chevrolet Nova;15.0;6;250.0;100.0;3336.;17.0;74;US\n',
 'Datsun B210;31.0;4;79.00;67.00;1950.;19.0;74;Japan\n',
 'Ford Pinto;26.0;4;122.0;80.00;2451.;16.5;74;US\n',
 'Toyota Corolla 1200;32.0;4;71.00;65.00;1836.;21.0;74;Japan\n',
 'Chevrolet Vega;25.0;4;140.0;75.00;2542.;17.0;74;US\n',
 'Chevrolet Chevelle Malibu Classic;16.0;6;250.0;100.0;3781.;17.0;74;US\n',
 'AMC Matador;16.0;6;258.0;110.0;3632.;18.0;74;US\n',
 'Plymouth Satellite Sebring;18.0;6;225.0;105.0;3613.;16.5;74;US\n',
 'Ford Gran Torino;16.0;8;302.0;140.0;4141.;14.0;74;US\n',
 'Buick Century Luxus (sw);13.0;8;350.0;150.0;4699.;14.5;74;US\n',
 'Dodge Coronet Custom (sw);14.0;8;318.0;150.0;4457.;13.5;74;US\n',
 'Ford Gran Torino (sw);14.0;8;302.0;140.0;4638.;16.0;74;US\n',
 'AMC Matador (sw);14.0;8;304.0;150.0;4257.;15.5;74;US\n',
 'Audi Fox;29.0;4;98.00;83.00;2219.;16.5;74;Europe\n',
 'Volkswagen Dasher;26.0;4;79.00;67.00;1963.;15.5;74;Europe\n',
 'Opel Manta;26.0;4;97.00;78.00;2300.;14.5;74;Europe\n',
 'Toyota Corolla;31.0;4;76.00;52.00;1649.;16.5;74;Japan\n',
 'Datsun 710;32.0;4;83.00;61.00;2003.;19.0;74;Japan\n',
 'Dodge Colt;28.0;4;90.00;75.00;2125.;14.5;74;US\n',
 'Fiat 128;24.0;4;90.00;75.00;2108.;15.5;74;Europe\n',
 'Fiat 124 TC;26.0;4;116.0;75.00;2246.;14.0;74;Europe\n',
 'Honda Civic;24.0;4;120.0;97.00;2489.;15.0;74;Japan\n',
 'Subaru;26.0;4;108.0;93.00;2391.;15.5;74;Japan\n',
 'Fiat x1.9;31.0;4;79.00;67.00;2000.;16.0;74;Europe\n',
 'Plymouth Valiant Custom;19.0;6;225.0;95.00;3264.;16.0;75;US\n',
 'Chevrolet Nova;18.0;6;250.0;105.0;3459.;16.0;75;US\n',
 'Mercury Monarch;15.0;6;250.0;72.00;3432.;21.0;75;US\n',
 'Ford Maverick;15.0;6;250.0;72.00;3158.;19.5;75;US\n',
 'Pontiac Catalina;16.0;8;400.0;170.0;4668.;11.5;75;US\n',
 'Chevrolet Bel Air;15.0;8;350.0;145.0;4440.;14.0;75;US\n',
 'Plymouth Grand Fury;16.0;8;318.0;150.0;4498.;14.5;75;US\n',
 'Ford LTD;14.0;8;351.0;148.0;4657.;13.5;75;US\n',
 'Buick Century;17.0;6;231.0;110.0;3907.;21.0;75;US\n',
 'Chevrolete Chevelle Malibu;16.0;6;250.0;105.0;3897.;18.5;75;US\n',
 'AMC Matador;15.0;6;258.0;110.0;3730.;19.0;75;US\n',
 'Plymouth Fury;18.0;6;225.0;95.00;3785.;19.0;75;US\n',
 'Buick Skyhawk;21.0;6;231.0;110.0;3039.;15.0;75;US\n',
 'Chevrolet Monza 2+2;20.0;8;262.0;110.0;3221.;13.5;75;US\n',
 'Ford Mustang II;13.0;8;302.0;129.0;3169.;12.0;75;US\n',
 'Toyota Corolla;29.0;4;97.00;75.00;2171.;16.0;75;Japan\n',
 'Ford Pinto;23.0;4;140.0;83.00;2639.;17.0;75;US\n',
 'AMC Gremlin;20.0;6;232.0;100.0;2914.;16.0;75;US\n',
 'Pontiac Astro;23.0;4;140.0;78.00;2592.;18.5;75;US\n',
 'Toyota Corolla;24.0;4;134.0;96.00;2702.;13.5;75;Japan\n',
 'Volkswagen Dasher;25.0;4;90.00;71.00;2223.;16.5;75;Europe\n',
 'Datsun 710;24.0;4;119.0;97.00;2545.;17.0;75;Japan\n',
 'Ford Pinto;18.0;6;171.0;97.00;2984.;14.5;75;US\n',
 'Volkswagen Rabbit;29.0;4;90.00;70.00;1937.;14.0;75;Europe\n',
 'AMC Pacer;19.0;6;232.0;90.00;3211.;17.0;75;US\n',
 'Audi 100LS;23.0;4;115.0;95.00;2694.;15.0;75;Europe\n',
 'Peugeot 504;23.0;4;120.0;88.00;2957.;17.0;75;Europe\n',
 'Volvo 244DL;22.0;4;121.0;98.00;2945.;14.5;75;Europe\n',
 'Saab 99LE;25.0;4;121.0;115.0;2671.;13.5;75;Europe\n',
 'Honda Civic CVCC;33.0;4;91.00;53.00;1795.;17.5;75;Japan\n',
 'Fiat 131;28.0;4;107.0;86.00;2464.;15.5;76;Europe\n',
 'Opel 1900;25.0;4;116.0;81.00;2220.;16.9;76;Europe\n',
 'Capri ii;25.0;4;140.0;92.00;2572.;14.9;76;US\n',
 'Dodge Colt;26.0;4;98.00;79.00;2255.;17.7;76;US\n',
 'Renault 12tl;27.0;4;101.0;83.00;2202.;15.3;76;Europe\n',
 'Chevrolet Chevelle Malibu Classic;17.5;8;305.0;140.0;4215.;13.0;76;US\n',
 'Dodge Coronet Brougham;16.0;8;318.0;150.0;4190.;13.0;76;US\n',
 'AMC Matador;15.5;8;304.0;120.0;3962.;13.9;76;US\n',
 'Ford Gran Torino;14.5;8;351.0;152.0;4215.;12.8;76;US\n',
 'Plymouth Valiant;22.0;6;225.0;100.0;3233.;15.4;76;US\n',
 'Chevrolet Nova;22.0;6;250.0;105.0;3353.;14.5;76;US\n',
 'Ford Maverick;24.0;6;200.0;81.00;3012.;17.6;76;US\n',
 'AMC Hornet;22.5;6;232.0;90.00;3085.;17.6;76;US\n',
 'Chevrolet Chevette;29.0;4;85.00;52.00;2035.;22.2;76;US\n',
 'Chevrolet Woody;24.5;4;98.00;60.00;2164.;22.1;76;US\n',
 'Volkswagen Rabbit;29.0;4;90.00;70.00;1937.;14.2;76;Europe\n',
 'Honda Civic;33.0;4;91.00;53.00;1795.;17.4;76;Japan\n',
 'Dodge Aspen SE;20.0;6;225.0;100.0;3651.;17.7;76;US\n',
 'Ford Grenada ghia;18.0;6;250.0;78.00;3574.;21.0;76;US\n',
 'Pontiac Ventura SJ;18.5;6;250.0;110.0;3645.;16.2;76;US\n',
 'AMC Pacer d/l;17.5;6;258.0;95.00;3193.;17.8;76;US\n',
 'Volkswagen Rabbit;29.5;4;97.00;71.00;1825.;12.2;76;Europe\n',
 'Datsun B-210;32.0;4;85.00;70.00;1990.;17.0;76;Japan\n',
 'Toyota Corolla;28.0;4;97.00;75.00;2155.;16.4;76;Japan\n',
 'Ford Pinto;26.5;4;140.0;72.00;2565.;13.6;76;US\n',
 'Volvo 245;20.0;4;130.0;102.0;3150.;15.7;76;Europe\n',
 'Plymouth Volare Premier v8;13.0;8;318.0;150.0;3940.;13.2;76;US\n',
 'Peugeot 504;19.0;4;120.0;88.00;3270.;21.9;76;Europe\n',
 'Toyota Mark II;19.0;6;156.0;108.0;2930.;15.5;76;Japan\n',
 'Mercedes-Benz 280s;16.5;6;168.0;120.0;3820.;16.7;76;Europe\n',
 'Cadillac Seville;16.5;8;350.0;180.0;4380.;12.1;76;US\n',
 'Chevrolet C10;13.0;8;350.0;145.0;4055.;12.0;76;US\n',
 'Ford F108;13.0;8;302.0;130.0;3870.;15.0;76;US\n',
 'Dodge D100;13.0;8;318.0;150.0;3755.;14.0;76;US\n',
 'Honda Accord CVCC;31.5;4;98.00;68.00;2045.;18.5;77;Japan\n',
 'Buick Opel Isuzu Deluxe;30.0;4;111.0;80.00;2155.;14.8;77;US\n',
 'Renault 5 GTL;36.0;4;79.00;58.00;1825.;18.6;77;Europe\n',
 'Plymouth Arrow GS;25.5;4;122.0;96.00;2300.;15.5;77;US\n',
 'Datsun F-10 Hatchback;33.5;4;85.00;70.00;1945.;16.8;77;Japan\n',
 'Chevrolet Caprice Classic;17.5;8;305.0;145.0;3880.;12.5;77;US\n',
 'Oldsmobile Cutlass Supreme;17.0;8;260.0;110.0;4060.;19.0;77;US\n',
 'Dodge Monaco Brougham;15.5;8;318.0;145.0;4140.;13.7;77;US\n',
 'Mercury Cougar Brougham;15.0;8;302.0;130.0;4295.;14.9;77;US\n',
 'Chevrolet Concours;17.5;6;250.0;110.0;3520.;16.4;77;US\n',
 'Buick Skylark;20.5;6;231.0;105.0;3425.;16.9;77;US\n',
 'Plymouth Volare Custom;19.0;6;225.0;100.0;3630.;17.7;77;US\n',
 'Ford Grenada;18.5;6;250.0;98.00;3525.;19.0;77;US\n',
 'Pontiac Grand Prix LJ;16.0;8;400.0;180.0;4220.;11.1;77;US\n',
 'Chevrolet Monte Carlo Landau;15.5;8;350.0;170.0;4165.;11.4;77;US\n',
 'Chrysler Cordoba;15.5;8;400.0;190.0;4325.;12.2;77;US\n',
 'Ford Thunderbird;16.0;8;351.0;149.0;4335.;14.5;77;US\n',
 'Volkswagen Rabbit Custom;29.0;4;97.00;78.00;1940.;14.5;77;Europe\n',
 'Pontiac Sunbird Coupe;24.5;4;151.0;88.00;2740.;16.0;77;US\n',
 'Toyota Corolla Liftback;26.0;4;97.00;75.00;2265.;18.2;77;Japan\n',
 'Ford Mustang II 2+2;25.5;4;140.0;89.00;2755.;15.8;77;US\n',
 'Chevrolet Chevette;30.5;4;98.00;63.00;2051.;17.0;77;US\n',
 'Dodge Colt m/m;33.5;4;98.00;83.00;2075.;15.9;77;US\n',
 'Subaru DL;30.0;4;97.00;67.00;1985.;16.4;77;Japan\n',
 'Volkswagen Dasher;30.5;4;97.00;78.00;2190.;14.1;77;Europe\n',
 'Datsun 810;22.0;6;146.0;97.00;2815.;14.5;77;Japan\n',
 'BMW 320i;21.5;4;121.0;110.0;2600.;12.8;77;Europe\n',
 'Mazda RX-4;21.5;3;80.00;110.0;2720.;13.5;77;Japan\n',
 'Volkswagen Rabbit Custom Diesel;43.1;4;90.00;48.00;1985.;21.5;78;Europe\n',
 'Ford Fiesta;36.1;4;98.00;66.00;1800.;14.4;78;US\n',
 'Mazda GLC Deluxe;32.8;4;78.00;52.00;1985.;19.4;78;Japan\n',
 'Datsun B210 GX;39.4;4;85.00;70.00;2070.;18.6;78;Japan\n',
 'Honda Civic CVCC;36.1;4;91.00;60.00;1800.;16.4;78;Japan\n',
 'Oldsmobile Cutlass Salon Brougham;19.9;8;260.0;110.0;3365.;15.5;78;US\n',
 'Dodge Diplomat;19.4;8;318.0;140.0;3735.;13.2;78;US\n',
 'Mercury Monarch ghia;20.2;8;302.0;139.0;3570.;12.8;78;US\n',
 'Pontiac Phoenix LJ;19.2;6;231.0;105.0;3535.;19.2;78;US\n',
 'Chevrolet Malibu;20.5;6;200.0;95.00;3155.;18.2;78;US\n',
 'Ford Fairmont (auto);20.2;6;200.0;85.00;2965.;15.8;78;US\n',
 'Ford Fairmont (man);25.1;4;140.0;88.00;2720.;15.4;78;US\n',
 'Plymouth Volare;20.5;6;225.0;100.0;3430.;17.2;78;US\n',
 'AMC Concord;19.4;6;232.0;90.00;3210.;17.2;78;US\n',
 'Buick Century Special;20.6;6;231.0;105.0;3380.;15.8;78;US\n',
 'Mercury Zephyr;20.8;6;200.0;85.00;3070.;16.7;78;US\n',
 'Dodge Aspen;18.6;6;225.0;110.0;3620.;18.7;78;US\n',
 'AMC Concord d/l;18.1;6;258.0;120.0;3410.;15.1;78;US\n',
 'Chevrolet Monte Carlo Landau;19.2;8;305.0;145.0;3425.;13.2;78;US\n',
 'Buick Regal Sport Coupe (turbo);17.7;6;231.0;165.0;3445.;13.4;78;US\n',
 'Ford Futura;18.1;8;302.0;139.0;3205.;11.2;78;US\n',
 'Dodge Magnum XE;17.5;8;318.0;140.0;4080.;13.7;78;US\n',
 'Chevrolet Chevette;30.0;4;98.00;68.00;2155.;16.5;78;US\n',
 'Toyota Corolla;27.5;4;134.0;95.00;2560.;14.2;78;Japan\n',
 'Datsun 510;27.2;4;119.0;97.00;2300.;14.7;78;Japan\n',
 'Dodge Omni;30.9;4;105.0;75.00;2230.;14.5;78;US\n',
 'Toyota Celica GT Liftback;21.1;4;134.0;95.00;2515.;14.8;78;Japan\n',
 'Plymouth Sapporo;23.2;4;156.0;105.0;2745.;16.7;78;US\n',
 'Oldsmobile Starfire SX;23.8;4;151.0;85.00;2855.;17.6;78;US\n',
 'Datsun 200-SX;23.9;4;119.0;97.00;2405.;14.9;78;Japan\n',
 'Audi 5000;20.3;5;131.0;103.0;2830.;15.9;78;Europe\n',
 'Volvo 264gl;17.0;6;163.0;125.0;3140.;13.6;78;Europe\n',
 'Saab 99gle;21.6;4;121.0;115.0;2795.;15.7;78;Europe\n',
 'Peugeot 604sl;16.2;6;163.0;133.0;3410.;15.8;78;Europe\n',
 'Volkswagen Scirocco;31.5;4;89.00;71.00;1990.;14.9;78;Europe\n',
 'Honda Accord LX;29.5;4;98.00;68.00;2135.;16.6;78;Japan\n',
 'Pontiac Lemans V6;21.5;6;231.0;115.0;3245.;15.4;79;US\n',
 'Mercury Zephyr 6;19.8;6;200.0;85.00;2990.;18.2;79;US\n',
 'Ford Fairmont 4;22.3;4;140.0;88.00;2890.;17.3;79;US\n',
 'AMC Concord DL 6;20.2;6;232.0;90.00;3265.;18.2;79;US\n',
 'Dodge Aspen 6;20.6;6;225.0;110.0;3360.;16.6;79;US\n',
 'Chevrolet Caprice Classic;17.0;8;305.0;130.0;3840.;15.4;79;US\n',
 'Ford LTD Landau;17.6;8;302.0;129.0;3725.;13.4;79;US\n',
 'Mercury Grand Marquis;16.5;8;351.0;138.0;3955.;13.2;79;US\n',
 'Dodge St. Regis;18.2;8;318.0;135.0;3830.;15.2;79;US\n',
 'Buick Estate Wagon (sw);16.9;8;350.0;155.0;4360.;14.9;79;US\n',
 'Ford Country Squire (sw);15.5;8;351.0;142.0;4054.;14.3;79;US\n',
 'Chevrolet Malibu Classic (sw);19.2;8;267.0;125.0;3605.;15.0;79;US\n',
 'Chrysler Lebaron Town @ Country (sw);18.5;8;360.0;150.0;3940.;13.0;79;US\n',
 'Volkswagen Rabbit Custom;31.9;4;89.00;71.00;1925.;14.0;79;Europe\n',
 'Mazda GLC Deluxe;34.1;4;86.00;65.00;1975.;15.2;79;Japan\n',
 'Dodge Colt Hatchback Custom;35.7;4;98.00;80.00;1915.;14.4;79;US\n',
 'AMC Spirit DL;27.4;4;121.0;80.00;2670.;15.0;79;US\n',
 'Mercedes Benz 300d;25.4;5;183.0;77.00;3530.;20.1;79;Europe\n',
 'Cadillac Eldorado;23.0;8;350.0;125.0;3900.;17.4;79;US\n',
 'Peugeot 504;27.2;4;141.0;71.00;3190.;24.8;79;Europe\n',
 'Oldsmobile Cutlass Salon Brougham;23.9;8;260.0;90.00;3420.;22.2;79;US\n',
 'Plymouth Horizon;34.2;4;105.0;70.00;2200.;13.2;79;US\n',
 'Plymouth Horizon TC3;34.5;4;105.0;70.00;2150.;14.9;79;US\n',
 'Datsun 210;31.8;4;85.00;65.00;2020.;19.2;79;Japan\n',
 'Fiat Strada Custom;37.3;4;91.00;69.00;2130.;14.7;79;Europe\n',
 'Buick Skylark Limited;28.4;4;151.0;90.00;2670.;16.0;79;US\n',
 'Chevrolet Citation;28.8;6;173.0;115.0;2595.;11.3;79;US\n',
 'Oldsmobile Omega Brougham;26.8;6;173.0;115.0;2700.;12.9;79;US\n',
 'Pontiac Phoenix;33.5;4;151.0;90.00;2556.;13.2;79;US\n',
 'Volkswagen Rabbit;41.5;4;98.00;76.00;2144.;14.7;80;Europe\n',
 'Toyota Corolla Tercel;38.1;4;89.00;60.00;1968.;18.8;80;Japan\n',
 'Chevrolet Chevette;32.1;4;98.00;70.00;2120.;15.5;80;US\n',
 'Datsun 310;37.2;4;86.00;65.00;2019.;16.4;80;Japan\n',
 'Chevrolet Citation;28.0;4;151.0;90.00;2678.;16.5;80;US\n',
 'Ford Fairmont;26.4;4;140.0;88.00;2870.;18.1;80;US\n',
 'AMC Concord;24.3;4;151.0;90.00;3003.;20.1;80;US\n',
 'Dodge Aspen;19.1;6;225.0;90.00;3381.;18.7;80;US\n',
 'Audi 4000;34.3;4;97.00;78.00;2188.;15.8;80;Europe\n',
 'Toyota Corolla Liftback;29.8;4;134.0;90.00;2711.;15.5;80;Japan\n',
 'Mazda 626;31.3;4;120.0;75.00;2542.;17.5;80;Japan\n',
 'Datsun 510 Hatchback;37.0;4;119.0;92.00;2434.;15.0;80;Japan\n',
 'Toyota Corolla;32.2;4;108.0;75.00;2265.;15.2;80;Japan\n',
 'Mazda GLC;46.6;4;86.00;65.00;2110.;17.9;80;Japan\n',
 'Dodge Colt;27.9;4;156.0;105.0;2800.;14.4;80;US\n',
 'Datsun 210;40.8;4;85.00;65.00;2110.;19.2;80;Japan\n',
 'Volkswagen Rabbit C (Diesel);44.3;4;90.00;48.00;2085.;21.7;80;Europe\n',
 'Volkswagen Dasher (diesel);43.4;4;90.00;48.00;2335.;23.7;80;Europe\n',
 'Audi 5000s (diesel);36.4;5;121.0;67.00;2950.;19.9;80;Europe\n',
 'Mercedes-Benz 240d;30.0;4;146.0;67.00;3250.;21.8;80;Europe\n',
 'Honda Civic 1500 gl;44.6;4;91.00;67.00;1850.;13.8;80;Japan\n',
 'Renault Lecar Deluxe;40.9;4;85.00;0;1835.;17.3;80;Europe\n',
 'Subaru DL;33.8;4;97.00;67.00;2145.;18.0;80;Japan\n',
 'Volkswagen Rabbit;29.8;4;89.00;62.00;1845.;15.3;80;Europe\n',
 'Datsun 280-ZX;32.7;6;168.0;132.0;2910.;11.4;80;Japan\n',
 'Mazda RX-7 GS;23.7;3;70.00;100.0;2420.;12.5;80;Japan\n',
 'Triumph TR7 Coupe;35.0;4;122.0;88.00;2500.;15.1;80;Europe\n',
 'Ford Mustang Cobra;23.6;4;140.0;0;2905.;14.3;80;US\n',
 'Honda Accord;32.4;4;107.0;72.00;2290.;17.0;80;Japan\n',
 'Plymouth Reliant;27.2;4;135.0;84.00;2490.;15.7;81;US\n',
 'Buick Skylark;26.6;4;151.0;84.00;2635.;16.4;81;US\n',
 'Dodge Aries Wagon (sw);25.8;4;156.0;92.00;2620.;14.4;81;US\n',
 'Chevrolet Citation;23.5;6;173.0;110.0;2725.;12.6;81;US\n',
 'Plymouth Reliant;30.0;4;135.0;84.00;2385.;12.9;81;US\n',
 'Toyota Starlet;39.1;4;79.00;58.00;1755.;16.9;81;Japan\n',
 'Plymouth Champ;39.0;4;86.00;64.00;1875.;16.4;81;US\n',
 'Honda Civic 1300;35.1;4;81.00;60.00;1760.;16.1;81;Japan\n',
 'Subaru;32.3;4;97.00;67.00;2065.;17.8;81;Japan\n',
 'Datsun 210 MPG;37.0;4;85.00;65.00;1975.;19.4;81;Japan\n',
 'Toyota Tercel;37.7;4;89.00;62.00;2050.;17.3;81;Japan\n',
 'Mazda GLC 4;34.1;4;91.00;68.00;1985.;16.0;81;Japan\n',
 'Plymouth Horizon 4;34.7;4;105.0;63.00;2215.;14.9;81;US\n',
 'Ford Escort 4W;34.4;4;98.00;65.00;2045.;16.2;81;US\n',
 'Ford Escort 2H;29.9;4;98.00;65.00;2380.;20.7;81;US\n',
 'Volkswagen Jetta;33.0;4;105.0;74.00;2190.;14.2;81;Europe\n',
 'Renault 18i;34.5;4;100.0;0;2320.;15.8;81;Europe\n',
 'Honda Prelude;33.7;4;107.0;75.00;2210.;14.4;81;Japan\n',
 'Toyota Corolla;32.4;4;108.0;75.00;2350.;16.8;81;Japan\n',
 'Datsun 200SX;32.9;4;119.0;100.0;2615.;14.8;81;Japan\n',
 'Mazda 626;31.6;4;120.0;74.00;2635.;18.3;81;Japan\n',
 'Peugeot 505s Turbo Diesel;28.1;4;141.0;80.00;3230.;20.4;81;Europe\n',
 'Saab 900s;0;4;121.0;110.0;2800.;15.4;81;Europe\n',
 'Volvo Diesel;30.7;6;145.0;76.00;3160.;19.6;81;Europe\n',
 'Toyota Cressida;25.4;6;168.0;116.0;2900.;12.6;81;Japan\n',
 'Datsun 810 Maxima;24.2;6;146.0;120.0;2930.;13.8;81;Japan\n',
 'Buick Century;22.4;6;231.0;110.0;3415.;15.8;81;US\n',
 'Oldsmobile Cutlass LS;26.6;8;350.0;105.0;3725.;19.0;81;US\n',
 'Ford Grenada gl;20.2;6;200.0;88.00;3060.;17.1;81;US\n',
 'Chrysler Lebaron Salon;17.6;6;225.0;85.00;3465.;16.6;81;US\n',
 'Chevrolet Cavalier;28.0;4;112.0;88.00;2605.;19.6;82;US\n',
 'Chevrolet Cavalier Wagon;27.0;4;112.0;88.00;2640.;18.6;82;US\n',
 'Chevrolet Cavalier 2-door;34.0;4;112.0;88.00;2395.;18.0;82;US\n',
 'Pontiac J2000 SE Hatchback;31.0;4;112.0;85.00;2575.;16.2;82;US\n',
 'Dodge Aries SE;29.0;4;135.0;84.00;2525.;16.0;82;US\n',
 'Pontiac Phoenix;27.0;4;151.0;90.00;2735.;18.0;82;US\n',
 'Ford Fairmont Futura;24.0;4;140.0;92.00;2865.;16.4;82;US\n',
 'AMC Concord DL;23.0;4;151.0;0;3035.;20.5;82;US\n',
 'Volkswagen Rabbit l;36.0;4;105.0;74.00;1980.;15.3;82;Europe\n',
 'Mazda GLC Custom l;37.0;4;91.00;68.00;2025.;18.2;82;Japan\n',
 'Mazda GLC Custom;31.0;4;91.00;68.00;1970.;17.6;82;Japan\n',
 'Plymouth Horizon Miser;38.0;4;105.0;63.00;2125.;14.7;82;US\n',
 'Mercury Lynx l;36.0;4;98.00;70.00;2125.;17.3;82;US\n',
 'Nissan Stanza XE;36.0;4;120.0;88.00;2160.;14.5;82;Japan\n',
 'Honda Accord;36.0;4;107.0;75.00;2205.;14.5;82;Japan\n',
 'Toyota Corolla;34.0;4;108.0;70.00;2245;16.9;82;Japan\n',
 'Honda Civic;38.0;4;91.00;67.00;1965.;15.0;82;Japan\n',
 'Honda Civic (auto);32.0;4;91.00;67.00;1965.;15.7;82;Japan\n',
 'Datsun 310 GX;38.0;4;91.00;67.00;1995.;16.2;82;Japan\n',
 'Buick Century Limited;25.0;6;181.0;110.0;2945.;16.4;82;US\n',
 'Oldsmobile Cutlass Ciera (diesel);38.0;6;262.0;85.00;3015.;17.0;82;US\n',
 'Chrysler Lebaron Medallion;26.0;4;156.0;92.00;2585.;14.5;82;US\n',
 'Ford Grenada l;22.0;6;232.0;112.0;2835;14.7;82;US\n',
 'Toyota Celica GT;32.0;4;144.0;96.00;2665.;13.9;82;Japan\n',
 'Dodge Charger 2.2;36.0;4;135.0;84.00;2370.;13.0;82;US\n',
 'Chevrolet Camaro;27.0;4;151.0;90.00;2950.;17.3;82;US\n',
 'Ford Mustang GL;27.0;4;140.0;86.00;2790.;15.6;82;US\n',
 'Volkswagen Pickup;44.0;4;97.00;52.00;2130.;24.6;82;Europe\n',
 'Dodge Rampage;32.0;4;135.0;84.00;2295.;11.6;82;US\n',
 'Ford Ranger;28.0;4;120.0;79.00;2625.;18.6;82;US\n',
 'Chevy S-10;31.0;4;119.0;82.00;2720.;19.4;82;US\n']
So you might be wondering which method to use? Use the readlines() method, or use the iterator methods?

Especially if you ending up reading the entire file - would one method be better than the other?

Consider this example, where we want to find out all the different origins in the file (last column of each row) - let's do this using both approaches.
'''
origins = set()
with open('cars.csv') as f:
    rows = f.readlines()
for row in rows[2:]:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)
print(origins)
#{'Japan', 'Europe', 'US'}
origins = set()
with open('cars.csv') as f:
    next(f), next(f)
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)
print(origins)
#{'Japan', 'Europe', 'US'}
# =============================================================================
# Now consider the first approach: we loaded the entire file into memory (a list), and then iterated through all the rows.
# 
# But in the second approach, we still iterated through all the rows, but we only need to store one row at a time - the overhead was therefore far smaller.
# 
# Often we can process files one row at a time and loading the entire file first, especially for huge files, is not always desirable.
# 
# The enumerate function is another lazy iterator:
# =============================================================================

e = enumerate('Python rocks!')
print('__iter__' in dir(e))
print('__next__' in dir(e))
True
True
iter(e)
#<enumerate at 0x1d75df12fc0>
e
#<enumerate at 0x1d75df12fc0>
# =============================================================================
# As we can see, the object and its iterator are the same object.
# 
# But enumerate is also lazy, so we need to iterate through it in order to recover all the elements:
# =============================================================================

list(e)
'''
[(0, 'P'),
 (1, 'y'),
 (2, 't'),
 (3, 'h'),
 (4, 'o'),
 (5, 'n'),
 (6, ' '),
 (7, 'r'),
 (8, 'o'),
 (9, 'c'),
 (10, 'k'),
 (11, 's'),
 (12, '!')]
Of course, once we have exhausted the iterator, we cannot use it again:
'''
list(e)
#[]
#The dictionary object provides methods that return iterables for the keys, values or tuples of key/value pairs:

d = {'a': 1, 'b': 2}
keys = d.keys()
'__iter__' in dir(keys), '__next__' in dir(keys)
#(True, False)
#More simply, we can just test to see if iter(keys) is the same object as keys - if not then we are dealing with an iterable.

iter(keys) is keys
# =============================================================================
# False
# So we have an iterable.
# 
# Similarly for .values() and .items():
# =============================================================================

values = d.values()
iter(values) is values
# =============================================================================
# False
# =============================================================================
items = d.items()
iter(items) is items
# =============================================================================
# False
# =============================================================================
# =============================================================================
# There are many other such functions and methods in Python, and we'll cover more of them in some upcoming videos
# =============================================================================

#Just be careful and know whether you are dealing with an iterable or an iterator. You can iterate and iterable over and over again, but can only do so once with an iterator.

​

EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:arduino
LIBS:flypi_components
LIBS:Arduino_Nano-cache
LIBS:flypi-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L BARREL_JACK CON1
U 1 1 577DE532
P 1600 1550
F 0 "CON1" H 1600 1800 50  0000 C CNN
F 1 "BARREL_JACK" H 1600 1350 50  0000 C CNN
F 2 "Connect:BARREL_JACK" H 1600 1550 50  0001 C CNN
F 3 "" H 1600 1550 50  0000 C CNN
	1    1600 1550
	1    0    0    -1  
$EndComp
$Comp
L arduino_mini U5
U 1 1 577DE666
P 6750 4900
F 0 "U5" H 7250 3950 70  0000 C CNN
F 1 "arduino_mini" H 7500 3850 70  0000 C CNN
F 2 "arduino_nano:DIP-30_W15.24mm_LongPads" H 6750 4850 60  0001 C CNN
F 3 "" H 6750 4900 60  0000 C CNN
	1    6750 4900
	1    0    0    -1  
$EndComp
$Comp
L LM2596 U1
U 1 1 577DEF55
P 3300 1300
F 0 "U1" H 3500 1300 60  0000 C CNN
F 1 "LM2596" H 3250 1300 60  0000 C CNN
F 2 "footprints:LM2596" H 3500 1300 60  0001 C CNN
F 3 "" H 3500 1300 60  0000 C CNN
	1    3300 1300
	1    0    0    -1  
$EndComp
$Comp
L CP1 C2
U 1 1 577DF0B8
P 2450 1300
F 0 "C2" H 2475 1400 50  0000 L CNN
F 1 "680µ" H 2475 1200 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D10_L21_P5" H 2450 1300 50  0001 C CNN
F 3 "" H 2450 1300 50  0000 C CNN
	1    2450 1300
	0    -1   -1   0   
$EndComp
$Comp
L D_Schottky D1
U 1 1 577DF1F1
P 3300 1100
F 0 "D1" H 3300 1200 50  0000 C CNN
F 1 "Schottky 5A" H 3300 1000 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_DO-201AD_Horizontal_RM15" H 3300 1100 50  0001 C CNN
F 3 "" H 3300 1100 50  0000 C CNN
	1    3300 1100
	-1   0    0    1   
$EndComp
$Comp
L CP1 C6
U 1 1 577DF33D
P 4350 1700
F 0 "C6" H 4375 1800 50  0000 L CNN
F 1 "220µ" H 4375 1600 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D8_L13_P3.8" H 4350 1700 50  0001 C CNN
F 3 "" H 4350 1700 50  0000 C CNN
	1    4350 1700
	1    0    0    -1  
$EndComp
$Comp
L CP1 C3
U 1 1 577DF624
P 2450 2650
F 0 "C3" H 2475 2750 50  0000 L CNN
F 1 "680µ" H 2475 2550 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D10_L21_P5" H 2450 2650 50  0001 C CNN
F 3 "" H 2450 2650 50  0000 C CNN
	1    2450 2650
	0    -1   -1   0   
$EndComp
$Comp
L CP1 C4
U 1 1 577DF6C1
P 4250 2800
F 0 "C4" H 4275 2900 50  0000 L CNN
F 1 "220µ" H 4275 2700 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D8_L13_P3.8" H 4250 2800 50  0001 C CNN
F 3 "" H 4250 2800 50  0000 C CNN
	1    4250 2800
	1    0    0    -1  
$EndComp
$Comp
L LM2596 U3
U 1 1 577DF744
P 3350 2400
F 0 "U3" H 3550 2400 60  0000 C CNN
F 1 "LM2596" H 3300 2400 60  0000 C CNN
F 2 "footprints:LM2596" H 3550 2400 60  0001 C CNN
F 3 "" H 3550 2400 60  0000 C CNN
	1    3350 2400
	1    0    0    -1  
$EndComp
$Comp
L D_Schottky D2
U 1 1 577DF7A9
P 3300 2200
F 0 "D2" H 3300 2300 50  0000 C CNN
F 1 "Schottky 5A" H 3300 2100 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_DO-201AD_Horizontal_RM15" H 3300 2200 50  0001 C CNN
F 3 "" H 3300 2200 50  0000 C CNN
	1    3300 2200
	-1   0    0    1   
$EndComp
$Comp
L Q_NPN_ECB Q2
U 1 1 577E148F
P 5350 2350
F 0 "Q2" H 5650 2400 50  0000 R CNN
F 1 "1A-NPN-ECB" H 5950 2300 50  0000 R CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 5550 2450 50  0001 C CNN
F 3 "" H 5350 2350 50  0000 C CNN
	1    5350 2350
	0    -1   -1   0   
$EndComp
$Comp
L R R2
U 1 1 577E166B
P 5350 2850
F 0 "R2" V 5430 2850 50  0000 C CNN
F 1 "270" V 5350 2850 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 5280 2850 50  0001 C CNN
F 3 "" H 5350 2850 50  0000 C CNN
	1    5350 2850
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 577E1F76
P 10000 1100
F 0 "R7" V 10080 1100 50  0000 C CNN
F 1 "220" V 10000 1100 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 9930 1100 50  0001 C CNN
F 3 "" H 10000 1100 50  0000 C CNN
	1    10000 1100
	0    1    1    0   
$EndComp
$Comp
L R R8
U 1 1 577E209A
P 10000 1300
F 0 "R8" V 10080 1300 50  0000 C CNN
F 1 "220" V 10000 1300 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 9930 1300 50  0001 C CNN
F 3 "" H 10000 1300 50  0000 C CNN
	1    10000 1300
	0    1    1    0   
$EndComp
$Comp
L R R9
U 1 1 577E210B
P 10000 1500
F 0 "R9" V 10080 1500 50  0000 C CNN
F 1 "220" V 10000 1500 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 9930 1500 50  0001 C CNN
F 3 "" H 10000 1500 50  0000 C CNN
	1    10000 1500
	0    1    1    0   
$EndComp
$Comp
L Q_NPN_ECB Q3
U 1 1 577E2D68
P 6100 2350
F 0 "Q3" H 6400 2400 50  0000 R CNN
F 1 "1A_NPN_ECB" H 6700 2300 50  0000 R CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 6300 2450 50  0001 C CNN
F 3 "" H 6100 2350 50  0000 C CNN
	1    6100 2350
	0    -1   -1   0   
$EndComp
$Comp
L R R4
U 1 1 577E2E07
P 6100 2850
F 0 "R4" V 6180 2850 50  0000 C CNN
F 1 "270" V 6100 2850 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 6030 2850 50  0001 C CNN
F 3 "" H 6100 2850 50  0000 C CNN
	1    6100 2850
	1    0    0    -1  
$EndComp
$Comp
L CP1 C1
U 1 1 577E326D
P 2400 3800
F 0 "C1" H 2425 3900 50  0000 L CNN
F 1 "680µ" H 2425 3700 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D10_L21_P5" H 2400 3800 50  0001 C CNN
F 3 "" H 2400 3800 50  0000 C CNN
	1    2400 3800
	0    -1   -1   0   
$EndComp
$Comp
L CP1 C5
U 1 1 577E33E2
P 4300 4250
F 0 "C5" H 4325 4350 50  0000 L CNN
F 1 "220µ" H 4325 4150 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D8_L13_P3.8" H 4300 4250 50  0001 C CNN
F 3 "" H 4300 4250 50  0000 C CNN
	1    4300 4250
	1    0    0    -1  
$EndComp
$Comp
L D_Schottky D3
U 1 1 577E34B5
P 3300 3350
F 0 "D3" H 3300 3450 50  0000 C CNN
F 1 "D_Schottky" H 3300 3250 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_DO-201AD_Horizontal_RM15" H 3300 3350 50  0001 C CNN
F 3 "" H 3300 3350 50  0000 C CNN
	1    3300 3350
	-1   0    0    1   
$EndComp
$Comp
L LM2596 U2
U 1 1 577E3581
P 3300 3550
F 0 "U2" H 3500 3550 60  0000 C CNN
F 1 "LM2596" H 3250 3550 60  0000 C CNN
F 2 "footprints:LM2596" H 3500 3550 60  0001 C CNN
F 3 "" H 3500 3550 60  0000 C CNN
	1    3300 3550
	1    0    0    -1  
$EndComp
$Comp
L INDUCTOR L1
U 1 1 577E380E
P 4000 3350
F 0 "L1" V 3950 3350 50  0000 C CNN
F 1 "33µH" V 4100 3350 50  0000 C CNN
F 2 "Inductors_NEOSID:Neosid_Inductor_MA-Bs75" H 4000 3350 50  0001 C CNN
F 3 "" H 4000 3350 50  0000 C CNN
	1    4000 3350
	0    -1   -1   0   
$EndComp
$Comp
L INDUCTOR L3
U 1 1 577E390F
P 4150 2450
F 0 "L3" V 4100 2450 50  0000 C CNN
F 1 "33µH" V 4250 2450 50  0000 C CNN
F 2 "Inductors_NEOSID:Neosid_Inductor_MA-Bs75" H 4150 2450 50  0001 C CNN
F 3 "" H 4150 2450 50  0000 C CNN
	1    4150 2450
	0    -1   -1   0   
$EndComp
$Comp
L INDUCTOR L2
U 1 1 577E530A
P 4100 1300
F 0 "L2" V 4050 1300 50  0000 C CNN
F 1 "33µH" V 4200 1300 50  0000 C CNN
F 2 "Inductors_NEOSID:Neosid_Inductor_MA-Bs75" H 4100 1300 50  0001 C CNN
F 3 "" H 4100 1300 50  0000 C CNN
	1    4100 1300
	0    -1   -1   0   
$EndComp
$Comp
L Q_NPN_ECB Q4
U 1 1 577E5AE1
P 6800 2350
F 0 "Q4" H 7100 2400 50  0000 R CNN
F 1 "1A_NPN_ECB" H 7400 2300 50  0000 R CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 7000 2450 50  0001 C CNN
F 3 "" H 6800 2350 50  0000 C CNN
	1    6800 2350
	0    -1   -1   0   
$EndComp
$Comp
L R R5
U 1 1 577E5D84
P 6800 2850
F 0 "R5" V 6880 2850 50  0000 C CNN
F 1 "270" V 6800 2850 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 6730 2850 50  0001 C CNN
F 3 "" H 6800 2850 50  0000 C CNN
	1    6800 2850
	1    0    0    -1  
$EndComp
$Comp
L L298N U4
U 1 1 577E6C96
P 3750 5150
F 0 "U4" H 4000 5150 60  0000 C CNN
F 1 "L298N" H 3750 5150 60  0000 C CNN
F 2 "TO_SOT_Packages_THT:Multiwatt_15_Vertical" H 3750 5150 60  0001 C CNN
F 3 "" H 3750 5150 60  0000 C CNN
	1    3750 5150
	1    0    0    -1  
$EndComp
$Comp
L C C10
U 1 1 577E79E9
P 2850 6100
F 0 "C10" H 2875 6200 50  0000 L CNN
F 1 "100n" H 2875 6000 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 2888 5950 50  0001 C CNN
F 3 "" H 2850 6100 50  0000 C CNN
	1    2850 6100
	-1   0    0    1   
$EndComp
$Comp
L C C7
U 1 1 577E7EFE
P 4700 5550
F 0 "C7" H 4725 5650 50  0000 L CNN
F 1 "100n" H 4725 5450 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 4738 5400 50  0001 C CNN
F 3 "" H 4700 5550 50  0000 C CNN
	1    4700 5550
	1    0    0    -1  
$EndComp
NoConn ~ 4400 6600
NoConn ~ 4400 6400
NoConn ~ 4400 6200
NoConn ~ 4400 6000
NoConn ~ 4400 5800
NoConn ~ 4400 5600
$Comp
L R R1
U 1 1 577E8665
P 2900 4910
F 0 "R1" H 2900 4910 60  0000 C CNN
F 1 "20W " H 2950 5010 60  0000 C CNN
F 2 "TO_SOT_Packages_THT:TO-220-2_Vertical" H 2900 4910 60  0001 C CNN
F 3 "" H 2900 4910 60  0000 C CNN
	1    2900 4910
	-1   0    0    1   
$EndComp
$Comp
L Q_NPN_ECB Q1
U 1 1 577EB1CC
P 5200 4900
F 0 "Q1" H 5500 4950 50  0000 R CNN
F 1 "1A_NPN_ECB" H 5800 4850 50  0000 R CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 5400 5000 50  0001 C CNN
F 3 "" H 5200 4900 50  0000 C CNN
	1    5200 4900
	-1   0    0    1   
$EndComp
$Comp
L R R3
U 1 1 577EB79F
P 5550 5050
F 0 "R3" V 5630 5050 50  0000 C CNN
F 1 "270" V 5550 5050 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 5480 5050 50  0001 C CNN
F 3 "" H 5550 5050 50  0000 C CNN
	1    5550 5050
	1    0    0    -1  
$EndComp
NoConn ~ 6050 4500
NoConn ~ 6050 4800
NoConn ~ 6050 4900
NoConn ~ 6050 5000
NoConn ~ 6050 5300
NoConn ~ 6050 4700
NoConn ~ 6050 6200
NoConn ~ 7450 5600
NoConn ~ 7450 5700
NoConn ~ 7450 4350
NoConn ~ 6900 3750
$Comp
L Conn_01x03 P4
U 1 1 577F06E4
P 5200 6650
F 0 "P4" H 5200 6850 50  0000 C CNN
F 1 "Therm +s-" V 5300 6650 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S03B-EH_03x2.50mm_Angled" H 5200 6650 50  0001 C CNN
F 3 "" H 5200 6650 50  0000 C CNN
	1    5200 6650
	0    1    1    0   
$EndComp
$Comp
L R 1k1
U 1 1 577F0E14
P 5200 6100
F 0 "1k1" V 5280 6100 50  0000 C CNN
F 1 "R" V 5200 6100 50  0000 C CNN
F 2 "Resistors_THT:R_Box_L13.0mm_W4.0mm_P9.00mm" V 5130 6100 50  0001 C CNN
F 3 "" H 5200 6100 50  0000 C CNN
	1    5200 6100
	1    0    0    -1  
$EndComp
$Comp
L C C8
U 1 1 577F0EB3
P 5200 5550
F 0 "C8" H 5225 5650 50  0000 L CNN
F 1 "100n" H 5225 5450 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 5238 5400 50  0001 C CNN
F 3 "" H 5200 5550 50  0000 C CNN
	1    5200 5550
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x03 P8
U 1 1 577F19C2
P 7900 700
F 0 "P8" H 7900 900 50  0000 C CNN
F 1 "Ring +-s" V 8000 700 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S03B-EH_03x2.50mm_Angled" H 7900 700 50  0001 C CNN
F 3 "" H 7900 700 50  0000 C CNN
	1    7900 700 
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x04 P9
U 1 1 577F1F65
P 8750 1350
F 0 "P9" H 8750 1600 50  0000 C CNN
F 1 "matrix +-scsd" V 8850 1350 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S04B-EH_04x2.50mm_Angled" H 8750 1350 50  0001 C CNN
F 3 "" H 8750 1350 50  0000 C CNN
	1    8750 1350
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x03 P7
U 1 1 577F2704
P 7100 1350
F 0 "P7" H 7100 1550 50  0000 C CNN
F 1 "servo +s-" V 7200 1350 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S03B-EH_03x2.50mm_Angled" H 7100 1350 50  0001 C CNN
F 3 "" H 7100 1350 50  0000 C CNN
	1    7100 1350
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x02 P6
U 1 1 577F293A
P 6350 1350
F 0 "P6" H 6350 1500 50  0000 C CNN
F 1 "HP2+-" V 6450 1350 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S02B-EH_02x2.50mm_Angled" H 6350 1350 50  0001 C CNN
F 3 "" H 6350 1350 50  0000 C CNN
	1    6350 1350
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x02 P5
U 1 1 577F29F3
P 5650 1350
F 0 "P5" H 5650 1500 50  0000 C CNN
F 1 "HP1+-" V 5750 1350 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S02B-EH_02x2.50mm_Angled" H 5650 1350 50  0001 C CNN
F 3 "" H 5650 1350 50  0000 C CNN
	1    5650 1350
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x04 P10
U 1 1 577F3156
P 10700 1200
F 0 "P10" H 10700 1450 50  0000 C CNN
F 1 "RGB RG-B" V 10800 1200 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S04B-EH_04x2.50mm_Angled" H 10700 1200 50  0001 C CNN
F 3 "" H 10700 1200 50  0000 C CNN
	1    10700 1200
	1    0    0    -1  
$EndComp
NoConn ~ 6050 6100
$Comp
L Conn_01x02 P1
U 1 1 577F4FBB
P 1650 5500
F 0 "P1" H 1650 5650 50  0000 C CNN
F 1 "PeltS1S2" V 1750 5500 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S02B-EH_02x2.50mm_Angled" H 1650 5500 50  0001 C CNN
F 3 "" H 1650 5500 50  0000 C CNN
	1    1650 5500
	-1   0    0    1   
$EndComp
$Comp
L Conn_01x02 P3
U 1 1 577F82F4
P 5100 4350
F 0 "P3" H 5100 4500 50  0000 C CNN
F 1 "Fan+-" V 5200 4350 50  0000 C CNN
F 2 "Connectors_JST:JST_EH_S02B-EH_02x2.50mm_Angled" H 5100 4350 50  0001 C CNN
F 3 "" H 5100 4350 50  0000 C CNN
	1    5100 4350
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1900 1650 2900 1650
Wire Wire Line
	1900 1450 2900 1450
Connection ~ 2200 1650
Wire Wire Line
	2800 1850 2900 1850
Wire Wire Line
	2800 1100 2800 1950
Connection ~ 2800 1650
Wire Wire Line
	2300 1300 2300 1450
Connection ~ 2300 1450
Wire Wire Line
	2600 1300 2600 1650
Connection ~ 2600 1650
Wire Wire Line
	2800 1100 3150 1100
Wire Wire Line
	3450 1100 3750 1100
Wire Wire Line
	3750 1100 3750 1550
Wire Wire Line
	4100 1750 3750 1750
Wire Wire Line
	4100 1550 5020 1550
Wire Wire Line
	1900 1650 1900 1550
Wire Wire Line
	3450 2200 3800 2200
Wire Wire Line
	3800 2200 3800 2650
Wire Wire Line
	3800 2650 3950 2650
Wire Wire Line
	4050 2850 3800 2850
Connection ~ 2800 1850
Wire Wire Line
	4800 1490 4800 1950
Connection ~ 4350 1550
Wire Wire Line
	4800 1950 2800 1950
Wire Wire Line
	4350 1850 4350 1950
Connection ~ 4350 1950
Wire Wire Line
	5350 2550 5350 2700
Wire Wire Line
	5150 2650 5150 2250
Connection ~ 4250 2650
Wire Wire Line
	5550 2250 5600 2250
Wire Wire Line
	5600 2250 5600 1550
Wire Wire Line
	5700 3100 5700 1550
Wire Wire Line
	6100 2700 6100 2550
Wire Wire Line
	6300 2250 6300 1550
Wire Wire Line
	6400 3100 6400 1550
Connection ~ 5700 3100
Wire Wire Line
	5900 2650 5900 2250
Connection ~ 5150 2650
Wire Wire Line
	3850 2450 3850 2550
Wire Wire Line
	3850 2550 3950 2550
Wire Wire Line
	3950 2550 3950 2650
Wire Wire Line
	4450 2550 4450 2450
Wire Wire Line
	3750 3500 3750 3800
Wire Wire Line
	3750 3500 3700 3500
Wire Wire Line
	3700 3500 3700 3350
Wire Wire Line
	3700 3350 3450 3350
Wire Wire Line
	2200 3350 3150 3350
Wire Wire Line
	2200 4100 2900 4100
Wire Wire Line
	2900 3700 2250 3700
Wire Wire Line
	2250 3700 2250 3800
Wire Wire Line
	2050 1450 2050 5900
Connection ~ 2050 1450
Wire Wire Line
	2250 3800 2050 3800
Wire Wire Line
	2200 1650 2200 6950
Wire Wire Line
	2550 3800 2700 3800
Wire Wire Line
	2900 3900 2700 3900
Connection ~ 2700 3900
Wire Wire Line
	4300 3350 4300 4100
Wire Wire Line
	4300 4000 3750 4000
Connection ~ 4300 4000
Wire Wire Line
	2200 4400 4300 4400
Connection ~ 2700 4100
Wire Wire Line
	4400 1300 4400 1400
Wire Wire Line
	3800 1300 3750 1300
Connection ~ 3750 1300
Wire Wire Line
	4100 1550 4100 1750
Wire Wire Line
	4400 1400 4350 1400
Wire Wire Line
	4350 1400 4350 1550
Wire Wire Line
	7000 1550 7000 2250
Wire Wire Line
	6600 2650 6600 2250
Connection ~ 5900 2650
Wire Wire Line
	6800 2550 6800 2700
Wire Wire Line
	7200 3100 7200 1550
Connection ~ 6400 3100
Wire Wire Line
	10150 1100 10500 1100
Wire Wire Line
	10150 1300 10500 1300
Wire Wire Line
	10500 1400 10500 1500
Wire Wire Line
	10500 1500 10150 1500
Wire Wire Line
	2050 5900 3100 5900
Connection ~ 2050 3800
Wire Wire Line
	2200 6700 3100 6700
Wire Wire Line
	2850 5900 2850 5950
Connection ~ 2850 5900
Wire Wire Line
	2850 6250 2850 7000
Connection ~ 2850 6700
Wire Wire Line
	4400 5400 4700 5400
Wire Wire Line
	4700 5700 4700 7000
Wire Wire Line
	4700 7000 2850 7000
Wire Wire Line
	2200 4600 2900 4600
Wire Wire Line
	2900 5300 3100 5300
Wire Wire Line
	2300 5700 3100 5700
Wire Wire Line
	8850 1550 8850 3450
Wire Wire Line
	8950 1550 8950 3550
Wire Wire Line
	4300 3350 8650 3350
Wire Wire Line
	8850 3450 5800 3450
Wire Wire Line
	5800 3450 5800 5200
Wire Wire Line
	5800 5200 6050 5200
Wire Wire Line
	8950 3550 5900 3550
Wire Wire Line
	5900 3550 5900 5100
Wire Wire Line
	5900 5100 6050 5100
Wire Wire Line
	7450 4950 9400 4950
Wire Wire Line
	9400 4950 9400 1100
Wire Wire Line
	9400 1100 9850 1100
Wire Wire Line
	7450 5200 9550 5200
Wire Wire Line
	9550 5200 9550 1300
Wire Wire Line
	9550 1300 9850 1300
Wire Wire Line
	9850 1500 9700 1500
Wire Wire Line
	9700 1500 9700 5300
Wire Wire Line
	9700 5300 7450 5300
Wire Wire Line
	8000 4850 7450 4850
Wire Wire Line
	8000 900  8000 4850
Wire Wire Line
	7450 4750 7700 4750
Wire Wire Line
	7700 4750 7700 1700
Wire Wire Line
	7700 1700 7100 1700
Wire Wire Line
	7100 1700 7100 1550
Wire Wire Line
	7450 4650 7600 4650
Wire Wire Line
	7600 4650 7600 3000
Wire Wire Line
	7600 3000 6800 3000
Wire Wire Line
	7450 4250 7450 3250
Wire Wire Line
	7450 3250 5700 3250
Wire Wire Line
	5700 3250 5700 7100
Wire Wire Line
	5700 7100 2900 7100
Wire Wire Line
	2900 7100 2900 6300
Wire Wire Line
	2900 6300 3100 6300
Wire Wire Line
	7450 5400 8250 5400
Wire Wire Line
	8250 5400 8250 6500
Wire Wire Line
	2950 7150 6950 7150
Wire Wire Line
	2950 7150 2950 6100
Wire Wire Line
	2950 6100 3100 6100
Wire Wire Line
	7450 5500 8200 5500
Wire Wire Line
	8200 5500 8200 6450
Wire Wire Line
	3000 7050 6900 7050
Wire Wire Line
	3000 7050 3000 6500
Wire Wire Line
	3000 6500 3100 6500
Wire Wire Line
	2200 6950 6750 6950
Wire Wire Line
	6750 6950 6750 6450
Wire Wire Line
	5100 4700 5100 4550
Wire Wire Line
	5400 4900 5550 4900
Wire Wire Line
	5700 5250 5550 5250
Wire Wire Line
	5550 5250 5550 5200
Connection ~ 5700 5250
Wire Wire Line
	4700 5400 4700 3650
Wire Wire Line
	4700 3650 6750 3650
Wire Wire Line
	6750 3650 6750 3750
Wire Wire Line
	5100 5100 3300 5100
Wire Wire Line
	3300 5100 3300 4500
Wire Wire Line
	3300 4500 2050 4500
Connection ~ 2050 4500
Wire Wire Line
	4800 4450 2050 4450
Connection ~ 2050 4450
Wire Wire Line
	7450 4550 7550 4550
Wire Wire Line
	7550 4550 7550 3150
Wire Wire Line
	7550 3150 5350 3150
Wire Wire Line
	5350 3150 5350 3000
Wire Wire Line
	7450 4450 7500 4450
Wire Wire Line
	7500 4450 7500 3200
Wire Wire Line
	7500 3200 6100 3200
Wire Wire Line
	6100 3200 6100 3000
Wire Wire Line
	4150 4700 5200 4700
Wire Wire Line
	5200 4700 5200 4550
Wire Wire Line
	4150 4550 4150 4700
Wire Wire Line
	2200 4550 4150 4550
Connection ~ 2200 4600
Connection ~ 2200 4550
Connection ~ 2200 4400
Connection ~ 2200 3350
Wire Wire Line
	2300 2550 2950 2550
Wire Wire Line
	2700 3800 2700 4100
Connection ~ 2200 4100
Wire Wire Line
	2200 2750 2950 2750
Wire Wire Line
	2600 2950 2950 2950
Wire Wire Line
	8750 3100 8750 1550
Wire Wire Line
	7900 3100 7900 900 
Connection ~ 7200 3100
Connection ~ 7900 3100
Wire Wire Line
	10350 3100 10350 1200
Wire Wire Line
	10350 1200 10500 1200
Connection ~ 8750 3100
Wire Wire Line
	5950 3650 5950 5950
Wire Wire Line
	5950 5950 5300 5950
Wire Wire Line
	5300 5950 5300 6450
Connection ~ 5950 3650
Wire Wire Line
	5100 6450 5100 6250
Wire Wire Line
	5100 6250 4850 6250
Wire Wire Line
	4850 5400 4850 6950
Connection ~ 4850 6950
Connection ~ 2200 6700
Wire Wire Line
	5200 5700 5200 5950
Wire Wire Line
	5200 5400 4850 5400
Connection ~ 4850 6250
Wire Wire Line
	5200 5700 5850 5700
Wire Wire Line
	5850 5700 5850 5400
Wire Wire Line
	5850 5400 6050 5400
Wire Wire Line
	5200 6250 5200 6450
Wire Wire Line
	8250 6500 6950 6500
Wire Wire Line
	6950 6500 6950 7150
Wire Wire Line
	6900 7050 6900 6450
Wire Wire Line
	6900 6450 8200 6450
Wire Wire Line
	7800 900  7800 3350
Wire Wire Line
	8650 3350 8650 1550
Connection ~ 7800 3350
Wire Wire Line
	2200 3100 10350 3100
Wire Wire Line
	4250 2950 4250 3100
Connection ~ 4250 3100
Connection ~ 2200 3100
Wire Wire Line
	3150 2200 2200 2200
Connection ~ 2200 2200
Wire Wire Line
	2300 2650 2050 2650
Connection ~ 2050 2650
Wire Wire Line
	2300 2650 2300 2550
Wire Wire Line
	2600 2650 2600 2950
Connection ~ 2200 2750
Connection ~ 2600 2750
Wire Wire Line
	4050 2650 6600 2650
Wire Wire Line
	4050 2650 4050 2850
Wire Wire Line
	4250 2650 4250 2550
Wire Wire Line
	4250 2550 4450 2550
Wire Wire Line
	4800 3750 4800 4450
$Comp
L GND #PWR01
U 1 1 577EB9A4
P 1800 2000
F 0 "#PWR01" H 1800 1750 50  0001 C CNN
F 1 "GND" H 1800 1850 50  0000 C CNN
F 2 "" H 1800 2000 50  0000 C CNN
F 3 "" H 1800 2000 50  0000 C CNN
	1    1800 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 2000 1800 1900
Wire Wire Line
	1800 1900 2200 1900
Connection ~ 2200 1900
Wire Wire Line
	4800 3750 6600 3750
$Comp
L USB_A J12
U 1 1 59ED406F
P 4820 1140
F 0 "J12" H 4620 1590 50  0000 L CNN
F 1 "USB_A" H 4620 1490 50  0000 L CNN
F 2 "Connectors:USB_A_Vertical" H 4970 1090 50  0001 C CNN
F 3 "" H 4970 1090 50  0001 C CNN
	1    4820 1140
	0    1    1    0   
$EndComp
NoConn ~ 4820 1440
NoConn ~ 4720 1440
Wire Wire Line
	4420 1040 4420 1230
Wire Wire Line
	4800 1490 4450 1490
Wire Wire Line
	4450 1490 4450 1230
Wire Wire Line
	4450 1230 4420 1230
Connection ~ 4420 1140
Wire Wire Line
	5020 1550 5020 1440
Wire Wire Line
	5600 1550 5650 1550
Wire Wire Line
	5700 1550 5750 1550
Wire Wire Line
	6300 1550 6350 1550
Wire Wire Line
	6400 1550 6450 1550
Wire Wire Line
	2900 4600 2900 4760
Wire Wire Line
	2900 5060 2900 5300
Wire Wire Line
	3100 5500 2900 5500
Wire Wire Line
	2900 5500 2900 5400
Wire Wire Line
	2900 5400 1850 5400
Wire Wire Line
	2300 5500 2300 5700
Wire Wire Line
	2300 5500 1850 5500
$EndSCHEMATC

# Notes on `FlyPi.scad`

## _Caution_

These parts have _not_ been printed to verify the design.  Although the design
has been checked carefully, it is possible that some parts may not function
as desired.  No warranty for any fitness of use is given or implied.

## Viewing modes

The design may be viewed in two different modes:

1. `EXPLODED_VIEW`: shows how the parts relate to one another in normal use.
2. `PRINTABLE_LAYOUT`: used to reduce the labour costs during printing by
 allowing multiple parts to be printed at the same time, and to be printed in
 an orientation compatible with fused filament fabrication.

The current view is controlled by setting the `assembly_location` variable near
the top of the file to equal either `EXPLODED_VIEW` or `PRINTABLE_LAYOUT`.

## About batches

There are variables that enable the printing of parts in batches.  
Batches are sets of connected parts that lie flat on the Z = 0 plane
and they are oriented to be printable with fused filament fabrication.  
Connection "wires" tie parts together, reducing the labour costs for printing.  
These connection wires should be cut off after the parts have been printed.

There are currently three batches of parts, and most of the parts in a batch are
related to each other. When viewing in `PRINTABLE_LAYOUT` mode, the current batch
is controlled by the `printing_batch_number` variable; this variable is ignored
in the `EXPLODED_VIEW` viewing mode.

The size of a batch is determined by the maximum printable volume, which is set
by the `max_print_bounds` variable near the top of the file.  The value of this
variable is currently set to the bounds for PLA printing supported by [Shapeways](https://shapeways.com).  
For those bounds, there are 3 batches.

To facilitate the placement of parts for the printable layout, the variable
`CHECKING_LAYOUT` may be set to `true` to show the X-Y profile of the printable
bounding box.

## Camera mounts

There are two different camera mounts supported, with and without servo motor
support.  The variable `use_servo_focus` controls which one of these is incorporated in the
design when the `show_camera_mount` variable is set to 1.

If `use_servo_focus == true` then the two gears that are used in conjunction with that
mount are also constructed.  A third party library, MCAD, is used for the
gear design, so that gear tooth shape is the involute form.  The pressure
angle was chosen to be 20 degrees but this may need to be changed.

## Selection of parts

Parts may be selected for construction in either viewing mode by setting the
switch variables at the top of the `FlyPi.scad` file.

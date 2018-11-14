# polarAxes2D
Inkscape extension to assist creating 2D polar axes


<img src="docs/images/Examples.png" width="900px"/>

### main features

The main features are

 - linear and log10 scales for R axis
 - optional grid lines in R and Theta directions
 - adjustable tick mark intervals and sizes
 - LaTeX support

# Installation and requirements

This extension was partially developed in Inkscape 0.48 and partially in 0.91 in Linux (Kubuntu 12.04 and 14.04). It should work on both versions of Inkscape. Also, they should work in different OSs too as long as all requirements are installed.

This extension requires another extension to run, inkscapeMadeEasy <https://github.com/fsmMLK/inkscapeMadeEasy>, which contains several backstage methods and classes.

In order to use polarAxes2D extension, you must also download inkscapeMadeEasy files and put them inside Inkscape's extension directory. Please refer to inkscapeMadeEasy installation instructions. In the end you must have the following files and directories in your Inkscape extension directory.

```
inkscape/extensions/
            |-- inkscapeMadeEasy_Base.py
            |-- inkscapeMadeEasy_Draw.py
            |-- inkscapeMadeEasy_Plot.py
            |-- textextLib
            |   |-- __init__.py
            |   |-- basicLatexPackages.tex
            |   |-- textext.inx
            |   |-- textext.py
            |
            |-- polarAxes2D.py
            `-- polarAxes2D.inx
```

**Disabling LaTeX support of inkscapeMadeEasy**

Many of the methods implemented in inkscapeMadeEasy project use LaTeX to generate text. To this end I decided to employ the excellent extension **textext** from Pauli Virtanen  <https://pav.iki.fi/software/textext/>. 

LaTeX support via textext extension requires LaTeX typesetting system in your computer (it's free and awesome! =] ), together with a few python modules (pygtk and Tkinter among others). The later might be a problem for non-Linux systems (precompiled inkscape for Windows as OS X don't come with them).

Since many people don't use LaTeX and/or don't have it installed, inkscapeMadeEasy's LaTeX support is now optional. **By default, LaTeX support is ENABLED.**

Please refer to <https://fsmmlk.github.io/inkscapeMadeEasy/#installation-and-requirements> on how to easily disable LaTeX support.

.. warning:: Since disabling LaTeX support is a new feature, this project was not yet extensively checked for misplacements/errors when this support is disabled. Please report any issues you find.

# Usage

The extension can be found under `extensions > fsmMLK > Plot 2D > Polar` menu.
'
This extension is presented in two tabs, **R axis** and  **Theta axis**. They are used to configure independently the axes of your chart. The tabs have most of the same control elements, with the exception of a few elements exclusive to R axis.

<img src="docs/images/Config_Raxis.png" width="700px"/>

<img src="docs/images/Config_Taxis.png" width="600px"/>


**R axis label (R axis only):** label of the R axis. This string must be LaTeX compatible. Any LaTeX commands or environments are valid. If you want to write in mathematical environment, enclose your text with $...$. You don't have to escape any backslashes.

> Tip: Since `siunitx` package is included in basicLatexPackages.tex file by default in inkscapeMadeEasy, you can use any unit command available there 

Ex: `Foobar $\sqrt{x^2}$ so fancy! (\si{\newton\per\squaremetre})`

<img src="docs/images/Legend_01.png" width="400px"/>

**R/Theta min and max:** Set the limits of the axes. The extension will inform if these limits are invalid.
  
  - The upper limit must be greater than the lower limit
  - If logarithmic scale is checked (R axis only), then the limits must be greater than 1.0
  - If logarithmic scale is checked (R axis only), then the lower limit will be rounded down to the nearest power of 10 and the upper rounded up to the nearest power of 10 in order to complete the decades. Ex: 1.2 to 12, then the limits will be rounded to 1 to 100
  - In theta direction, the values must be in degrees.

**Logarithmic scale (R axis only):** Set the axis to be represented in log10 scale. In such case, the limits of the axis must be both greater than one.

**Add grid to R/Theta axis:** Draw grid lines in R or Theta axes.
   - *linear scale:* The grid lines will be placed at each tick mark
   - *logarithmic scale:* The grid lines will be placed dividing each decade in 10 parts

**Add ticks to R/Theta axis:** Draw tick marks with associated values in R or Theta axes.

**R/Theta tick step:** Tick marks interval in units of your chart. This value is not referenced to  in logarithmic scale. In theta direction, the values must be in degrees.

Ex: limits from 0 to 2, with tick step of 0.5 will produce ticks at 0, 0.5, 1, 1.5, 2

> Note: The ticks will radiate from the origin R=0 or Theta=0 unless the origin does not lie within the limits. In such cases, the ticks will radiate  from the lower limit.
>
> Examples
>
> <img src="docs/images/TickStep.png" width="600px"/>


**R tick length (R axis only)** The distance between the tick marks, in px.
   - *linear scale:* The distance between ticks in px.
   - *logarithmic scale:* The size of each decade in px.

<img src="docs/images/TickLength.png" width="500px"/>

**R tick suffix value (R axis only):** Optional extra suffix to be added to the tick values. You can use any LaTeX text/commands valid in mathematical environment $...$. You don't have to enclose your text between $...$. You don't have to escape any backslashes.

<img src="docs/images/TickSuffix.png" width="500px"/>

**General aspect factor:** (present in R axis tab only) General aspect ratio between line width and text width. I designed this extension to have an overall aspect ratio that looked nice to my eyes. It is a function of R tick length. With this control you can scale both line widths and text height to fit your needs.

<img src="docs/images/generalAspectRatio.png" width="700px"/>

# Observations
 - The Radius must be positive
 - The limits of Theta are bounded between 0 and 360 degrees
 - Angle indication is in degrees.
 - The axes will be created at the center of your screen.

# Examples

<img src="docs/images/Examples.png" width="900px"/>

# To do

 - Add option to allow theta in radians.



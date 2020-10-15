#!/usr/bin/python

# --------------------------------------------------------------------------------------
#
#    polarAxes2D: - Inkscape extension to assist creating 2D polar axes
#
#    Copyright (C) 2016 by Fernando Moura
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------------------------

import inkex
import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw
import inkscapeMadeEasy_Plot as inkPlot
import math

#---------------------------------------------


class AxisCartesian(inkBase.inkscapeMadeEasy):

    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.OptionParser.add_option("--tab", action="store", type="string", dest="tab", default="object")

        self.OptionParser.add_option("--rMin", action="store", type="float", dest="rMin", default=0)
        self.OptionParser.add_option("--rMax", action="store", type="float", dest="rMax", default=5)
        self.OptionParser.add_option("--rLabel", action="store", type="string", dest="rLabel", default='')
        self.OptionParser.add_option("--rScale", action="store", type="float", dest="rScale", default=20)
        self.OptionParser.add_option("--rLog10scale", action="store", type="inkbool", dest="rLog10scale", default=False)
        self.OptionParser.add_option("--rTicks", action="store", type="inkbool", dest="rTicks", default=True)
        self.OptionParser.add_option("--rTickStep", action="store", type="float", dest="rTickStep", default=1)
        self.OptionParser.add_option("--rGrid", action="store", type="inkbool", dest="rGrid", default=True)
        self.OptionParser.add_option("--rExtraText", action="store", type="string", dest="rExtraText", default='')

        self.OptionParser.add_option("--tMin", action="store", type="float", dest="tMin", default=0)
        self.OptionParser.add_option("--tMax", action="store", type="float", dest="tMax", default=360)
        self.OptionParser.add_option("--tTicks", action="store", type="inkbool", dest="tTicks", default=False)
        self.OptionParser.add_option("--tTickStep", action="store", type="float", dest="tTickStep", default=45)
        self.OptionParser.add_option("--tGrid", action="store", type="inkbool", dest="tGrid", default=True)

        self.OptionParser.add_option("--generalAspectFactor", action="store", type="float", dest="generalAspectFactor", default=1.0)

    def effect(self):

        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.view_center[0], self.view_center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        #root_layer = self.current_layer
        root_layer = self.document.getroot()
        #root_layer = self.getcurrentLayer()

        Rlimits = [so.rMin, so.rMax]
        Tlimits = [so.tMin, so.tMax]

        #defines text height and line width
        textSize = so.generalAspectFactor * 0.25 * so.rScale
        lineWidthAxis = so.generalAspectFactor * so.rScale / 35.0

        inkPlot.axis.polar(self, root_layer, rLim=Rlimits, tLim=Tlimits, position=position, rLabel=so.rLabel,
                           rlog10scale=so.rLog10scale, rTicks=so.rTicks, tTicks=so.tTicks, rTickStep=so.rTickStep, tTickStep=so.tTickStep,
                           rScale=so.rScale, rAxisUnitFactor=so.rExtraText, rGrid=so.rGrid, tGrid=so.tGrid, forceTextSize=textSize, forceLineWidth=lineWidthAxis, drawAxis=True, ExtraLenghtAxisR=0.0)

if __name__ == '__main__':
    axis = AxisCartesian()
    axis.affect()

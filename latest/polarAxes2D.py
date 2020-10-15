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

import math

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Plot as inkPlot


# ---------------------------------------------


class AxisCartesian(inkBase.inkscapeMadeEasy):

    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="object")
        self.arg_parser.add_argument("--subtab_axis", type=str, dest="subtab_axis", default="object")

        self.arg_parser.add_argument("--rMin", type=float, dest="rMin", default=0)
        self.arg_parser.add_argument("--rMax", type=float, dest="rMax", default=5)
        self.arg_parser.add_argument("--rLabel", type=str, dest="rLabel", default='')
        self.arg_parser.add_argument("--rScale", type=float, dest="rScale", default=20)
        self.arg_parser.add_argument("--rLog10scale", type=self.bool, dest="rLog10scale", default=False)
        self.arg_parser.add_argument("--rTicks", type=self.bool, dest="rTicks", default=True)
        self.arg_parser.add_argument("--rTickStep", type=float, dest="rTickStep", default=1)
        self.arg_parser.add_argument("--rGrid", type=self.bool, dest="rGrid", default=True)
        self.arg_parser.add_argument("--rExtraText", type=str, dest="rExtraText", default='')

        self.arg_parser.add_argument("--tMin", type=float, dest="tMin", default=0)
        self.arg_parser.add_argument("--tMax", type=float, dest="tMax", default=360)
        self.arg_parser.add_argument("--tTicks", type=self.bool, dest="tTicks", default=False)
        self.arg_parser.add_argument("--tTickStep", type=float, dest="tTickStep", default=45)
        self.arg_parser.add_argument("--tGrid", type=self.bool, dest="tGrid", default=True)

        self.arg_parser.add_argument("--generalAspectFactor", type=float, dest="generalAspectFactor", default=1.0)

    def effect(self):
        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        # root_layer = self.current_layer
        root_layer = self.document.getroot()
        # root_layer = self.getcurrentLayer()

        Rlimits = [so.rMin, so.rMax]
        Tlimits = [so.tMin, so.tMax]

        # defines text height and line width
        textSize = so.generalAspectFactor * 0.25 * so.rScale
        lineWidthAxis = so.generalAspectFactor * so.rScale / 35.0

        inkPlot.axis.polar(self, root_layer, rLim=Rlimits, tLim=Tlimits, position=position, rLabel=so.rLabel, rlog10scale=so.rLog10scale,
                           rTicks=so.rTicks, tTicks=so.tTicks, rTickStep=so.rTickStep, tTickStep=so.tTickStep, rScale=so.rScale,
                           rAxisUnitFactor=so.rExtraText, rGrid=so.rGrid, tGrid=so.tGrid, forceTextSize=textSize, forceLineWidth=lineWidthAxis,
                           drawAxis=True, ExtraLengthAxisR=0.0)


if __name__ == '__main__':
    axis = AxisCartesian()
    axis.run()

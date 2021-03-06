from typing import Tuple, Set, Iterable, List

class GH_Distribute:
    None = 0
    Vertical = 1
    Horizontal = 2
class GH_Align:
    None = 0
    Left = 1
    Right = 2
    Top = 3
    Bottom = 4
    Vertical = 5
    Horizontal = 6
class GH_Solver:
    def __init__(self): ...
    def __init__(self, boxes : Iterable[RectangleF]): ...
    def AddBox (self, box : RectangleF) -> None: ...
    @property
    def Region (self) -> RectangleF: ...
    @Region.setter
    def Region (self, Value : RectangleF) -> None: ...
    def CreateAutoRegion (self) -> None: ...
    def Inflate (self, x : Single, y : Single) -> None: ...
    def Solve (self, align : GH_Align, distribute : GH_Distribute) -> List: ...
    def Align_Left (region : RectangleF, boxes : List) -> List: ...
    def Align_Right (region : RectangleF, boxes : List) -> List: ...
    def Align_Vertical (region : RectangleF, boxes : List) -> List: ...
    def Align_Top (region : RectangleF, boxes : List) -> List: ...
    def Align_Bottom (region : RectangleF, boxes : List) -> List: ...
    def Align_Horizontal (region : RectangleF, boxes : List) -> List: ...
    def Distribute_Vertical (region : RectangleF, boxes : List) -> List: ...
    def Distribute_Horizontal (region : RectangleF, boxes : List) -> List: ...

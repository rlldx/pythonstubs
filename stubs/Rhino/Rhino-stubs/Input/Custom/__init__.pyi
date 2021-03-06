from typing import Tuple, Set, Iterable, List

class GetArc:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    @property
    def AllowDeformable (self) -> bool: ...
    @AllowDeformable.setter
    def AllowDeformable (self, value : bool) -> None: ...
    @property
    def Deformable (self) -> bool: ...
    @Deformable.setter
    def Deformable (self, value : bool) -> None: ...
    @property
    def DeformablePointCount (self) -> int: ...
    @DeformablePointCount.setter
    def DeformablePointCount (self, value : int) -> None: ...
    @property
    def DeformableDegree (self) -> int: ...
    @DeformableDegree.setter
    def DeformableDegree (self, value : int) -> None: ...
    @property
    def DefaultRadius (self) -> float: ...
    @DefaultRadius.setter
    def DefaultRadius (self, value : float) -> None: ...
    def Get (self) -> Tuple[Result, Arc]: ...
class GetCircle:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    @property
    def AllowDeformable (self) -> bool: ...
    @AllowDeformable.setter
    def AllowDeformable (self, value : bool) -> None: ...
    @property
    def Deformable (self) -> bool: ...
    @Deformable.setter
    def Deformable (self, value : bool) -> None: ...
    @property
    def DeformablePointCount (self) -> int: ...
    @DeformablePointCount.setter
    def DeformablePointCount (self, value : int) -> None: ...
    @property
    def DeformableDegree (self) -> int: ...
    @DeformableDegree.setter
    def DeformableDegree (self, value : int) -> None: ...
    @property
    def DefaultSize (self) -> float: ...
    @DefaultSize.setter
    def DefaultSize (self, value : float) -> None: ...
    @property
    def InDiameterMode (self) -> bool: ...
    @InDiameterMode.setter
    def InDiameterMode (self, value : bool) -> None: ...
    def Get (self) -> Tuple[Result, Circle]: ...
class ConeConstraint:
    None = 0
    Vertical = 1
    AroundCurve = 2
class GetCone:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    @property
    def ConeConstraint (self) -> ConeConstraint: ...
    @ConeConstraint.setter
    def ConeConstraint (self, value : ConeConstraint) -> None: ...
    @property
    def DefaultSize (self) -> float: ...
    @DefaultSize.setter
    def DefaultSize (self, value : float) -> None: ...
    @property
    def InDiameterMode (self) -> bool: ...
    @InDiameterMode.setter
    def InDiameterMode (self, value : bool) -> None: ...
    @property
    def ApexAngleDegrees (self) -> float: ...
    @ApexAngleDegrees.setter
    def ApexAngleDegrees (self, value : float) -> None: ...
    @property
    def BaseAngleDegrees (self) -> float: ...
    @BaseAngleDegrees.setter
    def BaseAngleDegrees (self, value : float) -> None: ...
    @property
    def Height (self) -> float: ...
    @Height.setter
    def Height (self, value : float) -> None: ...
    @property
    def Cap (self) -> bool: ...
    @Cap.setter
    def Cap (self, value : bool) -> None: ...
    @property
    def AllowInputAngle (self) -> bool: ...
    @AllowInputAngle.setter
    def AllowInputAngle (self, value : bool) -> None: ...
    def Get (self) -> Tuple[Result, Cone]: ...
class CylinderConstraint:
    None = 0
    Vertical = 1
    AroundCurve = 2
class GetCylinder:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    @property
    def CylinderConstraint (self) -> CylinderConstraint: ...
    @CylinderConstraint.setter
    def CylinderConstraint (self, value : CylinderConstraint) -> None: ...
    @property
    def DefaultSize (self) -> float: ...
    @DefaultSize.setter
    def DefaultSize (self, value : float) -> None: ...
    @property
    def InDiameterMode (self) -> bool: ...
    @InDiameterMode.setter
    def InDiameterMode (self, value : bool) -> None: ...
    @property
    def BothSidesOption (self) -> bool: ...
    @BothSidesOption.setter
    def BothSidesOption (self, value : bool) -> None: ...
    @property
    def Height (self) -> float: ...
    @Height.setter
    def Height (self, value : float) -> None: ...
    @property
    def Cap (self) -> bool: ...
    @Cap.setter
    def Cap (self, value : bool) -> None: ...
    def Get (self) -> Tuple[Result, Cylinder]: ...
class GetLineMode:
    TwoPoint = 0
    SurfaceNormal = 1
    Angled = 2
    Vertical = 3
    FourPoint = 4
    Bisector = 5
    Perpendicular = 6
    Tangent = 7
    CurveEnd = 8
    CPlaneNormalVector = 9
class GetLine:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    def Get (self) -> Tuple[Result, Line]: ...
    @property
    def FirstPointPrompt (self) -> str: ...
    @FirstPointPrompt.setter
    def FirstPointPrompt (self, value : str) -> None: ...
    @property
    def MidPointPrompt (self) -> str: ...
    @MidPointPrompt.setter
    def MidPointPrompt (self, value : str) -> None: ...
    @property
    def SecondPointPrompt (self) -> str: ...
    @SecondPointPrompt.setter
    def SecondPointPrompt (self, value : str) -> None: ...
    @property
    def AcceptZeroLengthLine (self) -> bool: ...
    @AcceptZeroLengthLine.setter
    def AcceptZeroLengthLine (self, value : bool) -> None: ...
    @property
    def HaveFeedbackColor (self) -> bool: ...
    @property
    def FeedbackColor (self) -> Color: ...
    @FeedbackColor.setter
    def FeedbackColor (self, value : Color) -> None: ...
    @property
    def FixedLength (self) -> float: ...
    @FixedLength.setter
    def FixedLength (self, value : float) -> None: ...
    def EnableFromBothSidesOption (self, on : bool) -> None: ...
    def EnableFromMidPointOption (self, on : bool) -> None: ...
    def EnableAllVariations (self, on : bool) -> None: ...
    def SetFirstPoint (self, point : Point3d) -> None: ...
    @property
    def GetLineMode (self) -> GetLineMode: ...
    @GetLineMode.setter
    def GetLineMode (self, value : GetLineMode) -> None: ...
class GetPolyline:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    def Get (self) -> Tuple[Result, Polyline]: ...
    @property
    def FirstPointPrompt (self) -> str: ...
    @FirstPointPrompt.setter
    def FirstPointPrompt (self, value : str) -> None: ...
    @property
    def SecondPointPrompt (self) -> str: ...
    @SecondPointPrompt.setter
    def SecondPointPrompt (self, value : str) -> None: ...
    @property
    def ThirdPointPrompt (self) -> str: ...
    @ThirdPointPrompt.setter
    def ThirdPointPrompt (self, value : str) -> None: ...
    @property
    def FourthPointPrompt (self) -> str: ...
    @FourthPointPrompt.setter
    def FourthPointPrompt (self, value : str) -> None: ...
    @property
    def MinPointCount (self) -> int: ...
    @MinPointCount.setter
    def MinPointCount (self, value : int) -> None: ...
    @property
    def MaxPointCount (self) -> int: ...
    @MaxPointCount.setter
    def MaxPointCount (self, value : int) -> None: ...
    def SetFirstPoint (self, point : Point3d) -> None: ...
class GetTransform(GetPoint):
    def AddTransformObjects (self, list : TransformObjectList) -> None: ...
    def CalculateTransform (self, viewport : RhinoViewport, point : Point3d) -> Transform: ...
    @property
    def HaveTransform (self) -> bool: ...
    @HaveTransform.setter
    def HaveTransform (self, value : bool) -> None: ...
    @property
    def Transform (self) -> Transform: ...
    @Transform.setter
    def Transform (self, value : Transform) -> None: ...
    @property
    def ObjectList (self) -> TransformObjectList: ...
    def GetXform (self) -> GetResult: ...
class PickStyle:
    None = 0
    PointPick = 1
    WindowPick = 2
    CrossingPick = 3
class PickMode:
    Wireframe = 1
    Shaded = 2
class PickContext:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    @property
    def View (self) -> RhinoView: ...
    @View.setter
    def View (self, value : RhinoView) -> None: ...
    @property
    def PickLine (self) -> Line: ...
    @PickLine.setter
    def PickLine (self, value : Line) -> None: ...
    @property
    def PickStyle (self) -> PickStyle: ...
    @PickStyle.setter
    def PickStyle (self, value : PickStyle) -> None: ...
    @property
    def PickMode (self) -> PickMode: ...
    @PickMode.setter
    def PickMode (self, value : PickMode) -> None: ...
    @property
    def PickGroupsEnabled (self) -> bool: ...
    @PickGroupsEnabled.setter
    def PickGroupsEnabled (self, value : bool) -> None: ...
    @property
    def SubObjectSelectionEnabled (self) -> bool: ...
    @SubObjectSelectionEnabled.setter
    def SubObjectSelectionEnabled (self, value : bool) -> None: ...
    @property
    def GetObjectUsed (self) -> GetObject: ...
    def SetPickTransform (self, transform : Transform) -> None: ...
    def UpdateClippingPlanes (self) -> None: ...
    def PickFrustumTest (self, box : BoundingBox) -> Tuple[bool, bool]: ...
    def PickFrustumTest (self, point : Point3d) -> Tuple[bool, float, float]: ...
    def PickFrustumTest (self, points : Set(Point3d)) -> Tuple[bool, int, float, float]: ...
    def PickFrustumTest (self, cloud : PointCloud) -> Tuple[bool, int, float, float]: ...
    def PickFrustumTest (self, line : Line) -> Tuple[bool, float, float, float]: ...
    def PickFrustumTest (self, bezier : BezierCurve) -> Tuple[bool, float, float, float]: ...
    def PickFrustumTest (self, curve : NurbsCurve) -> Tuple[bool, float, float, float]: ...
    def PickFrustumTest (self, mesh : Mesh, pickStyle : MeshPickStyle) -> Tuple[bool, Point3d, Point2d, Point2d, float, float, MeshHitFlag, int]: ...
    def PickFrustumTest (self, mesh : Mesh, pickStyle : MeshPickStyle) -> Tuple[bool, Point3d, float, float, MeshHitFlag, int]: ...
    def PickMeshTopologyVertices (self, mesh : Mesh) -> Set(int): ...
class GetFileNameMode:
    Open = 0
    OpenTemplate = 1
    OpenImage = 2
    OpenRhinoOnly = 3
    OpenTextFile = 5
    OpenWorksession = 6
    Import = 7
    Attach = 8
    LoadPlugIn = 9
    Save = 10
    SaveSmall = 11
    SaveTemplate = 12
    SaveImage = 13
    Export = 14
    SaveTextFile = 17
    SaveWorksession = 18
class GetString(GetBaseClass):
    def __init__(self): ...
    def Get (self) -> GetResult: ...
    def GetLiteralString (self) -> GetResult: ...
class GetOption(GetBaseClass):
    def __init__(self): ...
    def Get (self) -> GetResult: ...
class GetNumber(GetBaseClass):
    def __init__(self): ...
    def Get (self) -> GetResult: ...
    def SetLowerLimit (self, lowerLimit : float, strictlyGreaterThan : bool) -> None: ...
    def SetUpperLimit (self, upperLimit : float, strictlyLessThan : bool) -> None: ...
class GetInteger(GetBaseClass):
    def __init__(self): ...
    def Get (self) -> GetResult: ...
    def Number (self) -> int: ...
    def SetLowerLimit (self, lowerLimit : int, strictlyGreaterThan : bool) -> None: ...
    def SetUpperLimit (self, upperLimit : int, strictlyLessThan : bool) -> None: ...
class GetObjectGeometryFilter:
    def __init__(self, object : Object, method : IntPtr): ...
    def Invoke (self, rhObject : RhinoObject, geometry : GeometryBase, componentIndex : ComponentIndex) -> bool: ...
    def BeginInvoke (self, rhObject : RhinoObject, geometry : GeometryBase, componentIndex : ComponentIndex, callback : AsyncCallback, object : Object) -> IAsyncResult: ...
    def EndInvoke (self, result : IAsyncResult) -> bool: ...
class GetObject(GetBaseClass):
    def __init__(self): ...
    def ActiveGetObject (doc : RhinoDoc) -> GetObject: ...
    @property
    def GeometryFilter (self) -> ObjectType: ...
    @GeometryFilter.setter
    def GeometryFilter (self, value : ObjectType) -> None: ...
    @property
    def GeometryAttributeFilter (self) -> GeometryAttributeFilter: ...
    @GeometryAttributeFilter.setter
    def GeometryAttributeFilter (self, value : GeometryAttributeFilter) -> None: ...
    def CustomGeometryFilter (self, rhObject : RhinoObject, geometry : GeometryBase, componentIndex : ComponentIndex) -> bool: ...
    def SetCustomGeometryFilter (self, filter : GetObjectGeometryFilter) -> None: ...
    def PassesGeometryAttributeFilter (self, rhObject : RhinoObject, geometry : GeometryBase, componentIndex : ComponentIndex) -> bool: ...
    def EnablePreSelect (self, enable : bool, ignoreUnacceptablePreselectedObjects : bool) -> None: ...
    def DisablePreSelect (self) -> None: ...
    def EnablePostSelect (self, enable : bool) -> None: ...
    @property
    def DeselectAllBeforePostSelect (self) -> bool: ...
    @DeselectAllBeforePostSelect.setter
    def DeselectAllBeforePostSelect (self, value : bool) -> None: ...
    @property
    def OneByOnePostSelect (self) -> bool: ...
    @OneByOnePostSelect.setter
    def OneByOnePostSelect (self, value : bool) -> None: ...
    @property
    def SubObjectSelect (self) -> bool: ...
    @SubObjectSelect.setter
    def SubObjectSelect (self, value : bool) -> None: ...
    @property
    def ChooseOneQuestion (self) -> bool: ...
    @ChooseOneQuestion.setter
    def ChooseOneQuestion (self, value : bool) -> None: ...
    @property
    def BottomObjectPreference (self) -> bool: ...
    @BottomObjectPreference.setter
    def BottomObjectPreference (self, value : bool) -> None: ...
    @property
    def GroupSelect (self) -> bool: ...
    @GroupSelect.setter
    def GroupSelect (self, value : bool) -> None: ...
    @property
    def InactiveDetailPickEnabled (self) -> bool: ...
    @InactiveDetailPickEnabled.setter
    def InactiveDetailPickEnabled (self, value : bool) -> None: ...
    def EnableSelPrevious (self, enable : bool) -> None: ...
    def EnableHighlight (self, enable : bool) -> None: ...
    @property
    def ReferenceObjectSelect (self) -> bool: ...
    @ReferenceObjectSelect.setter
    def ReferenceObjectSelect (self, value : bool) -> None: ...
    def EnableIgnoreGrips (self, enable : bool) -> None: ...
    def EnablePressEnterWhenDonePrompt (self, enable : bool) -> None: ...
    def SetPressEnterWhenDonePrompt (self, prompt : str) -> None: ...
    @property
    def AlreadySelectedObjectSelect (self) -> bool: ...
    @AlreadySelectedObjectSelect.setter
    def AlreadySelectedObjectSelect (self, value : bool) -> None: ...
    def Get (self) -> GetResult: ...
    def GetMultiple (self, minimumNumber : int, maximumNumber : int) -> GetResult: ...
    @property
    def ObjectCount (self) -> int: ...
    def Object (self, index : int) -> ObjRef: ...
    def Objects (self) -> Set(ObjRef): ...
    @property
    def ObjectsWerePreselected (self) -> bool: ...
    @property
    def SerialNumber (self) -> UInt32: ...
    def EnableClearObjectsOnEntry (self, enable : bool) -> None: ...
    def EnableUnselectObjectsOnExit (self, enable : bool) -> None: ...
    def AppendToPickList (self, objref : ObjRef) -> None: ...
    def ClearObjects (self) -> None: ...
class GeometryAttributeFilter:
    WireCurve = 1
    EdgeCurve = 2
    ClosedCurve = 4
    OpenCurve = 8
    SeamEdge = 16
    ManifoldEdge = 32
    NonmanifoldEdge = 64
    MatedEdge = 112
    SurfaceBoundaryEdge = 128
    TrimmingBoundaryEdge = 256
    BoundaryEdge = 384
    ClosedSurface = 512
    OpenSurface = 1024
    TrimmedSurface = 2048
    UntrimmedSurface = 4096
    SubSurface = 8192
    TopSurface = 16384
    ManifoldPolysrf = 32768
    NonmanifoldPolysrf = 65536
    ClosedPolysrf = 131072
    OpenPolysrf = 262144
    ClosedMesh = 524288
    OpenMesh = 1048576
    BoundaryInnerLoop = 2097152
    MatedInnerLoop = 4194304
    InnerLoop = 6291456
    BoundaryOuterLoop = 8388608
    MatedOuterLoop = 16777216
    OuterLoop = 25165824
    SpecialLoop = 33554432
    AcceptAllAttributes = 4294967295
class GetPoint(GetBaseClass):
    def __init__(self): ...
    def SetBasePoint (self, basePoint : Point3d, showDistanceInStatusBar : bool) -> None: ...
    def TryGetBasePoint (self) -> Tuple[bool, Point3d]: ...
    def GetPlanarConstraint (self, vp : RhinoViewport) -> Tuple[bool, RhinoViewport, Plane]: ...
    def ConstrainDistanceFromBasePoint (self, distance : float) -> None: ...
    @property
    def DynamicDrawColor (self) -> Color: ...
    @DynamicDrawColor.setter
    def DynamicDrawColor (self, value : Color) -> None: ...
    def SetCursor (self, cursor : CursorStyle) -> None: ...
    def EnableObjectSnapCursors (self, enable : bool) -> None: ...
    def DrawLineFromPoint (self, startPoint : Point3d, showDistanceInStatusBar : bool) -> None: ...
    def EnableDrawLineFromPoint (self, enable : bool) -> None: ...
    def EnableNoRedrawOnExit (self, noRedraw : bool) -> None: ...
    def PermitOrthoSnap (self, permit : bool) -> None: ...
    def PermitFromOption (self, permit : bool) -> None: ...
    def PermitConstraintOptions (self, permit : bool) -> None: ...
    def PermitTabMode (self, permit : bool) -> None: ...
    def PermitElevatorMode (self, permitMode : int) -> None: ...
    def PermitObjectSnap (self, permit : bool) -> None: ...
    def AddSnapPoint (self, point : Point3d) -> int: ...
    def AddSnapPoints (self, points : Set(Point3d)) -> int: ...
    def AddConstructionPoint (self, point : Point3d) -> int: ...
    def AddConstructionPoints (self, points : Set(Point3d)) -> int: ...
    def ClearSnapPoints (self) -> None: ...
    def ClearConstructionPoints (self) -> None: ...
    def GetSnapPoints (self) -> Set(Point3d): ...
    def GetConstructionPoints (self) -> Set(Point3d): ...
    def EnableCurveSnapTangentBar (self, drawTangentBarAtSnapPoint : bool, drawEndPoints : bool) -> None: ...
    def EnableCurveSnapPerpBar (self, drawPerpBarAtSnapPoint : bool, drawEndPoints : bool) -> None: ...
    def EnableCurveSnapArrow (self, drawDirectionArrowAtSnapPoint : bool, reverseArrow : bool) -> None: ...
    def EnableSnapToCurves (self, enable : bool) -> None: ...
    def Constrain (self, from_ : Point3d, to : Point3d) -> bool: ...
    def Constrain (self, line : Line) -> bool: ...
    def Constrain (self, arc : Arc) -> bool: ...
    def Constrain (self, circle : Circle) -> bool: ...
    def Constrain (self, plane : Plane, allowElevator : bool) -> bool: ...
    def Constrain (self, sphere : Sphere) -> bool: ...
    def Constrain (self, cylinder : Cylinder) -> bool: ...
    def Constrain (self, curve : Curve, allowPickingPointOffObject : bool) -> bool: ...
    def Constrain (self, surface : Surface, allowPickingPointOffObject : bool) -> bool: ...
    def Constrain (self, brep : Brep, wireDensity : int, faceIndex : int, allowPickingPointOffObject : bool) -> bool: ...
    def Constrain (self, mesh : Mesh, allowPickingPointOffObject : bool) -> bool: ...
    def ConstrainToConstructionPlane (self, throughBasePoint : bool) -> bool: ...
    def ConstrainToTargetPlane (self) -> None: ...
    def ConstrainToVirtualCPlaneIntersection (self, plane : Plane) -> bool: ...
    def ClearConstraints (self) -> None: ...
    def InterruptMouseMove (self) -> bool: ...
    def add_MouseMove (self, value : EventHandler) -> None: ...
    def remove_MouseMove (self, value : EventHandler) -> None: ...
    @property
    def Tag (self) -> Object: ...
    @Tag.setter
    def Tag (self, value : Object) -> None: ...
    def add_MouseDown (self, value : EventHandler) -> None: ...
    def remove_MouseDown (self, value : EventHandler) -> None: ...
    def add_DynamicDraw (self, value : EventHandler) -> None: ...
    def remove_DynamicDraw (self, value : EventHandler) -> None: ...
    @property
    def FullFrameRedrawDuringGet (self) -> bool: ...
    @FullFrameRedrawDuringGet.setter
    def FullFrameRedrawDuringGet (self, value : bool) -> None: ...
    def add_PostDrawObjects (self, value : EventHandler) -> None: ...
    def remove_PostDrawObjects (self, value : EventHandler) -> None: ...
    def Get (self, onMouseUp : bool) -> GetResult: ...
    def Get (self, onMouseUp : bool, get2DPoint : bool) -> GetResult: ...
    def Get (self) -> GetResult: ...
    def PointOnObject (self) -> ObjRef: ...
    def PointOnCurve (self) -> Tuple[Curve, float]: ...
    def PointOnSurface (self) -> Tuple[Surface, float, float]: ...
    def PointOnBrep (self) -> Tuple[BrepFace, float, float]: ...
class GetPointDrawEventArgs(DrawEventArgs):
    @property
    def CurrentPoint (self) -> Point3d: ...
    @property
    def Source (self) -> GetPoint: ...
class GetPointMouseEventArgs:
    @property
    def Source (self) -> GetPoint: ...
    @property
    def Viewport (self) -> RhinoViewport: ...
    @property
    def Point (self) -> Point3d: ...
    @property
    def WindowPoint (self) -> Point: ...
    @property
    def LeftButtonDown (self) -> bool: ...
    @property
    def RightButtonDown (self) -> bool: ...
    @property
    def ShiftKeyDown (self) -> bool: ...
    @property
    def ControlKeyDown (self) -> bool: ...
    @property
    def MiddleButtonDown (self) -> bool: ...
class GetBaseClass:
    def Dispose (self) -> None: ...
    def SetCommandPrompt (self, prompt : str) -> None: ...
    def SetCommandPromptDefault (self, defaultValue : str) -> None: ...
    def SetDefaultPoint (self, point : Point3d) -> None: ...
    def SetDefaultNumber (self, defaultNumber : float) -> None: ...
    def SetDefaultInteger (self, defaultValue : int) -> None: ...
    def SetDefaultString (self, defaultValue : str) -> None: ...
    def SetDefaultColor (self, defaultColor : Color) -> None: ...
    def SetWaitDuration (self, milliseconds : int) -> None: ...
    def ClearDefault (self) -> None: ...
    def GotDefault (self) -> bool: ...
    def AddOption (self, englishOption : str) -> int: ...
    def AddOption (self, englishOption : str, englishOptionValue : str) -> int: ...
    def AddOption (self, englishOption : str, englishOptionValue : str, hiddenOption : bool) -> int: ...
    def AddOption (self, optionName : LocalizeStringPair) -> int: ...
    def AddOption (self, optionName : LocalizeStringPair, optionValue : LocalizeStringPair) -> int: ...
    def AddOption (self, optionName : LocalizeStringPair, optionValue : LocalizeStringPair, hiddenOption : bool) -> int: ...
    def AddOptionDouble (self, englishName : str, numberValue : OptionDouble, prompt : str) -> Tuple[int, OptionDouble]: ...
    def AddOptionDouble (self, optionName : LocalizeStringPair, numberValue : OptionDouble, prompt : str) -> Tuple[int, OptionDouble]: ...
    def AddOptionDouble (self, englishName : str, numberValue : OptionDouble) -> Tuple[int, OptionDouble]: ...
    def AddOptionDouble (self, optionName : LocalizeStringPair, numberValue : OptionDouble) -> Tuple[int, OptionDouble]: ...
    def AddOptionInteger (self, englishName : str, intValue : OptionInteger, prompt : str) -> Tuple[int, OptionInteger]: ...
    def AddOptionInteger (self, optionName : LocalizeStringPair, intValue : OptionInteger, prompt : str) -> Tuple[int, OptionInteger]: ...
    def AddOptionInteger (self, englishName : str, intValue : OptionInteger) -> Tuple[int, OptionInteger]: ...
    def AddOptionInteger (self, optionName : LocalizeStringPair, intValue : OptionInteger) -> Tuple[int, OptionInteger]: ...
    def AddOptionColor (self, optionName : LocalizeStringPair, colorValue : OptionColor, prompt : str) -> Tuple[int, OptionColor]: ...
    def AddOptionColor (self, optionName : LocalizeStringPair, colorValue : OptionColor) -> Tuple[int, OptionColor]: ...
    def AddOptionColor (self, englishName : str, colorValue : OptionColor, prompt : str) -> Tuple[int, OptionColor]: ...
    def AddOptionColor (self, englishName : str, colorValue : OptionColor) -> Tuple[int, OptionColor]: ...
    def AddOptionToggle (self, englishName : str, toggleValue : OptionToggle) -> Tuple[int, OptionToggle]: ...
    def AddOptionToggle (self, optionName : LocalizeStringPair, toggleValue : OptionToggle) -> Tuple[int, OptionToggle]: ...
    def AddOptionList (self, englishOptionName : str, listValues : Iterable[str], listCurrentIndex : int) -> int: ...
    def AddOptionList (self, optionName : LocalizeStringPair, listValues : Iterable[LocalizeStringPair], listCurrentIndex : int) -> int: ...
    def AddOptionEnumList (self, englishOptionName : str, defaultValue : T) -> int: ...
    def AddOptionEnumList (self, englishOptionName : str, defaultValue : T, include : Set(T)) -> int: ...
    def AddOptionEnumSelectionList (self, englishOptionName : str, enumSelection : Iterable[T], listCurrentIndex : int) -> int: ...
    def GetSelectedEnumValue (self) -> T: ...
    def GetSelectedEnumValueFromSelectionList (self, selectionList : Iterable[T]) -> T: ...
    def ClearCommandOptions (self) -> None: ...
    def EnableTransparentCommands (self, enable : bool) -> None: ...
    def AcceptNothing (self, enable : bool) -> None: ...
    def AcceptUndo (self, enable : bool) -> None: ...
    def AcceptEnterWhenDone (self, enable : bool) -> None: ...
    def AcceptNumber (self, enable : bool, acceptZero : bool) -> None: ...
    def AcceptPoint (self, enable : bool) -> None: ...
    def AcceptColor (self, enable : bool) -> None: ...
    def AcceptString (self, enable : bool) -> None: ...
    def AcceptCustomMessage (self, enable : bool) -> None: ...
    def PostCustomMessage (messageData : Object) -> None: ...
    def CustomMessage (self) -> Object: ...
    def Result (self) -> GetResult: ...
    def CommandResult (self) -> Result: ...
    def Option (self) -> CommandLineOption: ...
    def OptionIndex (self) -> int: ...
    def Number (self) -> float: ...
    def StringResult (self) -> str: ...
    def Point (self) -> Point3d: ...
    def Vector (self) -> Vector3d: ...
    def Color (self) -> Color: ...
    def View (self) -> RhinoView: ...
    def PickRectangle (self) -> Rectangle: ...
    def Point2d (self) -> Point: ...
    def Rectangle2d (self) -> Rectangle: ...
    def Line2d (self) -> Set(Point): ...
class CommandLineOption:
    def IsValidOptionName (optionName : str) -> bool: ...
    def IsValidOptionValueName (optionValue : str) -> bool: ...
    @property
    def Index (self) -> int: ...
    @property
    def CurrentListOptionIndex (self) -> int: ...
    @property
    def EnglishName (self) -> str: ...
class OptionToggle:
    def __init__(self, initialValue : bool, offValue : str, onValue : str): ...
    def __init__(self, initialValue : bool, offValue : LocalizeStringPair, onValue : LocalizeStringPair): ...
    def Dispose (self) -> None: ...
    @property
    def CurrentValue (self) -> bool: ...
    @CurrentValue.setter
    def CurrentValue (self, value : bool) -> None: ...
    @property
    def InitialValue (self) -> bool: ...
class OptionDouble:
    def __init__(self, initialValue : float): ...
    def __init__(self, initialValue : float, lowerLimit : float, upperLimit : float): ...
    def __init__(self, initialValue : float, setLowerLimit : bool, limit : float): ...
    def Dispose (self) -> None: ...
    @property
    def CurrentValue (self) -> float: ...
    @CurrentValue.setter
    def CurrentValue (self, value : float) -> None: ...
    @property
    def InitialValue (self) -> float: ...
class OptionInteger:
    def __init__(self, initialValue : int): ...
    def __init__(self, initialValue : int, lowerLimit : int, upperLimit : int): ...
    def __init__(self, initialValue : int, setLowerLimit : bool, limit : int): ...
    def Dispose (self) -> None: ...
    @property
    def CurrentValue (self) -> int: ...
    @CurrentValue.setter
    def CurrentValue (self, value : int) -> None: ...
    @property
    def InitialValue (self) -> int: ...
class OptionColor:
    def __init__(self, initialValue : Color): ...
    def Dispose (self) -> None: ...
    @property
    def CurrentValue (self) -> Color: ...
    @CurrentValue.setter
    def CurrentValue (self, value : Color) -> None: ...
    @property
    def InitialValue (self) -> Color: ...
class TaskCompleteEventArgs:
    def __init__(self, task : Task, doc : RhinoDoc): ...
    @property
    def Task (self) -> Task: ...
    @Task.setter
    def Task (self, value : Task) -> None: ...
    @property
    def Doc (self) -> RhinoDoc: ...
    @Doc.setter
    def Doc (self, value : RhinoDoc) -> None: ...
    @property
    def Redraw (self) -> bool: ...
    @Redraw.setter
    def Redraw (self, value : bool) -> None: ...
class GetCancel(GetBaseClass):
    def __init__(self): ...
    @property
    def Token (self) -> CancellationToken: ...
    def add_TaskCompleted (self, value : EventHandler) -> None: ...
    def remove_TaskCompleted (self, value : EventHandler) -> None: ...
    @property
    def ProgressReporting (self) -> bool: ...
    @ProgressReporting.setter
    def ProgressReporting (self, value : bool) -> None: ...
    @property
    def ProgressMessage (self) -> str: ...
    @ProgressMessage.setter
    def ProgressMessage (self, value : str) -> None: ...
    def Wait (self, task : Task, doc : RhinoDoc) -> Result: ...
    def WaitAll (self, tasks : Iterable[Task], doc : RhinoDoc) -> Result: ...
    @property
    def Progress (self) -> IProgress: ...
class MeshPickStyle:
    WireframePicking = 0
    ShadedModePicking = 1
    VertexOnlyPicking = 2
class MeshHitFlag:
    Vertex = 0
    Edge = 1
    Face = 2
    Invalid = -1

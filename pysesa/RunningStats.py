# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_RunningStats', [dirname(__file__)])
        except ImportError:
            import _RunningStats
            return _RunningStats
        if fp is not None:
            try:
                _mod = imp.load_module('_RunningStats', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _RunningStats = swig_import_helper()
    del swig_import_helper
else:
    import _RunningStats
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class RunningStats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RunningStats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RunningStats, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _RunningStats.new_RunningStats()
        try: self.this.append(this)
        except: self.this = this
    def Clear(self): return _RunningStats.RunningStats_Clear(self)
    def Push(self, *args): return _RunningStats.RunningStats_Push(self, *args)
    def NumDataValues(self): return _RunningStats.RunningStats_NumDataValues(self)
    def Mean(self): return _RunningStats.RunningStats_Mean(self)
    def Variance(self): return _RunningStats.RunningStats_Variance(self)
    def StandardDeviation(self): return _RunningStats.RunningStats_StandardDeviation(self)
    def Skewness(self): return _RunningStats.RunningStats_Skewness(self)
    def Kurtosis(self): return _RunningStats.RunningStats_Kurtosis(self)
    def __iadd__(self, *args): return _RunningStats.RunningStats___iadd__(self, *args)
    __swig_destroy__ = _RunningStats.delete_RunningStats
    __del__ = lambda self : None;
RunningStats_swigregister = _RunningStats.RunningStats_swigregister
RunningStats_swigregister(RunningStats)

# This file is compatible with both classic and new-style classes.



from . import instructions
from . import formatters
from .InputContainer import InputContainer
from .InstructionSet import InstructionSet
from .InstructionList import InstructionList
from .ScriptParser import ScriptParser
from .ScriptRunner import ScriptRunner
from .Collector import Collector

def ilist_factory():
    return InstructionList()

def load_default_instruction_set(iset):
    iset.add("searchpast", instructions.SearchPastInstruction)
    iset.add("searchuptill", instructions.SearchUpTillInstruction)
    iset.add("copytillwith", instructions.CopyTillWithInstruction)
    iset.add("copyuptill", instructions.CopyUpTillInstruction)
    iset.add("if", instructions.IfInstruction)
    iset.add("elseif", instructions.ElseIfInstruction)
    iset.add("else", instructions.ElseInstruction)
    iset.add("endif", instructions.EndIfInstruction)
    iset.add("repeat", instructions.RepeatInstruction)
    return iset

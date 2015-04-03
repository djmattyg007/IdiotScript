#!/usr/bin/python3

import os, sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Invalid number of arguments.")
    sys.exit()

if os.path.isfile(sys.argv[1]) == False:
    print("IdiotScript program does not exist.")
    sys.exit()


import io
import idiotscript
from idiotscript import InstructionSet, Collector, ScriptParser, ScriptRunner, InputContainer
from idiotscript import formatters

def get_input():
    if len(sys.argv) == 3:
        # We've been passed a filename for the input content
        with open(sys.argv[2], "r", encoding = "utf-8") as input_file:
            return input_file.read()
    else:
        # Assume we're receiving data from stdin
        from io import StringIO
        try:
            stdin_file = sys.stdin.buffer.read()
        except AttributeError:
            stdin_file = sys.stdin.read()
        io_obj = StringIO(stdin_file.decode("utf-8"))
        return io_obj.read()

# Prepare the default instruction set.
my_iset = idiotscript.load_default_instruction_set(InstructionSet())
# Initialise the script parser with the default instruction set.
# We need to pass it an instruction list factory, as it's going to
# be creating lots of them.
parser = ScriptParser(my_iset, idiotscript.ilist_factory)

# Load the IdiotScript program into memory
with open(sys.argv[1]) as program_file:
    program = program_file.read()

my_ilist = parser.parse(program)
inputtext = get_input()

my_collector = Collector()
runner = ScriptRunner(InputContainer(inputtext))
runner.run(my_ilist, my_collector)

nl_formatter = formatters.NewlineFormatter()
print(nl_formatter.format(my_collector))


import re

PREDEFINED = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

for i in range(16):
    PREDEFINED["R" + str(i)] = i

COMP = {
    "0":"0101010", "1":"0111111", "-1":"0111010",
    "D":"0001100", "A":"0110000", "M":"1110000",
    "!D":"0001101", "!A":"0110001", "!M":"1110001",
    "-D":"0001111", "-A":"0110011", "-M":"1110011",
    "D+1":"0011111", "A+1":"0110111", "M+1":"1110111",
    "D-1":"0001110", "A-1":"0110010", "M-1":"1110010",
    "D+A":"0000010", "D+M":"1000010",
    "D-A":"0010011", "D-M":"1010011",
    "A-D":"0000111", "M-D":"1000111",
    "D&A":"0000000", "D&M":"1000000",
    "D|A":"0010101", "D|M":"1010101"
}

DEST = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

def first_pass(lines):
    symbols = PREDEFINED.copy()
    cleaned = []
    address = 0

    for line_no, raw in enumerate(lines, 1):
        line = raw.split("//")[0].strip()

        if not line:
            continue

        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]

            if not re.fullmatch(r"[A-Za-z_.$:][\w.$:]*", label):
                raise ValueError(f"Invalid label at line {line_no}: {line}")

            if label in symbols:
                print(f"WARNING: Duplicate label '{label}' at line {line_no}")
            else:
                symbols[label] = address

        else:
            cleaned.append((line_no, line))
            address += 1

    return symbols, cleaned


def second_pass(symbols, instructions):
    output = []
    next_variable = 16

    for line_no, line in instructions:

        try:
            if line.startswith("@"):
                value = line[1:].strip()

                if value.isdigit():
                    number = int(value)
                else:
                    if not re.fullmatch(r"[A-Za-z_.$:][\w.$:]*", value):
                        raise ValueError("Invalid symbol")

                    if value not in symbols:
                        symbols[value] = next_variable
                        next_variable += 1

                    number = symbols[value]

                if number < 0 or number > 32767:
                    raise ValueError("A-instruction value out of range")

                output.append(format(number, "016b"))

            else:
                parts = line.split(";")

                if len(parts) > 2:
                    raise ValueError("Invalid jump instruction")

                left = parts[0].strip()
                jump = parts[1].strip() if len(parts) == 2 else ""

                if "=" in left:
                    if left.count("=") != 1:
                        raise ValueError("Invalid destination")
                    dest, comp = left.split("=")
                    dest = dest.strip()
                    comp = comp.strip()
                else:
                    dest = ""
                    comp = left.strip()

                if dest not in DEST:
                    raise ValueError("Invalid destination")

                if comp not in COMP:
                    raise ValueError("Invalid computation")

                if jump not in JUMP:
                    raise ValueError("Invalid jump")

                binary = "111" + COMP[comp] + DEST[dest] + JUMP[jump]
                output.append(binary)

        except Exception as error:
            raise ValueError(f"Error at line {line_no}: {line} ({error})")

    return output


def assemble(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    symbols, instructions = first_pass(lines)
    machine_code = second_pass(symbols, instructions)

    output_file = filename.rsplit(".", 1)[0] + ".hack"

    with open(output_file, "w") as file:
        file.write("\n".join(machine_code) + "\n")

    print("Assembly successful!")
    print("Output file:", output_file)
    print("Total instructions:", len(machine_code))


print("Two-Pass Assembler created successfully!")

import re

def unify(C):
    if not C:
        return []

    (S, T), *C_prime = C

    if S == T:
        return unify(C_prime)
    elif isinstance(S, str) and S not in FV(T):
        substitution = {S: T}
        return [(S, T)] + unify([(apply_substitution(substitution, p), apply_substitution(substitution, q)) for p, q in C_prime])
    elif isinstance(T, str) and T not in FV(S):
        substitution = {T: S}
        return [(T, S)] + unify([(apply_substitution(substitution, p), apply_substitution(substitution, q)) for p, q in C_prime])
    elif is_valid_type(S) and is_valid_type(T):
        subconstraints = get_subconstraints(S, T)
        if subconstraints:
            return unify(C_prime + subconstraints)
        else:
            return "No se puede unificar las restricciones"
    else:
        return "No se puede unificar las restricciones"



def apply_substitution(substitution, term):
    if isinstance(term, str):
        return substitution.get(term, term)
    elif isinstance(term, tuple):
        return tuple(apply_substitution(substitution, t) for t in term)
    else:
        return term


def FV(term):
    if isinstance(term, str):
        return {term}
    elif isinstance(term, tuple):
        return FV(term[0]) | FV(term[1])
    else:
        return set()


def is_valid_type(type_str):
    if type_str in ("Nat", "Bool"):
        return True
    if isinstance(type_str, str) and re.match(r"^[a-zA-Z][a-zA-Z0-9]*$", type_str):
        return True
    if isinstance(type_str, str) and re.match(r"^[a-zA-Z][a-zA-Z0-9]*\s*->\s*[a-zA-Z][a-zA-Z0-9]*$", type_str):
        return True
    return False


def parse_type(type_str):
    if type_str == "Nat":
        return "Nat"
    if type_str == "Bool":
        return "Bool"
    if re.match(r"^[a-zA-Z][a-zA-Z0-9]*$", type_str):
        return type_str
    if re.match(r"^[a-zA-Z][a-zA-Z0-9]*\s*->\s*[a-zA-Z][a-zA-Z0-9]*$", type_str):
        match = re.match(r"^([a-zA-Z][a-zA-Z0-9]*)\s*->\s*([a-zA-Z][a-zA-Z0-9]*)$", type_str)
        if match:
            return (parse_type(match.group(1)), parse_type(match.group(2)))
    raise ValueError(f"Invalid type: {type_str}")


def get_subconstraints(S, T):
    if isinstance(S, str) and isinstance(T, str):
        return [(S, T)]
    elif isinstance(S, tuple) and isinstance(T, tuple):
        return [(S[0], T[0]), (S[1], T[1])]
    else:
        return []


def read_constraints(filename):
    constraints = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            constraint = line.strip().split("=")
            constraints.append((parse_type(constraint[0].strip()), parse_type(constraint[1].strip())))
    return constraints


def main():
    filename = input("Ingrese el nombre del archivo: ")
    constraints = read_constraints(filename)
    result = unify(constraints)
    if result == "fail":
        print("No se puede unificar las restricciones.")
    else:
        print(result)


if __name__ == '__main__':
    main()

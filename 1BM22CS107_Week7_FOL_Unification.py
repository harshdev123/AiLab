def is_variable(term):
    """Check if the term is a variable."""
    return isinstance(term, str) and term.islower() and len(term) == 1


def occurs_check(var, term):
    """Check if a variable occurs in a term."""
    if var == term:
        return True
    if isinstance(term, tuple):  
        return any(occurs_check(var, sub_term) for sub_term in term[1:])
    return False


def unify(psi1, psi2, subst=None):
    """Unify two terms psi1 and psi2."""
    if subst is None:
        subst = {}

  
    if psi1 == psi2:
        return subst

    if is_variable(psi1):
        return unify_variable(psi1, psi2, subst)


    if is_variable(psi2):
        return unify_variable(psi2, psi1, subst)

    if isinstance(psi1, tuple) and isinstance(psi2, tuple):
        if psi1[0] != psi2[0]:  
            return None

     
        if len(psi1) != len(psi2):
            return None

     
        for arg1, arg2 in zip(psi1[1:], psi2[1:]):
            subst = unify(arg1, arg2, subst)
            if subst is None:  # Step 5(b)
                return None
        return subst

 
    return None


def unify_variable(var, term, subst):
    """Unify a variable with a term."""
    if var in subst: 
        return unify(subst[var], term, subst)
    elif isinstance(term, str) and term in subst:  
        return unify(var, subst[term], subst)
    elif occurs_check(var, term):  
        return None
    else:  
        subst[var] = term
        return subst



def parse_term(term_str):
    """
    Parse a string representation of a term into a tuple or variable.
    For example:
        "f(x, y)" -> ("f", "x", "y")
        "x" -> "x"
    """
    term_str = term_str.strip()
    if "(" in term_str and term_str.endswith(")"):
        predicate = term_str[:term_str.index("(")]
        arguments = term_str[term_str.index("(") + 1:-1].split(",")
        return (predicate,) + tuple(arg.strip() for arg in arguments)
    return term_str  


psi1 = input("Enter Ψ1: ").strip()
psi2 = input("Enter Ψ2: ").strip()


term1 = parse_term(psi1)
term2 = parse_term(psi2)

result = unify(term1, term2)
if result is not None:
    print("Unification Successful!")
    print("Substitutions:")
    for var, value in result.items():
        print(f"{var} -> {value}")
else:
    print("Unification Failed!")

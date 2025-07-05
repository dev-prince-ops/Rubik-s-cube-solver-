import kociemba

def solve_cube(cube_string):
    """Generate solution using two-phase algorithm"""
    try:
        solution=kociemba.solve(cube_string)
        return solution
    except ValueError as e:
        print(f"Invalid cube state: {e}")
        return None

def format_solution(solution):
    """Format solution for easier reading"""
    if not solution:
        return "No solution found"
    
    moves=solution.split()
    formatted=[]
    step=1
    
    for move in moves:
        # Convert to standard notation
        if move.endswith("2"):
            formatted.append(f"{step}. {move[0]}²")
        elif move.endswith("'"):
            formatted.append(f"{step}. {move[0]}'")
        else:
            formatted.append(f"{step}. {move}")
        step+=1
    
    return "\n".join(formatted)

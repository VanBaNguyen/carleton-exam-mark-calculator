import ast
import operator

def safe_eval(expr):
    """Safely evaluate an arithmetic expression (numbers, +, -, *, /, parentheses)."""
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        elif isinstance(node, ast.BinOp) and type(node.op) in ops:
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -_eval(node.operand)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            return +_eval(node.operand)
        else:
            raise ValueError(f"Unsupported expression: {ast.dump(node)}")

    tree = ast.parse(expr.strip(), mode='eval')
    return _eval(tree)

def percentages():
    flag = True

    while flag:
        try:
            mark_earned = safe_eval(input("The weight of all marks before the exam: "))

            mark_loss_string = input("Marks Lost (in %): ")
            mark_loss = 0.0 if mark_loss_string == "" else safe_eval(mark_loss_string)

            bonus_string = input("Enter the weight of any bonuses: ")
            bonus = 0

            if not bonus_string == "":
                bonus = safe_eval(bonus_string)
            flag = False
        except Exception:
            print("\n\nlol misinput TRY AGAIN\n\n")

    exam_weight = 100 - mark_earned

    current_mark = mark_earned - mark_loss + bonus
    
    def calculate_required(target):
        if exam_weight <= 0:
            return 0.0 if current_mark >= target else 100.0
        return max(0.0, round(((target - current_mark) / exam_weight) * 100, 2))

    mark_needed = calculate_required(90)
    mark_a = calculate_required(85)
    mark_a_minus = calculate_required(80)
    mark_b_plus = calculate_required(77)
    mark_b = calculate_required(73)
    pass_grade = calculate_required(50)

    marks = [mark_needed, mark_a, mark_a_minus]

    print(f"You need {mark_needed}% on the final exam for an A+")

    print(f"\nYou need {mark_a}% on the final exam for an A")

    print(f"You need {mark_a_minus}% on the final exam for an A-")

    print(f"You need {mark_b_plus}% on the final exam for a B+")
    print(f"You need {mark_b}% on the final exam for a B")

    if not pass_grade <= 0:
        print(f"You need {pass_grade}% on the final exam to pass")

    return {
        "A+": mark_needed,
        "A": mark_a,
        "A-": mark_a_minus,
        "Pass": pass_grade
    }

if __name__ == "__main__":
    percentages()

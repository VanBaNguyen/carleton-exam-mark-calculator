def percentages():
    flag = True

    while flag:
        try:
            mark_earned = float(input("The weight of all marks before the exam: "))

            mark_loss_string = input("Marks Lost (in %): ")
            mark_loss = 0.0 if mark_loss_string == "" else float(mark_loss_string)

            bonus_string = input("Enter the weight of any bonuses: ")
            bonus = 0

            if not bonus_string == "":
                bonus = float(bonus_string)
            flag = False
        except Exception:
            print("\n\nlol misinput TRY AGAIN\n\n")

    exam_weight = 100 - mark_earned

    mark_needed = round(((90 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)

    mark_a = round(((85 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)
    mark_a_minus = round(((80 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)

    mark_b_plus= round(((77 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)
    mark_b= round(((73 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)

    pass_grade = round(((50 - (mark_earned - mark_loss + bonus))/exam_weight)*100, 2)

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

"""
Learning Path Curator + Study Planner Agent
Grounded by Foundry IQ – suggests learning resources and builds adaptive schedules.
"""


class PlannerAgent:

    def create_plan(self, certification, total_hours, skills, hours_per_day, hours_studied):
        """
        Generates an intelligent, adaptive study plan based on certification
        requirements, learner progress, and available daily capacity.
        """
        remaining_hours = max(total_hours - hours_studied, 0)
        days_needed     = max(remaining_hours // max(hours_per_day, 1), 1)
        weeks_needed    = (days_needed + 6) // 7

        output = []
        output.append("── Learning Path Curator Agent ─────────────────────────")
        output.append(f"  Certification Target : {certification}")
        output.append(f"  Required Hours       : {total_hours} hrs total")
        output.append(f"  Hours Completed      : {hours_studied} hrs")
        output.append(f"  Remaining Hours      : {remaining_hours} hrs")
        output.append(f"  Daily Study Capacity : {hours_per_day} hrs/day")
        output.append(f"  Estimated Completion : {days_needed} days (~{weeks_needed} week(s))")
        output.append("")
        output.append("── Core Skills Mapped (Foundry IQ – Grounded) ───────────")
        for i, skill in enumerate(skills, 1):
            output.append(f"  [{i}] {skill}")
        output.append("")
        output.append("── Adaptive Study Plan Generated ────────────────────────")

        if weeks_needed <= 1:
            output.append("  Week 1 : Intensive revision + mock tests")
        elif weeks_needed == 2:
            output.append("  Week 1 : Core concepts + hands-on labs")
            output.append("  Week 2 : Mock exams + targeted revision")
        else:
            output.append("  Week 1 : Core concepts and fundamentals")
            output.append("  Week 2 : Hands-on practice and labs")
            output.append(f"  Week {weeks_needed} : Mock exams + final revision")

        output.append("")
        output.append("  Study Strategy : Morning deep-focus sessions (Foundry IQ cited)")
        output.append("  Daily Pattern  : Theory → Practice → Review cycle")
        output.append("  Milestone      : Practice test at 75% completion")
        output.append("")
        output.append("  [Planner Agent] Plan finalized. Dispatching to Engagement Agent.")

        return output

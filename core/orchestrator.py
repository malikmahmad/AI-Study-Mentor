"""
Orchestrator – Central reasoning coordinator for AI Study Mentor.
Manages agent communication, reasoning loop, and decision routing.
"""


class Orchestrator:

    def run_reasoning_loop(self, score, threshold, cert, skills):
        """
        Triggered when assessment score is below pass threshold.
        Simulates multi-agent reasoning and optimization cycle.
        """
        gap       = threshold - score
        iterations = 1 if gap <= 10 else 2

        output = []
        output.append("── Orchestrator: Reasoning Loop Analysis ──────────────")
        output.append(f"  Current Score    : {score}%")
        output.append(f"  Required Score   : {threshold}%")
        output.append(f"  Performance Gap  : {gap}%")
        output.append(f"  Loop Iterations  : {iterations} optimization cycle(s)")
        output.append("")
        output.append("── Root Cause Analysis ─────────────────────────────────")

        if gap <= 5:
            output.append("  Diagnosis : Learner is close to threshold.")
            output.append("  Root Cause: Minor knowledge gaps in specific topics.")
            output.append("  Strategy  : 2-day targeted revision + 1 mock test.")
        elif gap <= 10:
            output.append("  Diagnosis : Moderate performance gap detected.")
            output.append("  Root Cause: Inconsistent practice and missed topics.")
            output.append("  Strategy  : 3-day revision + concept reinforcement sessions.")
        else:
            output.append("  Diagnosis : Significant readiness gap identified.")
            output.append("  Root Cause: Insufficient study hours and weak foundations.")
            output.append("  Strategy  : Full study plan restart with structured milestones.")

        output.append("")
        output.append("── Optimized Re-Learning Path ───────────────────────────")

        weak_skills = skills[:2] if len(skills) >= 2 else skills
        output.append(f"  Priority Focus Areas : {', '.join(weak_skills)}")
        output.append(f"  Additional Hours     : +{max(4, gap // 2)} hrs recommended")
        output.append(f"  Revised Target Score : {threshold}% within next 7 days")
        output.append("")
        output.append("  [Orchestrator] Updated plan dispatched to Study Planner Agent.")
        output.append("  [Orchestrator] Re-engagement reminders scheduled via Engagement Agent.")
        output.append("  [Orchestrator] Progress tracking resumed. Next assessment in 7 days.")

        return output
